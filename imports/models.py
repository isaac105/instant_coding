import datetime

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
    current_round = db.Column(db.Integer)
    reg_date = db.Column(db.DateTime(timezone='Asia/Seoul'), nullable=False)

    rel_ranking = db.relationship('Ranking', backref='users')

    @staticmethod
    def create(**kwargs):
        kwargs.update({"stat": 1, "reg_date": datetime.datetime.now()})

        item = Users(**kwargs)

        db.session.add(item)
        db.session.flush()

        return item

    @staticmethod
    def update_round(user_idx: int, current_round: int):
        db.session.query(Users). \
            filter(Users.idx == user_idx). \
            update({'current_round': current_round})
        db.session.commit()

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

    @staticmethod
    def create(**kwargs):
        kwargs.update({"reg_date": datetime.datetime.now()})

        item = Ranking(**kwargs)

        db.session.add(item)
        db.session.flush()

        return item
