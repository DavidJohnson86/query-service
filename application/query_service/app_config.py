"""Application configuration loading and validation module.
"""
import logging.config

logger = logging.getLogger(__name__)

ENDPOINT = "https://www.ecb.europa.eu/stats/eurofxref/eurofxref-hist.zip"

logging_config = {
    "version": 1,
    "formatters": {"f": {"format": "%(asctime)s %(name)-12s %(levelname)-8s %(message)s"}},
    "handlers": {"h": {"class": "logging.StreamHandler", "formatter": "f", "level": logging.INFO}},
    "root": {
        "handlers": ["h"],
        "level": logging.INFO,
    },
}

logging.config.dictConfig(logging_config)
