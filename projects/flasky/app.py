from flask import Flask, request, current_app, make_response, abort


app = Flask(__name__)

def index() -> str:
    return '<h1>New app </h1>'

app.add_url_rule('/', 'index', index)

@app.route('/user/<name>')
def username(name: str) -> tuple[str, int]:
    userAgent = request.headers.get('user-agent')
    response = make_response('<h1>This document carries a cookie {}!</h1>'.format(userAgent))
    
    abort(403)
    response.status_code = 500
    response.headers = {}
    return response


if __name__ == '__main__':
    app.run(debug=True)
