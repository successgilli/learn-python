## Learnings
- `pytest` finds and runs test files which are identified by the files starting with `test_` or `_test`.
- Test functions are functions starting with `test_`.
- Test classes should be named `Test<Something>`
- To run all tests in the current and subdirectories, simply call `pytest`
- `pytest test_one.py` to run a single test suite
- Run test in multiple files `pytest <filename> <filename>`
- `pytest <dirname>` Starts in a particular directory (or more than one) and recursively searches for tests
- `pytest test_one.py::test_failing` to run a specific test in a suite.
- Skip tests using `@pytest.mark.skip()`
- To skip all other tests except a specific match, use `pytest -k <matching name>`. E.G `pytest -k TestEquality`.
- `pytest -k '<expression>'` can also be used with keywords such as `not`, `or`, `and` and `parenthesis`. E.G `pytest -k 'not test_with_fail'`
- By default, pytest hides print statements. To see print statements use `-s`. E.G
`pytest -s test_count_initial.py`.
- `--setup-show` allows us see the order of execution of tests especially useful with fixtures execution order.
```sh
collected 2 items                                                                                  
test_count_initial.py 
        SETUP    F cards_db
        test/cards/test_count_initial.py::test_empty (fixtures used: cards_db) .
 calling close

        TEARDOWN F cards_db
        SETUP    F cards_db
        test/cards/test_count_initial.py::test_empty2 (fixtures used: cards_db) .
 calling close

        TEARDOWN F cards_db
```
- Testing scope:

    `scope=’function’`
    Run once per test function. The setup portion is run before each test using the fixture. The teardown portion is run after each test using the fixture. This is the default scope used when no scope parameter is specified.

    `scope=’class’`
    Run once per test class, regardless of how many test methods are in the class.

    `scope=’module’`
    Run once per module, regardless of how many test functions or methods or other fixtures in the module use it.

    `scope=’package’`
    Run once per package, or test directory, regardless of how many test functions or methods or other fixtures in the package use it.

    `scope=’session’`
    Run once per session. All test methods and functions using a fixture of session scope share one setup and teardown call.
- Fixtures can depend on other fixtures but the scoping matters. A fixture can depend on another fixture of same scope or higher. E.G a function scoped fixture can depend on class scoped fixture but not the other way around.
- `conftest.py` file is an optional local plug-in file that can be used to hold fixtures. It can also contain setup or test hooks. This file is automatically read by `pytest` if exist and as a result, you do not need to import it.
- `pytest` provides a way to know what fixtures are available and to what test/test files. `fixtures` can be defined in conftest files in same directory, or in parent directories up to the root of the test directory which can create a mess. To discover them, you can ask pytest with the command `pytest --fixtures` or `pytest --fixtures test_count_initial.py` or even pass a directory name.
- `pytest --fixtures-per-test test_count_initial.py` will give you the fixtures used per test in that module. Useful for debugging.
- `pytest` ships with helpful builtin fixtures you can use. See docs for more builtins:
    - `Capsys` for capturing terminal outputs. Useful for asserting cli components
    - `tmp_dir` and similar temp file utilities for using temporary directories, files and paths.
    - `monkeypatch` for mocking and replacing objects in tests.
- `pytest --fixtures` has defined builtin fixture definitions at the top of its output.
    ```
    cache -- .../_pytest/cacheprovider.py:560
    Return a cache object that can persist state between testing sessions.

    capsys -- .../_pytest/capture.py:1007
        Enable text capturing of writes to ``sys.stdout`` and ``sys.stderr``.

    ...
    ```
- Mark tests with a custom marker using `@pytest.mark.<marker_name>`. Ypu can then run it or such tests with `pytest -m <marker_name>`
- If pytest sees `pytestmark` in a test module, it will apply the marks to all tests in that module. e.g 
```py
pytestmark = [pytest.mark.smoke, pytest.mark.coco] # Custom marker registers in pytest.ini file run with `-m smoke` or `-m coco`
```
- Declared markers can be registered in a `pytest.ini` file
- You can use combinations such as `-m​​ ​​"finish and exception"`, `-m​​ ​​"(exception or smoke) and (not finish)"`, etc
- `pytest --markers` will list available markers