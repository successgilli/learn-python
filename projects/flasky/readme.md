## Flask webserver
- Flask comes with a development server that can be started with `flask run`
- This command looks for the flask app instance contained in the script file set by the env variable `FLASK_APP`.
- Set this variable in the virtual env by running `export FLASK_APP=app.py` where `app.py` is simply the file that holds your flask instance. It can be any name you choose.
- Another alternative to having to manually run `flask run`
is to simply start the development server using the flask app instance with `app.run` like so:
```py
app = Flask(__name__)
...
if __name__ == '__main__':
    app.run()
```
- Run the app.py script `python3 app.py`
- The webserver can also be started in debug mode.
- To do this, set env variable `FLASK_DEBUG=1` when using `flask run`
- If using `app.run` in script, simply pass `app.run(debug=True)`
- Two components of the server are then turned on when debug mode is activated, the reloader that watches source files for changes and reloads/restarts your webserver and a debugger that opens an interactive stack trace in the browser when errors occur.
- Flask applications maintain two main contexts;
    - Application context: `g` and `current_app`
    - Request context: `session` and `request`

    1) `g` is an object that can be used to hold temporary values that can be shared within the scope of a request. E.G values collected by one middleware can be stored in `g` and used in another middleware or request hook.
    2) `current_app` is the context object for the current application
    3) `session` is a dictionary for holding session data that should be remembered across requests
    4) `request` is the encapsulation of the http request sent by the client.
- There are request hooks you can use to run handler before and after request.

## Templates
Flask uses the Jinja templating engine for rendering static assets.

## Flask shell
- Flask applications can be accessed via the terminal with `flask shell` which will open an environment that allows you to interact with the flask application. You can import like you would in a flask app variables, db objects and call/interact with them like you would programmatically.
- In the shell, you will have to import object each time you start the shell. Flask shell offers decorators that allow you to specify objects you want exposed out of the box each time you open the shell. With this, those objects are readily available for access and usage without having to import them each time in the shell.

```py
@app.shell_context_processor
def shell_context():
    return dict(db=db, User=User, Role=Role)
```

