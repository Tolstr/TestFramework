import pytest



@pytest.fixture() #reduces code and repetition like do not need login every time or webdiver run once
def some_fixturezzz():
    print("\n SETUP STARTED:") #different kind of functionality
    yield False
    print("\n TEARDOWN STARTED")


def test_fixture_one(some_fixturezzz):
    assert False == some_fixturezzz

def test_fixture_two(some_fixturezzz):
    assert True == some_fixturezzz



