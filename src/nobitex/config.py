from dynaconf import Dynaconf  # type: ignore

settings = Dynaconf(
    envvar_prefix="DYNACONF",
    settings_files=["settings.toml", ".secrets.toml"],
)

KEY = settings.key
USERNAME = settings.username
PASSWORD = settings.password
TWO_FACTOR_AUTHENTICATION_CODE = settings.two_factor_authentication_code
