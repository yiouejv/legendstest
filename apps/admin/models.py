# coding=utf-8
from sqlalchemy import Column, String, Boolean, DateTime, Integer
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from uuid import uuid4
from config import Base, session

# 创建模型
class Admin(Base):
    __tablename__ = 'admin'
    admin_uuid = Column(String(50), primary_key=True, nullable=False)
    admin_name = Column(String(50), nullable=False)
    admin_email = Column(String(50), unique=True)
    _admin_password = Column(String(100), nullable=False)
    admin_phone = Column(String(11), nullable=False, unique=True)
    admin_is_super = Column(Boolean, default=False)
    admin_is_delete = Column(Boolean, default=False)
    admin_create_time = Column(DateTime, default=datetime.now)

    def __init__(self,admin_uuid, admin_email, admin_name, admin_password, admin_phone, admin_is_super, admin_is_delete=None, admin_create_time=None):
        self.admin_uuid = admin_uuid
        self.admin_email = admin_email
        self.admin_name = admin_name
        self.admin_password = admin_password
        self.admin_phone = admin_phone
        self.admin_is_super = admin_is_super
        self.admin_is_delete = admin_is_delete
        self.admin_create_time = admin_create_time

    @property
    def admin_password(self):
        return self._admin_password

    @admin_password.setter
    def admin_password(self, raw_admin_password):
        self._admin_password = generate_password_hash(raw_admin_password)

    def check_admin_password(self, raw_admin_password):
        result = check_password_hash(self.admin_password, raw_admin_password)
        return result

    # def __len__(self):
        # return len(self.)


if __name__ == '__main__':
    # # 创建表
    Base.metadata.drop_all()
    Base.metadata.create_all()
    admin = Admin(admin_uuid=str(uuid4()),admin_name='yang', admin_email='yiouejv@126.com', admin_password='123456', admin_phone='15210212773', admin_is_super=True, admin_is_delete=False)
    session.add(admin)
    session.commit()
    pass

