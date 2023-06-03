# ///////////////////////////////////////////////////////////////////////////
# @file: config.py
# @time: 2022/12/14
# @author: Yuelin Xin
# @email: yuelinxin@miraclefactory.ai
# @organisation: Miracle Factory
# @url: https://miraclefactory.ai
# ///////////////////////////////////////////////////////////////////////////

# ///////////////////////////////////////////////////////////////////////////
# python import
from logging.config import dictConfig
# ///////////////////////////////////////////////////////////////////////////


log_config = dictConfig({
    "version": 1,
    "filters": {
        "backend_filter": {
            "backend_module": "backend",
        }
    },
    "formatters": {
        "standard": {"format": "%(asctime)s %(name)-12s %(levelname)-8s %(message)s"},
        "compact": {"format": "%(asctime)s %(message)s"},
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "standard",
            "stream": "ext://sys.stdout",
            "filters": ["backend_filter"],
        },
        "file": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "level": "DEBUG",
            "filename": "logs/app.log",
            "when": "D",
            "interval": 1,
            "formatter": "standard",
        },
    },
    "loggers": {
        "": {"handlers": ["console", "file"], "level": "DEBUG"},
        "flask": {"level": "WARNING"},
        "sqlalchemy": {"level": "WARNING"},
        "werkzeug": {"level": "WARNING"},
    },
    "disable_existing_loggers": False,
})
