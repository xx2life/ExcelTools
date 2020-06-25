# -*- coding: utf-8 -*-
# Created by wumingming on 2020-06-25
# Copyright (c) 2020 wumingming. All rights reserved.

from fastapi import APIRouter

from app.api.excel_tools import router as router_excel

router = APIRouter()
router.include_router(router_excel, tags=["excel_tools"], prefix="/excel")
