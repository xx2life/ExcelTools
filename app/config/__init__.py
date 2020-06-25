# -*- coding: utf-8 -*-
# Created by wumingming on 2020-06-24
# Copyright (c) 2020 wumingming. All rights reserved.

import os

from starlette.datastructures import CommaSeparatedStrings
from databases import DatabaseURL


# BASE CONFIG
ALLOWED_HOSTS = CommaSeparatedStrings(os.getenv("ALLOWED_HOSTS", ""))

# API PREFIX
API_V1_STR = "/api"

# MongoDB
MAX_CONNECTIONS_COUNT = int(os.getenv("MAX_CONNECTIONS_COUNT", 10))
MIN_CONNECTIONS_COUNT = int(os.getenv("MIN_CONNECTIONS_COUNT", 10))

MONGODB_URL = os.getenv("MONGODB_URL","")
if not MONGODB_URL:
    MONGO_HOST = os.getenv("MONGO_HOST", "127.0.0.1")
    MONGO_PORT = int(os.getenv("MONGO_PORT", 27017))
    MONGO_USER = os.getenv("MONGO_USER", "")
    MONGO_PASS = os.getenv("MONGO_PASS", "")
    MONGO_DB = os.getenv("MONGO_DB", "")

    MONGODB_URL = DatabaseURL(
        f"mongodb://{MONGO_USER}:{MONGO_PASS}@{MONGO_HOST}:{MONGO_PORT}/{MONGO_DB}"
    )
else:
    MONGODB_URL = DatabaseURL(MONGODB_URL)