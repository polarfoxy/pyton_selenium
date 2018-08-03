from model.group import Group

def test_mod_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.mod_first_group(Group(name="123", header="123", footer="123"))

def test_mod_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.mod_first_group(Group(name="New group"))

def test_mod_first_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.mod_first_group(Group(header="New header"))
