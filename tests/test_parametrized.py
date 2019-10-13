import pytest






@pytest.mark.parametrize('param', ['Vova','tolia','jenia'])
def test_param(param):
    assert  0==param[0]

@pytest.mark.parametrize('param', [('UsernameTolia','PasswordTolia'),('Usernamevlad','Passwordvlad')])
def test_param(param):
    assert 0==param[0] and 1==param[1]