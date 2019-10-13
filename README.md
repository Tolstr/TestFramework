
##git 
* git init - Initialized git repository
* Create repository on github
* Create init commit (Read ME)
* git remote add origin https://github.com/Tolstr/TestFramework.git
* git push -u origin master
* Git Push from Pycharm (Ctrl+shift+k)
* Create git ignore file .gitignore to ignore extra files. Inside fie we copied files from our Boha project (you can google it). After commit and push.
* Pip install virtualenv (Installing virtual environment)
* virtualenv env (Initializing env)
* In file .gitignore add "env/" 
* OPen virtual environment: cd env, cd scripts, activate (verify that env activated), cd.., cd..
* Pip install pytest (verify if pytest working with command pytest)
* File-> Settings-> Project Interpreter and Add env scripts(C:\Python_Projects\TestFramwork\env\Scripts\python.exe)
## First test
* add python file that starts from "test_functions.py". ALways test_ first.
* Inside include pytest library (import pytest and create two tests functions with pass inside
* python -m  pytest test_functions.py (We call test_functions )
* python -m  pytest  (all tests will be executed )
* python -m  pytest test_functions.py::test_one (only test_one  from test_functions  will be executed )
* python -m  pytest -v test_functions.py::test_one (-v argument will show more details about test execution )
## Let's fail some test
* create additional test with "assert False" that is same like "assert 0". This will fail tests that we want to fail.
* For assertation user command "assert 2==2" (will pass). "assert 2==1" (will fail)
# Additional commands for pytest to see more data or run specific tests
* python -m  pytest -v test_functions.py::test_one test_functions.py::test_eight (Run specific test like test one and test eight in this case)
* pytest --collect-only (Shows how many tests we have)
* pytest -v -k "test_five" (Runs test by name)
## Structure
*see screenshot "structure_pytest.jpg"
* Create directory "tests" and put there our test_functions 
** Create in tests directory file "pytest.ini" - COME BACK LATER (avoid write -v that can be here)
## Test Marking 
* SKIP TEST: @pytest.mark.skip(reason='not working now')   Add before test case 
* FAil TEST: @pytest.mark.xfail(reason='test failing')      Add  before test case
## Creating test classes:
* Create py file class
* Proper name is: class TestAnyName(): and after going functions
* pytest -v tests/test_functions_class.py::TestClass  - run class 

## Parametrizied Tests
* "@pytest.mark.parametrize('param', [('UsernameTolia','PasswordTolia'),('Usernamevlad','Passwordvlad')])" - We run two same tests with different credentials which is our parameters. We call inside the test them by typing param instead of username.

##FICTURES
*Simple fixture is: @pytest.fixture()    Using for login (reduces attempt login every time), DB, Webdiver etc. See example in file test_fixture.py

