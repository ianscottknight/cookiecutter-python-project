from __future__ import annotations
from typing import TYPE_CHECKING, List, Tuple, Dict, Optional, Union, Any
if TYPE_CHECKING:
    pass

import sys
import logging


logger = logging.getLogger(__name__)
logging_formatter = logging.Formatter(
    "%(asctime)s::%(levelname)s::%(message)s", "%Y-%m-%d %H:%M:%S"
)


def get_logger(name: str = __name__, log_file_path: str = None, debug: bool = False) -> logging.Logger:
    """
    Configure and return a logger for a script, module, etc.

    Args:
        name (str, optional): Name of the logger. Default is the module's name.
        log_file_path (str, optional): Path to the log file. If not provided, logging to a file is disabled.
        debug (bool, optional): Whether to set the logger to debug mode. Default is False.

    Returns:
        logging.Logger: Configured logger instance.
    """
    # Create a logger specific to this script/module
    logger = logging.getLogger(name)

    # Set logger level based on the debug flag
    logger.setLevel(logging.DEBUG if debug else logging.INFO)

    # Check if the logger already has handlers to avoid duplicate logs
    if not logger.handlers:
        # Configure stream handler for console output
        sh = logging.StreamHandler(sys.stdout)
        sh.setLevel(logging.DEBUG if debug else logging.INFO)
        sh.setFormatter(logging_formatter)
        logger.addHandler(sh)

        # Configure file handler if log_file_path is provided
        if log_file_path:
            fh = logging.FileHandler(log_file_path)
            fh.setLevel(logging.DEBUG)
            fh.setFormatter(logging_formatter)
            logger.addHandler(fh)

    return logger
