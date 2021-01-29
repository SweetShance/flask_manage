from sqlalchemy.sql importort 
from manageApp import db, ma
from .baseModel import BaseModel


class Product(db.Model, BaseModel):
    """
        产品信息表
    """
    __tablename__ = "product"
    product_code = db.Column(db.VARCHAR(20), primary_key=True, comment="产品编号")
    title = db.Column(db.VARCHAR(20), unique=True, comment="产品名")
    pay = db.Column(db.DOUBLE, default=0, comment="价钱")
    created_at = db.Column(db.DateTime， server_default=fun.now())
    updated_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime)
    
    def __init__(self, product_code, title, pay):
        self.product_code = product_code
        self.title = title
        self.pay = pay
    

class ProductSchema(ma.SQLALchemySchema):
    class Meta:
        model = Product
        fields = ("product_code", "title", "pay", "created_at", "updated_at", "deleted_at")