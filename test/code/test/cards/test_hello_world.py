import pathlib
import pytest
from hello_world import hello
import os
import time

def test_hello_writes_to_file():
    assert hello() == None

    with open('./hello.txt', 'r') as file:
        assert file.readline() == "Hello World!\n"
    
    # Clean up
    os.remove('./hello.txt')


def test_hello_writes_to_file_in_tmp_dir(tmp_path: pathlib.Path, monkeypatch: pytest.MonkeyPatch):
    monkeypatch.chdir(tmp_path)

    assert hello() == None

    with open(str(tmp_path) + '/hello.txt', 'r') as file:
        assert file.readline() == "Hello World!\n"
