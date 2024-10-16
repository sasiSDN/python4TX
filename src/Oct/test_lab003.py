import pytest
import allure

@pytest.mark.smoke
def test_verify_sum():
    assert 2+2==4

@pytest.mark.  smoke
def test_verify_sub():
    assert 2-2==0

@pytest.mark.smoke
def test_verify_sub2():
    assert 22-22==0
@pytest.mark.reg
def test_verify_equal():
    assert 1-2!=0

@pytest.mark.skip(reason="not completed,skip it")
def test_verify_zero():
    assert 0-0!=0

