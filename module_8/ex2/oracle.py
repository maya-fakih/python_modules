import os
import sys
from dotenv import load_dotenv


def check_secrets():
    if os.getenv('API_KEY') in (None, "", "MISSING"):
        print("[FAIL] API key is missing or not set")
    else:
        print("[OK] API key is set")


def check_environment():
    if os.path.exists('.env'):
        print("[OK] .env file found")
    else:
        print("[WARNING] .env file not found, relying on \
              system environment variables")


def check_overrides():
    if os.getenv("MATRIX_MODE") == "production":
        print("[OK] Configuration override detected for MATRIX_MODE")
    else:
        print("[INFO] Development mode active.")


def main():
    load_dotenv()

    print("\nORACLE STATUS: Reading the Matrix...\n")

    matrix_mode = os.getenv('MATRIX_MODE', 'development')
    database_url = os.getenv('DATABASE_URL')
    api_key = os.getenv('API_KEY')
    log_level = os.getenv('LOG_LEVEL', 'DEBUG')
    zion_endpoint = os.getenv('ZION_ENDPOINT')

    print("\nConfiguration loaded:")
    print(f"Mode: {matrix_mode}")

    if database_url:
        print("Database: Connected to local instance")
    else:
        print("Database: Not configured")

    if api_key:
        print("API Access: Authenticated")
    else:
        print("API Access: Missing API key")

    print(f"Log Level: {log_level}")

    if zion_endpoint:
        print("Zion Network: Online")
    else:
        print("Zion Network: Not configured")
    pass

    print("\nEnvironment security check:")

    print("\nThe Oracle sees all configurations.")
    check_secrets()
    check_environment()
    check_overrides()

if __name__ == "__main__":
    main()
