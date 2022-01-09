# Copyright Contributors to the Amundsen project.
# SPDX-License-Identifier: Apache-2.0

import os
from typing import Dict, List, Set  # noqa: F401


class MatchRuleObject:
    def __init__(self,
                 schema_regex=None,  # type: str
                 table_name_regex=None,   # type: str
                 ) -> None:
        self.schema_regex = schema_regex
        self.table_name_regex = table_name_regex


class Config:
    LOG_FORMAT = '%(asctime)s.%(msecs)03d [%(levelname)s] %(module)s.%(funcName)s:%(lineno)d (%(process)d:' \
                 + '%(threadName)s) - %(message)s'
    LOG_DATE_FORMAT = '%Y-%m-%dT%H:%M:%S%z'
    LOG_LEVEL = 'INFO'

    # Path to the logging configuration file to be used by `fileConfig()` method
    # https://docs.python.org/3.7/library/logging.config.html#logging.config.fileConfig
    # LOG_CONFIG_FILE = 'app/logging.conf'
    LOG_CONFIG_FILE = None

    COLUMN_STAT_ORDER = None  # type: Dict[str, int]

    UNEDITABLE_SCHEMAS = set()  # type: Set[str]

    UNEDITABLE_TABLE_DESCRIPTION_MATCH_RULES = []  # type: List[MatchRuleObject]

    # Number of popular tables to be displayed on the index/search page
    POPULAR_TABLE_COUNT = 4  # type: int

    # Request Timeout Configurations in Seconds
    REQUEST_SESSION_TIMEOUT_SEC = 3

    # Frontend Application
    FRONTEND_BASE = ''


class LocalConfig(Config):
    DEBUG = False
    TESTING = False
    LOG_LEVEL = 'DEBUG'

    FRONTEND_PORT = '1919'

    # If installing using the Docker bootstrap, this should be modified to the docker host ip.
    LOCAL_HOST = '0.0.0.0'

    FRONTEND_BASE = os.environ.get('FRONTEND_BASE',
                                   'http://{LOCAL_HOST}:{PORT}'.format(
                                       LOCAL_HOST=LOCAL_HOST,
                                       PORT=FRONTEND_PORT))

    MYSQL_HOST=os.environ.get('MYSQL_HOST')
    MYSQL_PORT=int(os.environ.get('MYSQL_PORT', 3306))
    MYSQL_USER=os.environ.get('MYSQL_USER')
    MYSQL_PASSWORD=os.environ.get('MYSQL_PASSWORD')
    MYSQL_DB=os.environ.get('MYSQL_DB')
