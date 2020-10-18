from os import environ
from .custom_exception import EnvironnementVariableNotFound


def get_env_var(variable_name):
    env_var = environ.get(variable_name)

    if env_var is None:
        raise EnvironnementVariableNotFound(
            f"You need a {variable_name} environnement variable."
        )

    return env_var
