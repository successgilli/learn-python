import pathlib

import cards
import pytest

def test_version_v2(capsys: pytest.CaptureFixture):
    cards.cli.version()

    val = capsys.readouterr().out.rstrip()

    assert val == cards.__version__

def test_disabed_outpur(capsys: pytest.CaptureFixture):
    with capsys.disabled():
        print('labla')

def test_monkeypath(monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture):
    monkeypatch.setattr(cards, '__version__', '234')

    cards.cli.version()

    output = capsys.readouterr().out.rstrip()
    assert output == '234'

def test_env(capsys: pytest.CaptureFixture, monkeypatch: pytest.MonkeyPatch, tmp_path: pathlib.Path):
    monkeypatch.setenv('CARDS_DB_DIR', str(tmp_path))
    cards.cli.config()

    value = capsys.readouterr().out.rstrip()

    assert value == str(tmp_path)
