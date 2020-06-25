# -*- coding: utf-8 -*-
# Created by wumingming on 2020-06-24
# Copyright (c) 2020 wumingming. All rights reserved.

import time

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware

from app.api import router
from app.config import API_V1_STR,ALLOWED_HOSTS
from app.db.mongodb_utils import close_mongo_connection,connect_to_mongo


def get_app() -> FastAPI:
    app = FastAPI()

    origin = ALLOWED_HOSTS or ["*"]

    # 开启cors (跨源资源共享)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origin,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # 500字节以上开启gzip
    app.add_middleware(
        GZipMiddleware,
        minimum_size=500
    )

    # 添加中间件计算程序运行时间
    @app.middleware("http")
    async def add_process_time_helper(request: Request, call_next):
        start_time = time.time()
        response = await call_next(request)
        process_time = time.time() - start_time
        response.headers["X-Process-Time"] = str(process_time)
        return response

    app.include_router(router, prefix=API_V1_STR)

    # 添加数据库连接和关闭事件
    app.add_event_handler("startup",connect_to_mongo)
    app.add_event_handler("shutdown",close_mongo_connection)

    return app
