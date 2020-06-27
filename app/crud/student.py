# -*- coding: utf-8 -*-
# Created by wumingming on 2020-06-27
# Copyright (c) 2020 wumingming. All rights reserved.
from motor.motor_asyncio import AsyncIOMotorClient


async def find_student(db: AsyncIOMotorClient):
    students = []
    rows = db['python']['excel_data'].find({"_key": "student"}, {"_id": 0})

    async for row in rows:
        students.append(row)

    return students
