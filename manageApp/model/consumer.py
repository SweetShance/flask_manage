from sqlalchemy.sql import func
from marshmallow_sqlalchemy.fields import Nested
from manageApp import db, ma
from .members import MemberSchema
from .product import ProductSchema
from .baseModel import BaseModel


class Consumer(db.Model, BaseModel):
    """
        会员消费记录
    """
    __tablename__ = "consumer"
    id = db.Column(db.BigInteger, primary_key=True)
    phone = db.Column(db.VARCHAR(20), db.ForeignKey("members.phone"), nullable=False, comment="会员手机号")
    product_code = db.Column(db.VARCHAR(20), db.ForeignKey("product.product_code"), nullable=False, comment="产品编号")
    created_at = db.Column(db.DateTime, server_default=fun.now())
    updated_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime)
    members = db.relationship("Members", backref=db.backref("consumer"))
    product = db.relationship("Product", backref=db.backref("consumer"))
        
    def __init__(self, phone, product_code):
        self.phone = phone
        self.product_code = product_code


class ConsumerSchema(ma.SQLALchemySchema):
    class Meta:
        model = Consumer
        fields = ("phone", "product_code", "created_at", "updated_at", 
                  "created_at", "deleted_at")
    
    members = Nested(MemberSchema, only=["phone", "username"])
    product = Nested(ProductSchema, only=["title", "pay"])
    