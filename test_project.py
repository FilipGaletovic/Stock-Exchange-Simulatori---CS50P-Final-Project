import project
import hashlib
import main_menu
import load_save

def test_Account_init():
    password = "Filip!23"
    new_acc = project.Account("Filip", password)
    pass_to_hash =  hashlib.sha256(password.encode()).hexdigest()
    assert new_acc.username == "Filip"
    assert new_acc.password == pass_to_hash

def test_to_dict():
    new_acc = project.Account("Filip", "Filip!23")
    assert new_acc.to_dict() == {
            "username": new_acc.username,
            "password_hash": new_acc._password_hash,
            "balance": new_acc.balance,
            "invested": {}
        }

def test_login():
    assert project.login("sth", "sth") == False
    assert project.login("123", "12343") == False
    assert project.login("FilipG", "Filip!23") == True

def test_register():
    assert project.register("Steven", "Steve!23") == False

def test_fetch_user():
    user_data = load_save.load_users("accounts.json")
    name1 = "FilipG"
    name2 = "Steven"
    assert main_menu.fetch_user(name1, user_data) == 1
    assert main_menu.fetch_user(name2, user_data) == 0


