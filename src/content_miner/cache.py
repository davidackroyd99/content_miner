"""Provides functions that read and update the user cache"""

import configparser
from enum import Enum

_config = configparser.ConfigParser()
_CACHE_FP = "cache.ini"


class CacheKey(Enum):
    CONTENT_PATH = "content_path"
    KNOWN_WORDS_PATH = "known_words_path"
    DESTINATION_PATH = "destination_path"


def _build_cache():
    _config.read(_CACHE_FP)

    if len(_config.sections()) == 0:
        _config["cache"] = {}

    for key in CacheKey:
        if key.value not in _config["cache"].keys():
            _config["cache"][key.value] = ""


def read_key(key: CacheKey):
    return _config["cache"][key.value]


def update_key(key: CacheKey, value: str):
    _config["cache"][key.value] = value

    with open(_CACHE_FP, 'w') as configfile:
        _config.write(configfile)


_build_cache()  # build the cache when the module is imported
