# -*- coding: utf-8 -*-
# Created by wumingming on 2020-06-25
# Copyright (c) 2020 wumingming. All rights reserved.

from fastapi import APIRouter, Depends

from app.db.mongodb import AsyncIOMotorClient, get_database

router = APIRouter()


@router.get("/export")
async def excel_export(
        db: AsyncIOMotorClient = Depends(get_database)
):
    result = {"type": "export"}
    row = await db['python']['excel_data'].find_one({}, {"_id": 0})
    if row:
        result.update(row)
    return result


@router.post("/import")
async def excel_import(
        db: AsyncIOMotorClient = Depends(get_database)
):
    result = {"type": "import"}
    row = await db['python']['excel_data'].find_one({}, {"_id": 0})
    if row:
        result.update(row)
    return result