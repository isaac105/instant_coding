import datetime
import jwt

from .models import Users, Ranking
from flask import request, session, current_app
from werkzeug.security import generate_password_hash,check_password_hash


def standard_response(status, message):
    return {'status': status, 'message': message}


def token_required(f):
    def decorator():
        token = session.get("token")

        if not token or not session.get("user_idx"):
            return standard_response("success", "인증이 필요합니다.")
        try:
            data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = Users.query.filter_by(idx=data['idx']).first()
            if not current_user:
                return standard_response("fail", "로그인 정보를 확인해주세요.")
        except:
            return standard_response("fail", "로그인 할 수 없습니다. 다시 시도해주세요.")

        return f()

    return decorator


def signup_user():
    """
    request json example

    {
        "email": "test@gmail.com",
        "pwd": "1234",
        "name": "2호",
        "age": 25,
        "phone": "01056781234",
        "current_round": 1
    }
    """
    data = request.get_json()
    hashed_password = generate_password_hash(data['pwd'], method='sha256')

    if Users.query.filter_by(email=data["email"]).first():
        return standard_response('fail', '이메일이 중복됩니다. 다른 이메일을 입력해주세요.')

    user = Users()
    user.create(email=data['email'], pwd=hashed_password, name=data['name'],
                age=data['age'], phone='', current_round=0)
    return standard_response('success', '회원가입 성공')


def signin_user():
    """
    request json example

    {
        "email": "test@gmail.com",
        "pwd": "1234"
    }
    """
    data = request.get_json()
    user = Users.query.filter_by(email=data["email"]).first()
    if user and check_password_hash(user.pwd, data["pwd"]):
        token = jwt.encode(
            {'idx': user.idx, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=45)},
            current_app.config['SECRET_KEY'], "HS256")
        session["user_idx"] = user.idx
        session["name"] = user.name
        session["token"] = token

        return standard_response('success', '로그인 성공')

    return standard_response('fail', '로그인 실패')


def signout_user():
    try:
        del session["user_idx"]
        del session["name"]
        del session["token"]

        return standard_response('success', '로그아웃 되었습니다.')
    except:
        return standard_response('fail', '이미 로그아웃 되었습니다.')


@token_required
def update_user_round():
    """
    request json example

    {
        "user_idx": 1,
        "current_round": 3
    }
    """
    data = request.get_json()

    if session["user_idx"] == data['user_idx']:
        Users.update_round(data["user_idx"], data["current_round"])
        return standard_response('success', '라운드 정보 언데이트 성공')
    else:
        return standard_response('fail', '유저정보가 일치하지 않습니다.')


@token_required
def register_ranking():
    """
    request json example

    {
        "user_idx": 1,
        "hint_cnt": 3,
        "clear_time": 1234
    }
    """
    data = request.get_json()

    if session["user_idx"] == data['user_idx']:
        ranking = Ranking()
        ranking.create(user_idx=data['user_idx'], hint_cnt=data['hint_cnt'], clear_time=data['clear_time'])
        return standard_response('success', '랭킹등록 성공')
    else:
        return standard_response('fail', '유저정보가 일치하지 않습니다.')


def ranking_list():
    return Ranking.query.join(Users, Ranking.user_idx == Users.idx) \
        .add_columns(Users.name, Users.email)\
        .order_by(Ranking.hint_cnt.asc(), Ranking.clear_time.asc()).all()
