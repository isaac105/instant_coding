import json
import os

from flask import Flask, render_template, request, Response
from flask_migrate import Migrate
from impapp.models import db

application = Flask('instant_coding', static_url_path='/static', static_folder='static')
application.config.from_object('impapp.config.DevelopmentConfig')

db.init_app(application)
migrate = Migrate(application, db)


# API 응답용 함수 설정
def jsonify(data, status=200):
    class APIEncoder(json.JSONEncoder):
        def default(self, o):
            if isinstance(o, int) or isinstance(o, dict):
                return o
            else:
                return str(o)

    return Response(json.dumps(data, cls=APIEncoder), status=status, mimetype='application/json; charset=utf-8')


@application.route('/api/whoami')
def whoami():
    return jsonify({'ip': request.remote_addr, 'headers': dict(request.headers)})


@application.route('/favicon.ico')
def favicon():
    return application.send_static_file("images/favicon.ico")


@application.route('/signin')
def signin():
    return render_template("/user/signin.html")


@application.route("/")
def index():
    return render_template("/index.html")


@application.route("/lessons")
def lessonsStart():
    return render_template("/lessons.html")


@application.route("/lessons.html")
def lessons():
    return render_template("/lessons.html", path="/english/unit1/lesson1")


if __name__ == '__main__':
    application.run(host="0.0.0.0", port=5000, debug=True)
