from __future__ import annotations
from typing import TYPE_CHECKING, List, Tuple, Dict, Optional, Union, Any
if TYPE_CHECKING:
    pass

import logging
import logging.config
from logging.handlers import RotatingFileHandler


logger = logging.getLogger(__name__)


def setup_logging(stdout_level: Optional[str] = 'INFO', log_file: Optional[str] = None) -> None:
    """
    Set up logging for a Python application.

    Configures the root logger to log to console and optionally to a file.
    The console logging level is set by the stdout_level parameter (default: INFO).
    The file logging is activated by providing a file path to the log_file parameter.

    :param stdout_level: Optional log level for the console output.
                         Should be one of "debug", "info", "warning", "error", "critical".
                         Defaults to 'INFO'.
    :type stdout_level: str, optional
    :param log_file: Optional file path to activate file logging.
    :type log_file: str, optional
    :raises ValueError: If stdout_level is not a valid log level.
    :return: None
    :rtype: None
    """
    # Validate stdout_level
    stdout_level = stdout_level.upper()
    if stdout_level not in ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]:
        raise ValueError(f"Invalid stdout_level: {stdout_level}")

    # Create formatters
    simple_formatter = logging.Formatter('[%(levelname)s] %(asctime)s: %(message)s', datefmt='%Y-%m-%dT%H:%M:%S%z')
    detailed_formatter = logging.Formatter('[%(levelname)s|%(module)s|L%(lineno)d] %(asctime)s: %(message)s', datefmt='%Y-%m-%dT%H:%M:%S%z')

    # Create console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(stdout_level)
    console_handler.setFormatter(simple_formatter)

    # Create file handler if log_file is provided
    file_handler = None
    if log_file is not None:
        file_handler = RotatingFileHandler(log_file, maxBytes=10000000, backupCount=3)
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(detailed_formatter)

    # Get the root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)  # Setting root level to DEBUG to capture all levels

    # Clear existing handlers
    root_logger.handlers = []

    # Add handlers to the root logger
    root_logger.addHandler(console_handler)
    if file_handler:
        root_logger.addHandler(file_handler)
