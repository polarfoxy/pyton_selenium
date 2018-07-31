from model.group import Group

def test_mod_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.mod_first_group(Group(name="123", header="123", footer="123"))
    app.session.logout()