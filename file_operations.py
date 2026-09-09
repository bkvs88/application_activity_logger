import os
from logger import get_logger

logger = get_logger("file_ops")

SAMPLE_DIR = os.path.join(os.path.dirname(__file__), "data")
os.makedirs(SAMPLE_DIR, exist_ok=True)


def read_file() -> None:
    """Read and display the contents of a file.

    Prompts for a filename and reads it from the data/ directory.
    Handles missing files, empty files, and permission errors.
    Logs warnings and errors for failure cases.
    """
    logger.debug("File read operation started")
    try:
        filename = input("Enter filename to read: ").strip()
        filepath = os.path.join(SAMPLE_DIR, filename)

        if not os.path.exists(filepath):
            logger.error(f"File could not be opened: {filename}")
            print(f"Error: File '{filename}' not found.")
            return

        with open(filepath, "r") as f:
            content = f.read()

        if not content:
            logger.warning("File was empty")
            print("File is empty.")
        else:
            logger.info(f"File read successfully: {filename}")
            print(f"File contents:\n{content}")
    except PermissionError:
        logger.error(f"Permission denied reading file: {filename}")
        print(f"Error: Permission denied for '{filename}'.")
    except Exception as e:
        logger.critical(f"Unexpected application failure during file read: {e}")
        print("An unexpected error occurred while reading the file.")


def write_file() -> None:
    """Write user-provided content to a file.

    Prompts for a filename and content, then writes to the data/ directory.
    Handles permission errors and logs the operation result.
    """
    logger.debug("File write operation started")
    try:
        filename = input("Enter filename to write: ").strip()
        filepath = os.path.join(SAMPLE_DIR, filename)
        content = input("Enter content to write: ")

        with open(filepath, "w") as f:
            f.write(content)

        logger.info(f"File written successfully: {filename}")
        print(f"Content written to '{filename}'.")
    except PermissionError:
        logger.error(f"Permission denied writing file: {filename}")
        print(f"Error: Permission denied for '{filename}'.")
    except Exception as e:
        logger.critical(f"Unexpected application failure during file write: {e}")
        print("An unexpected error occurred while writing the file.")
