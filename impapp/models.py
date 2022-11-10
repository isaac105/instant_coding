# -*- coding: utf-8 -*-

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

__all__ = [
    # SQLAlchemy Table Class
    "Users", "Ranking"
]


class Users(db.Model):
    __tablename__ = 'users'
    idx = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    email = db.Column(db.Text, unique=True)
    pwd = db.Column(db.Text, nullable=False)
    name = db.Column(db.Text, nullable=False)
    age = db.Column(db.Text, nullable=False)
    phone = db.Column(db.Text)
    stat = db.Column(db.SMALLINT, nullable=False)
    reg_date = db.Column(db.DateTime(timezone='Asia/Seoul'), nullable=False)

    rel_ranking = db.relationship('Ranking', backref='users')

    def updateinfo(self, name=None, pwd=None, phone=None, stat=None):
        if name:
            self.name = name
        if pwd:
            self.pwd = pwd
        if phone:
            self.phone = phone
        if stat:
            self.stat = stat

    def __str__(self):
        return "name: {}\nemail: {}\nphone: {}\nstat: {}".format(self.name, self.email, self.phone, self.stat)


class Ranking(db.Model):
    idx = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    user_idx = db.Column(db.Integer, db.ForeignKey('users.idx'), nullable=True)
    hint_cnt = db.Column(db.Integer, nullable=False)
    clear_time = db.Column(db.Integer, nullable=False)
    reg_date = db.Column(db.DateTime(timezone='Asia/Seoul'), nullable=False)

    def __str__(self):
        return f"user_idx: {self.user_idx}\nclear_time: {self.clear_time}\nreg_date: {self.reg_date}"
