from logger import get_logger

logger = get_logger("auth")


def login() -> str | None:
    """Authenticate a user with username and password.

    Prompts for credentials and validates against hardcoded values
    (admin / admin123). Logs the result of each login attempt.

    Returns:
        The username string on success, or None on failure.
    """
    logger.debug("Login attempt started")
    try:
        username = input("Enter username: ").strip()
        password = input("Enter password: ").strip()

        if not username or not password:
            logger.warning("Empty username or password provided")
            print("Username and password cannot be empty.")
            return None

        if username == "admin" and password == "admin123":
            logger.info("User logged in")
            print(f"Welcome, {username}!")
            return username
        else:
            logger.warning("Invalid login attempt")
            print("Invalid credentials.")
            return None
    except Exception as e:
        logger.critical(f"Unexpected application failure during login: {e}")
        print("An unexpected error occurred during login.")
        return None


def logout(username: str) -> None:
    """End the user's active session.

    Logs the logout event and prints a goodbye message.

    Args:
        username: The name of the user logging out.
    """
    try:
        logger.info(f"User logged out: {username}")
        print(f"Goodbye, {username}!")
    except Exception as e:
        logger.critical(f"Unexpected application failure during logout: {e}")
        print("An unexpected error occurred during logout.")
