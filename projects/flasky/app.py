from api import create_app
import atexit
app = create_app()

@app.shell_context_processor
def make_shell_context():
    return dict(app=app)

@app.cli.command()
def test():
    import unittest

    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

@app.cli.command()
def hala():
    print('Madrid!')


def goodbye():
    print("Shutting down")

atexit.register(goodbye)
