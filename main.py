from logger import get_logger
from auth import login, logout
from calculator import calculate
from file_operations import read_file, write_file

logger = get_logger("main")


def display_menu() -> None:
    """Display the main application menu with available options."""
    print("\n===== Application Menu =====")
    print("1. Login")
    print("2. Calculate")
    print("3. Read a File")
    print("4. Write a File")
    print("5. Logout")
    print("============================")


def main() -> None:
    """Run the main application loop.

    Displays a menu and dispatches user choices to the appropriate
    module functions. Tracks the logged-in user state and requires
    authentication before accessing calculator or file operations.
    Handles keyboard interrupts gracefully.
    """
    logger.info("Application started")
    logged_in_user = None

    while True:
        display_menu()
        try:
            choice = input("Enter your choice (1-5): ").strip()
        except (EOFError, KeyboardInterrupt):
            logger.warning("User interrupted the application")
            print("\nExiting application.")
            break

        if choice == "1":
            if logged_in_user:
                print(f"Already logged in as {logged_in_user}.")
                logger.warning(f"Login attempted while already logged in as {logged_in_user}")
            else:
                logged_in_user = login()

        elif choice == "2":
            if not logged_in_user:
                print("Please login first.")
                logger.warning("Calculate attempted without login")
            else:
                calculate()

        elif choice == "3":
            if not logged_in_user:
                print("Please login first.")
                logger.warning("File read attempted without login")
            else:
                read_file()

        elif choice == "4":
            if not logged_in_user:
                print("Please login first.")
                logger.warning("File write attempted without login")
            else:
                write_file()

        elif choice == "5":
            if not logged_in_user:
                print("No user is logged in.")
                logger.warning("Logout attempted without active session")
            else:
                logout(logged_in_user)
                logged_in_user = None
            logger.info("Application ended")
            break

        else:
            logger.warning(f"Invalid menu choice: {choice}")
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.critical(f"Unexpected application failure: {e}")
        print("A critical error occurred. The application will now exit.")
