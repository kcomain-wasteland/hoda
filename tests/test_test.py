import os.path
import sys
import time

import requests
import pytest


def test_test():
    print("test 1")
    return True


def test_test2():
    print("test 2")
    return True


def test_test3():
    print("test 3")
    return True


def test_test4():
    print("test 4")
    return False


def test_test5():
    print("test 5")
    return True


def test_test6():
    print("test 2")
    return True


def test_test7():
    print("test 3")
    return True


def test_test8():
    print("test 1")
    return True


def test_test9():
    print("test 2")
    return True


def test_test10():
    print("test 3")
    return True


def test_test11(testserver):
    req = requests.get(os.path.join(testserver, "test/sleep"))
    assert req.status_code == 204, f"Expected return code 204, got {req.status_code}"


def test_test12(testserver):
    print("test 2")
    time.sleep(5)
    return True


@pytest.mark.xfail
def test_test13():
    print("test 3")
    raise OSError("Balls")


def test_test14():
    print("test 1")
    pytest.skip("test")
    return True


@pytest.mark.skipif(sys.version_info > (3, 7), reason="requires python3.7 or lower")
def test_test15():
    print("test 2")
    return True


@pytest.mark.xfail
def test_test16():
    print("test 3")
    raise SystemError


@pytest.mark.xfail
def test_rec():
    funcs = locals()
    print("call")
    for name, obj in funcs:
        if callable(obj):
            print(f"calling {name}")
            obj()
    return True
