import logging
import json
import sys

from loguru import logger


class InterceptHandler(logging.Handler):
    level_names = {
        50: 'CRITICAL',
        40: 'ERROR',
        30: 'WARNING',
        25: 'SUCCESS',
        20: 'INFO',
        10: 'DEBUG',
        5: 'TRACE',
        0: 'NOTSET',
    }

    def emit(self, record):
        try:
            level = logger.level(record.levelname).name
        except AttributeError:
            level = self.level_names[record.levelno]

        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(level, record.getMessage())


def init_logging(file_path: str, to_cli=True):
    """
    Setting up logging.
        - file_path - path to config file
        - to_cli: default = True - write to console

    The configuration is done via file_path.
    You need to specify "rotation", "retention" for logoru in the root of the json file.
    For each logger (default_logger, middleware_logger),
    you need to specify "serialize", "level" and "format",
    and optionally you can specify the path to the file for this particular logger.

    """
    logger.remove()
    logging.basicConfig(handlers=[InterceptHandler()], level=0)
    for log in ['uvicorn',
                'uvicorn.access'
                'uvicorn.error',
                'fastapi']:
        logging.getLogger(log).handlers = [InterceptHandler()]

    with open(file_path) as config_file:
        config = json.load(config_file)

    middleware_config = config["middleware_logger"]
    logger.add(
        middleware_config.get("path", config['path']),
        level=middleware_config['level'].upper(),
        format=middleware_config['format'],
        rotation=config['rotation'],
        retention=config['retention'],
        serialize=middleware_config['serialize'],
        compression='zip',
        enqueue=True,
        backtrace=True,
        filter=lambda record: "type" in record["extra"] and "middleware" == record["extra"]["type"]
    )

    default_config = config["default_logger"]
    logger.add(
        default_config.get("path", config['path']),
        level=default_config['level'].upper(),
        format=default_config['format'],
        rotation=config['rotation'],
        retention=config['retention'],
        serialize=default_config['serialize'],
        compression='zip',
        enqueue=True,
        backtrace=True,
        filter=lambda record: "type" not in record["extra"]
    )

    if to_cli is True:
        logger.add(
            sys.stdout,
            enqueue=True,
            backtrace=True,
            level=default_config['level'].upper(),
        )

    debug_config = config["debug_logger"]
    logger.add(
        debug_config.get("path", config['path']),
        level=debug_config['level'].upper(),
        format=debug_config['format'],
        rotation=config['rotation'],
        retention=config['retention'],
        serialize=debug_config['serialize'],
        compression='zip',
        enqueue=True,
        backtrace=True
    )

