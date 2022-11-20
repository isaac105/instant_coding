import datetime
import jwt

from .models import Users
from server import application
from flask import request, session
from functools import wraps
from werkzeug.security import generate_password_hash,check_password_hash


def standard_response(status, message):
    return {'status': status, 'message': message}


def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = session.get("token")

        if not token or not session.get("user_idx") or not session.get("is_active"):
            return standard_response("success", "인증이 필요합니다.")
        try:
            data = jwt.decode(token, application.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = Users.query.filter_by(idx=data['idx']).first()
        except:
            return standard_response("fail", "로그인 할 수 없습니다. 다시 시도해주세요.")

        return f(current_user, *args, **kwargs)

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
                age=data['age'], phone=data['phone'], current_round=data['current_round'])
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
    if check_password_hash(user.pwd, data["pwd"]):
        token = jwt.encode(
            {'idx': user.idx, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=45)},
            application.config['SECRET_KEY'], "HS256")

        session["user_idx"] = user.idx
        session["token"] = token

        return standard_response('success', '로그인 성공')

    return standard_response('fail', '로그인 실패')


def signout_user():
    try:
        del session["user_idx"]
        del session["token"]

        return standard_response('success', '로그아웃 되었습니다.')
    except:
        return standard_response('fail', '이미 로그아웃 되었습니다.')

