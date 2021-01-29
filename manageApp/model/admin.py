from sqlalchemy.sql import func
from manageApp import db, ma
from .baseModel import BaseModel


class Admin(db.Model, BaseModel):
    """
        管理员数据表
    """
    __tablename__ = "admin"
    
    username = db.Column(db.VARCHAR(20), primary_key=True)
    password = db.Column(db.VARCHAR(100), nullable=False)
    email = db.Column(db.VARCHAR(100), unique=True, nullable=False)
    phone = db.Column(db.VARCHAR(20), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=func.now())
    updated_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime)
    
    def __init__(self, username, password, email, phone):
        self.username = username
        self.password = password
        self.email = email
        self.phone = phone
    
    def set_password(self, password):
        self.password = password
        db.session.commit()
    

class AdminSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Admin
        fields = ("username", "password", "email", "phone", "created_at", "updated_at", "deleted_at")