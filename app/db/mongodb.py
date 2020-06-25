# -*- coding: utf-8 -*-
# Created by wumingming on 2020-06-25
# Copyright (c) 2020 wumingming. All rights reserved.

from motor.motor_asyncio import AsyncIOMotorClient


class DataBase:
    client: AsyncIOMotorClient = None


db = DataBase()


async def get_database() -> AsyncIOMotorClient:
    return db.client