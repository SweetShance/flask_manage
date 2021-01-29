from datetime import datetime
from manageApp import db

class BaseModel:
    """
        抽象类， 所有的模型类继承次方法
    """
    now = datetime.now()

    def create(self):
        self.updated_at = self.now
        db.session.add(self)
        db.session.commit()

    def update(self):
        self.updated_at = self.now
        db.session.commit()
    
    def delete(self):
        self.deleted_at = self.now

    @classmethod
    def delete_many(cls, ids):
        delete_count = cls.query.filter(cls.id.in_(ids), cls.deleted_at.is_(None)).update(
            {cls.deleted_at: self.now}, synchronize_session=False
        )
        db.session.commit()
        return delete_count

if __name__ == "__main__":
    print("ooo")
    class test(BaseModel):
        def hello(self):
            print("yyy")
    a = test()
    a.hello()