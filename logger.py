import logging
import os

LOG_DIR = os.path.join(os.path.dirname(__file__), "logs")
os.makedirs(LOG_DIR, exist_ok=True)

APPLICATION_LOG = os.path.join(LOG_DIR, "application.log")
ERROR_LOG = os.path.join(LOG_DIR, "error.log")


def get_logger(name: str = "app") -> logging.Logger:
    """Create and configure a logger with file and console handlers.

    Sets up three handlers: application.log (DEBUG+), error.log (WARNING+),
    and console output (INFO+). Each handler uses a human-readable format
    with timestamp, level, filename, and message.

    Args:
        name: The name identifier for the logger. Defaults to "app".

    Returns:
        A configured logging.Logger instance.
    """
    logger = logging.getLogger(name)

    if logger.handlers:
        return logger

    logger.setLevel(logging.DEBUG)

    app_handler = logging.FileHandler(APPLICATION_LOG)
    app_handler.setLevel(logging.DEBUG)

    error_handler = logging.FileHandler(ERROR_LOG)
    error_handler.setLevel(logging.WARNING)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(filename)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    app_handler.setFormatter(formatter)
    error_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(app_handler)
    logger.addHandler(error_handler)
    logger.addHandler(console_handler)

    return logger
