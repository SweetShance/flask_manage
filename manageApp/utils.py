from flask import make_response, jsonify
from enum import Enum 


class ErrCode(Enum):
    """
        2xx  成功  
        3xx  重定向  
        4xx  客户机中出现的错误 
        5xx  服务器中出现的错误  
    """
    success = {"200": "success"}
    
    def get_code(self):
        return list(self.value.keys())[0]
    
    def get_msg(self):
        return list(self.value.values())[0]


class ReturnValue:
    def return_value(status, data):
        errcode = ErrCode[status].get_code()
        errmsg = ErrCode[status].get_msg()
        return make_response(jsonify({ "errcode": errcode, "errmsg": errmsg, "data": data }))
    