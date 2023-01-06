import os


def test_gendiff():
    exit_status = os.system('gendiff --help')
    assert exit_status == 0
