import json
import os

from impapp import controllers
from impapp.models import db
from flask import Flask, render_template, request, jsonify, session
from flask_migrate import Migrate
from flask_session import Session

application = Flask('instant_coding', static_url_path='/static', static_folder='static')
application.config.from_object('impapp.config.DevelopmentConfig')

db.init_app(application)
migrate = Migrate(application, db)


def render_template_with_userinfo(template, **kwargs):
    if session.get('token'):
        kwargs.update({'is_logined': session['token'], 'name': session['name']})
    return render_template(template, **kwargs)


@application.route('/api/whoami')
def whoami():
    return jsonify({'ip': request.remote_addr, 'headers': dict(request.headers)})


@application.route('/favicon.ico')
def favicon():
    return application.send_static_file("images/favicon.ico")


# ------------------- User C: 회원가입 -------------------
# todo: 회원가입 탬플릿
@application.route('/signup', methods=['GET'])
def signup_template():
    return render_template_with_userinfo("/user/signup.html")


@application.route('/signup', methods=['POST'])
def signup():
    result = controllers.signup_user()
    return result["status"]


# ------------------- User R: 로그인 -------------------
@application.route('/signin', methods=['GET'])
def signin_template():
    return render_template_with_userinfo("/user/signin.html")


@application.route('/signin', methods=['POST'])
def signin():
    result = controllers.signin_user()
    return result["status"]


# ------------------- User U: 회원정보 수정은 미기획 (라운드 정보 수정은 추가) -------------------
@application.route('/signout', methods=['POST'])
def update_round_info():
    return jsonify(controllers.update_user_round())


# ------------------- User D: 로그아웃 -------------------
@application.route('/signout', methods=['GET'])
def signout():
    controllers.signout_user()
    return render_template_with_userinfo("/index.html")


# ------------------- Ranking C: 랭킹정보 추가 -------------------
@application.route('/rank', methods=['POST'])
def create_ranking():
    result = controllers.register_ranking()
    return result["status"]


# ------------------- Ranking R: 랭킹정보 조회 -------------------
@application.route('/rank', methods=['GET'])
def ranking_template():
    page = request.args.get('page', 1, int)
    return render_template_with_userinfo("/rank/list.html", rank_list=controllers.ranking_list(page))


@application.route("/")
def index():
    return render_template_with_userinfo("/index.html")


@application.route("/lessons")
def lessonsStart():
    return render_template_with_userinfo("/lessons.html")


@application.route("/gameStart")
def gameStart():
    return render_template_with_userinfo("/gameStart.html")


@application.route("/lessons.html")
def lessons():
    return render_template_with_userinfo("/lessons.html", path="/english/unit1/lesson1")


if __name__ == '__main__':
    server_session = Session(application)
    application.run(host="0.0.0.0", port=5000, debug=True)
