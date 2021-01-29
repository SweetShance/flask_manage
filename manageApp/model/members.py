from sqlalchemy.sql import func
from manageApp import db, ma
from .baseModel import BaseModel
import manageApp

class Members(db.Model, BaseModel):
    """
        会员信息表
    """
    __tablename__ = "members"
    phone = db.Column(db.VARCHAR(11),  primary_key=True)
    username = db.Column(db.VARCHAR(20))
    money = db.Column(db.Double, default=0, comment="会员钱数")
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime)


    def __init__(self, phone, money=0, username=""):
        self.phone = phone
        self.username = username
        self.money = money


# 序列化返回结果
class MemberSchema(ma.SQLALchemySchema):
    class Meta:
        model = Members
        fields = ("phone", "username", "money", "created_at", "updated_at", "deleted_at")

