from datetime import datetime
from flask import url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
# from flask import Column, String, Integer, ForeignKey
from werkzeug.security import generate_password_hash, check_password_hash
# 注意这里不再传入 app 了
db = SQLAlchemy()


class BaseModel(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)



class User(BaseModel, UserMixin):
    ROLE_USER = 10
    ROLE_COMPANY = 20 # 企业
    ROLE_ADMIN = 30

    __tablename__ = 'user'

    username = db.Column(db.String(16), index=True, unique=True, nullable=False)
    email = db.Column(db.String(32), unique=True, index=True, nullable=False)
    _password = db.Column('password',db.String(256))
    role = db.Column(db.Integer, default=ROLE_USER)
    nickname = db.Column(db.String(32), index=True, nullable=False)
    disabled = db.Column(db.Boolean, default=False) # 是否被禁用
    def __repr__(self):
        return 'name:{}'.format(self.nickname)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, pwd):
        self._password = generate_password_hash(pwd)

    @property
    def is_admin(self):
        return self.role == User.ROLE_ADMIN

    def check_password(self, pwd):
        return check_password_hash(self._password, pwd)

class UserInfo(BaseModel):
    __tablename__ = 'user_info'
    user_id = db.Column(db.Integer, index=True, unique=True, nullable=False)
    phone = db.Column(db.String(11), index=True)
    location = db.Column(db.String(128))
    degree1 = db.Column(db.String(128)) # 高中,大专,时间写在一起
    degree2 = db.Column(db.String(128)) # 本科
    degree3 = db.Column(db.String(128)) # 硕士
    degree4 = db.Column(db.String(128)) # 博士
    degree5 = db.Column(db.String(128)) # 其他
    career_exp1 = db.Column(db.String(1024)) # 工作经历
    career_exp2 = db.Column(db.String(1024)) # 工作经历
    career_exp3 = db.Column(db.String(1024)) # 工作经历
    career_exp4 = db.Column(db.String(1024)) # 工作经历
    career_exp5 = db.Column(db.String(1024)) # 工作经历
    career_exp6 = db.Column(db.String(1024)) # 工作经历
    career_exp7 = db.Column(db.String(1024)) # 工作经历
    cv1_url = db.Column(db.String(128))  # 简历1的地址
    cv2_url = db.Column(db.String(128))  # 简历2的地址
    cv3_url = db.Column(db.String(128))  # 简历3的地址
    cv1_open = db.Column(db.Boolean)  # 简历1是否公开
    cv2_open = db.Column(db.Boolean)  # 简历2是否公开
    cv3_open = db.Column(db.Boolean)  # 简历3是否公开


    def __repr__(self):
        return 'name:{}'.format(self.nickname)




class Job(BaseModel):
    __tablename__ = 'job'
    name = db.Column(db.String(64), index=True, unique=True, nullable=False)
    description = db.Column(db.String(64), unique=True, index=True, nullable=False)
    company_id = db.Column(db.Integer, index=True)
    salary_low = db.Column(db.Integer)
    salary_high = db.Column(db.Integer)
    location = db.Column(db.String(128))
    exp_req1= db.Column(db.String(128))
    exp_req2= db.Column(db.String(128))
    exp_req3= db.Column(db.String(128))
    exp_req4= db.Column(db.String(128))
    exp_req5= db.Column(db.String(128))
    exp_req6= db.Column(db.String(128))
    exp_req7= db.Column(db.String(128))
    exp_req8= db.Column(db.String(128))
    exp_req9= db.Column(db.String(128))
    exp_req10= db.Column(db.String(128))
    disabled = db.Column(db.Boolean, default=False)  # 是否被下线

    def __repr__(self):
        return 'name:{}'.format(self.name)


class Company(BaseModel):
    __tablename__ = 'company'
    name = db.Column(db.String(64), index=True, unique=True, nullable=False)
    description = db.Column(db.String(64), unique=True, index=True, nullable=False)
    logo_url = db.Column(db.String(128))
    web_site = db.Column(db.String(64))
    location = db.Column(db.String(128))

    def __repr__(self):
        return 'name:{}'.format(self.name)


class UserApply(BaseModel):

    __tablename__ = 'user_apply'

    user_id = db.Column(db.Integer)
    company_id = db.Column(db.Integer)
    job_id = db.Column(db.Integer)





