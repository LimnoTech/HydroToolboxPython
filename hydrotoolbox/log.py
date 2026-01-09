import logging
import sys

LOGGER = logging.getLogger(__name__)


def setup_logger():
    default_log_format = (
        "[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s"
    )
    default_date_format = "%Y-%m-%dT%H:%M:%SZ"

    logging.basicConfig(
        datefmt=default_date_format,
        format=default_log_format,
        stream=sys.stdout,
        level=logging.INFO,
    )

    LOGGER.debug("Logger has been set up.")
