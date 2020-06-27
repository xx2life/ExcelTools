# -*- coding: utf-8 -*-
# Created by wumingming on 2020-06-25
# Copyright (c) 2020 wumingming. All rights reserved.

import mimetypes
from datetime import datetime

from fastapi import APIRouter, Depends, File, UploadFile
from fastapi.responses import StreamingResponse

from app.db.mongodb import AsyncIOMotorClient, get_database
from app.utils.excel_tools import ExcelTools
from app.crud.student import find_student

router = APIRouter()


@router.get("/export")
async def excel_export(
        db: AsyncIOMotorClient = Depends(get_database)
):
    result = {"type": "export"}
    rows = await find_student(db)

    if rows:
        excel_tools = ExcelTools()

        excel = excel_tools.dict_to_excel(rows)

        file_name = 'devices' + '-' + datetime.now().strftime("%Y%m%d_%H%M%S") + '.xlsx'
        mime = mimetypes.guess_type(file_name)[0]

        return StreamingResponse(content=excel,
                                 media_type=mime,
                                 headers={'Content-Disposition': 'filename="%s"' % file_name})

    result.update({
        "status": "failed",
        "msg": "no data in mongodb"
    })
    return result


@router.post("/import")
async def excel_import(
        file: UploadFile = File(..., description="使用form表单上传文件")
):
    result = {"type": "import"}
    if file:
        excel_tool = ExcelTools()

        filename = file.filename
        ext = filename.split('.')[-1].replace('"', '')

        if ext not in ['xls', 'xlsx']:
            result.update({
                "status": "failed",
                "msg": "can't parse file format"
            })
            return result

        parsed_dict = excel_tool.excel_to_dict(file.file)
        result.update({
            "file_name": filename,
            "data": parsed_dict
        })

    return result
