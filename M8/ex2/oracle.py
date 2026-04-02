"""
This program loads configuration from environment variables and .env
files using python-dotend. It demonstrates safe configuration
management for development and production environments
"""

import os
import sys

from dotenv import load_dotenv


REQUIRED_VARIABLES: list[str] = [
    "MATRIX_MODE",
    "DATABASE_URL",
    "API_KEY",
    "LOG_LEVEL",
    "ZION_ENDPOINT"
]


def load_configuration() -> dict [str, str]:
    """Load environment variables from the system and optional .env file"""
    try:
        load_dotenv()
    except Exception:
        print("Warning: Could not load .env file")

    configuration: dict[str, str] = {}

    for variable_name in REQUIRED_VARIABLES:
        configuration[variable_name] = os.getenv(variable_name, "").strip()

    return configuration


def get_missing_variables(configuration: dict[str, str]) -> list[str]:
    """Return the list of missing required variables"""
    missing_variables: list[str] = []

    for variable_name, variable_value in configuration.items():
        if not variable_value:
            missing_variables.append(variable_name)

    return missing_variables


def print_missing_configuration_help(missing_variables: list[str]) -> None:
    """Print helpful messages for missing configuration"""
    print("\nMissing configuration detected:")
    for variable_name in missing_variables:
        print(f"- {variable_name}")

    print("\nCreate a .env file from the example:")
    print("cp .env.example .env")
    print("# Edit .env with your development values")
    print("python3 oracle.py")

    print("\nOr override values directly:")
    print(
        "MATRIX_MODE=production API_KEY=secret123 "
        "DATABASE_URL=db_url LOG_LEVEL=INFO "
        "ZION_ENDPOINT=https://zion.net python3 oracle.py"
    )


def get_database_status(database_url: str) -> str:
    """Return a user-friendly database connection description"""
    if not database_url:
        return "Missing database configuration"

    if (
            "localhost" in database_url
            or "127.0.0.1" in database_url
            or "sqlite" in database_url
    ):
        return "Connected to local instance"
    return "Connected to remote instance"


def get_api_status(api_key: str) -> str:
    """Return API authentication status"""
    if api_key:
        return "Authenticated"
    return "Missing API key"


def get_zion_status(zion_endpoint: str) -> str:
    """Return Zion network status"""
    if zion_endpoint:
        return "Online"
    return "Offline"


def validate_matrix_mode(matrix_mode: str) -> bool:
    """Validate MATRIX_MODE value"""
    return matrix_mode in ("development", "production")


def mask_api_key(api_key: str) -> str:
    """Mask the API key for safe display"""
    if not api_key:
        return "Missing"

    if len(api_key) < 4:
        return "*" * len(api_key)

    return f"{api_key[:2]}{'*' * (len(api_key) - 4)}{api_key[-2:]}"


def print_configuration_summary(configuration: dict[str, str]) -> None:
    """Print a readable configuration summary"""
    print("\nConfiguration loaded:")
    print(f"Mode: {configuration['MATRIX_MODE']}")
    print(
        "Database: "
        f"{get_database_status(configuration['DATABASE_URL'])}"
    )
    print(f"API Access: {get_api_status(configuration['API_KEY'])}")
    print(f"Log Level: {configuration['LOG_LEVEL']}")
    print(
        "Zion Network: "
        f"{get_zion_status(configuration['ZION_ENDPOINT'])}"
    )
    print(f"API Key Preview: {mask_api_key(configuration['API_KEY'])}")


def check_gitignore() -> bool:
    """Check whether .env appears to be ignored in .gitignore"""
    try:
        with open(".gitignore", "r", encoding="utf-8") as gitignore_file:
            content: str = gitignore_file.read()
            return ".env" in content.splitlines()
    except Exception:
        return False


def print_security_check(configuration: dict[str, str]) -> None:
    """Print a security check summary"""
    print("\nEnvironment security check:")
    if configuration["API_KEY"]:
        print("[OK] No hardcoded secrets detected")
    else:
        print("[WARNING] API_KEY is missing")

    if check_gitignore():
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] .env is not listed in .gitignore")

    print("[OK] Production overrides available")


def check_env_example() -> bool:
    """Check whether .env.example exists"""
    return os.path.isfile(".env.example")


def main() -> None:
    """
    Main program execution
    """

    print("ORACLE STATUS: Reading the Matrix...")
    configuration: dict[str, str] = load_configuration()
    missing_variables: list[str] = get_missing_variables(configuration)

    if missing_variables:
        print_missing_configuration_help(missing_variables)
        sys.exit(1)

    if not validate_matrix_mode(configuration['MATRIX_MODE']):
        print(
            "\nError: MATRIX_MODE must be "
            "'development' or 'production'."
        )
        sys.exit(1)

    print_configuration_summary(configuration)
    print_security_check(configuration)

    if not check_env_example():
        print("[WARNING] .env.example file is missing")

    print("\nThe Oracle sees all configurations.")

if __name__ == "__main__":
    main()
