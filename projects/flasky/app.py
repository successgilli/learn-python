from flask import Flask, make_response, render_template


app = Flask(__name__)

def index() -> str:
    return render_template('index.html')

app.add_url_rule('/', 'index', index)

@app.get('/user/<name>')
def username(name: str) -> tuple[str, int]:
    return render_template('user.html', name=name)

@app.errorhandler(404)
def app_error_404(e):
    return make_response(render_template('404.html', error=e), 404)

if __name__ == '__main__':
    app.run(debug=True)
