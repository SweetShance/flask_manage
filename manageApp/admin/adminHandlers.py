
from flask import request, jsonify, make_response
from manageApp.model.admin import Admin
from manageApp.utils import ReturnValue
from manageApp import cache


def create_one():
    if not request.is_json:
        pass



def get_one(id):
    return ReturnValue.return_value("success", {"name": "刘勇"})


def get_list():
    return ReturnValue.return_value("success", {"name": name})


def update_one(id):
    pass


def delete_one(id):
    pass


def delete_many():
    pass 