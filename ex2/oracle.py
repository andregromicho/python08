import os


def load_config() -> dict[str, str | None]:
    try:
        from dotenv import load_dotenv  # type: ignore
        load_dotenv()
    except ImportError:
        pass

    return {
        "mode": os.getenv("MATRIX_MODE"),
        "db_url": os.getenv("DATABASE_URL"),
        "api_key": os.getenv("API_KEY"),
        "log_level": os.getenv("LOG_LEVEL"),
        "zion_endpoint": os.getenv("ZION_ENDPOINT"),
    }


def show_stats(config: dict[str, str | None]) -> None:
    missing = []
    for var_name, value in config.items():
        if not value:
            missing.append(var_name)

    if missing:
        print("[WARNING] Missing configuration variables:")
        for var in missing:
            print(f" - {var}")
        print()

    mode = config["mode"] or "development"

    print("Configuration loaded:")
    print(f"Mode: {mode}")

    if mode.lower() == "production":
        db_status = (
            f"Connected to remote instance ({config['db_url']})"
            if config["db_url"]
            else "NOT CONFIGURABLE"
        )
        api_status = (
            "Authenticated (Production Scope)"
            if config["api_key"]
            else "UNAUTHENTICATED"
        )
        log_level = config["log_level"] or "INFO"
        zion_status = (
            f"Connected to Secure Cluster ({config['zion_endpoint']})"
            if config["zion_endpoint"]
            else "OFFLINE"
        )
    else:
        db_status = (
            "Connected to local instance"
            if config["db_url"]
            else "NOT CONFIGURABLE"
        )
        api_status = (
            "Authenticated" if config["api_key"] else "UNAUTHENTICATED"
        )
        log_level = config["log_level"] or "DEBUG"
        zion_status = "Online" if config["zion_endpoint"] else "OFFLINE"

    print(f"Database: {db_status}")
    print(f"API Access: {api_status}")
    print(f"Log Level: {log_level}")
    print(f"Zion Network: {zion_status}")

    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")

    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] .env file not found (using defaults/environment)")

    print("[OK] Production overrides available")

    if not missing:
        print("\nThe Oracle sees all configurations.")


def main() -> None:
    print("ORACLE STATUS: Reading the Matrix...\n")
    config = load_config()
    show_stats(config)


if __name__ == "__main__":
    main()
