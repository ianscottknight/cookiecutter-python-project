from __future__ import annotations
from typing import TYPE_CHECKING, List, Tuple, Dict, Optional, Union, Any
if TYPE_CHECKING:
    pass

import logging
import logging.config
import pathlib

import yaml


logger = logging.getLogger(__name__)


def setup_logging(stdout_level: Optional[str] = None) -> None:
    """
    Set up logging for a Python application.

    Loads logging configuration from a YAML file and sets up the root logger.
    Optionally sets the logging level for the console output based on the provided
    stdout_level. If stdout_level is not provided, the log level defined in the YAML
    configuration is used.

    :param stdout_level: Optional log level for the console output.
                         Should be one of "debug", "info", "warning", "error", "critical".
                         If None, the log level defined in the YAML configuration is used.
    :type stdout_level: str, optional
    :raises ValueError: If stdout_level is not a valid log level.
    :return: None
    :rtype: None
    """
    # Validate stdout_level
    if stdout_level is not None and stdout_level.lower() not in ["debug", "info", "warning", "error", "critical"]:
        raise ValueError(f"Invalid stdout_level: {stdout_level}")

    # Load the logging configuration from YAML file and configure the root logger
    config_file = pathlib.Path(__file__).parent.joinpath("logging_configs/default_config.yaml")
    try:
        with open(config_file) as f_in:
            config = yaml.safe_load(f_in)
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Logging configuration file not found: {config_file}") from e
    except yaml.YAMLError as e:
        raise ValueError(f"Error parsing logging configuration file: {config_file}") from e

    # Set the logging level for the root logger if stdout_level is provided
    # Otherwise, the level is set by the logging configuration
    if stdout_level is not None:
        config['handlers']['console']['level'] = stdout_level.upper()

    logging.config.dictConfig(config)
