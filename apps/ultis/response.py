"""
please import models to ./migrations/env.py to Flask Migrate working
"""
from flask_sqlalchemy import Pagination
from marshmallow import Schema


def return_paginate(datas: Pagination, schema: Schema):
    return {
        "total_page": datas.total,
        "page": datas.page,
        "data": schema.dump(datas.items),
    }
