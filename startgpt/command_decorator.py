import functools
from typing import Any, Callable, Optional, TypedDict

from startgpt.config import Config
from startgpt.models.command import Command, CommandParameter

# Unique identifier for start-gpt commands
START_GPT_COMMAND_IDENTIFIER = "start_gpt_command"


class CommandParameterSpec(TypedDict):
    type: str
    description: str
    required: bool


def command(
    name: str,
    description: str,
    parameters: dict[str, CommandParameterSpec],
    enabled: bool | Callable[[Config], bool] = True,
    disabled_reason: Optional[str] = None,
) -> Callable[..., Any]:
    """The command decorator is used to create Command objects from ordinary functions."""

    def decorator(func: Callable[..., Any]) -> Command:
        typed_parameters = [
            CommandParameter(
                name=param_name,
                description=parameter.get("description"),
                type=parameter.get("type", "string"),
                required=parameter.get("required", False),
            )
            for param_name, parameter in parameters.items()
        ]
        cmd = Command(
            name=name,
            description=description,
            method=func,
            parameters=typed_parameters,
            enabled=enabled,
            disabled_reason=disabled_reason,
        )

        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            return func(*args, **kwargs)

        wrapper.command = cmd

        setattr(wrapper, START_GPT_COMMAND_IDENTIFIER, True)

        return wrapper

    return decorator
