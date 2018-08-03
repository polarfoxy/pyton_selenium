from model.contact import Contact

def test_mod_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    app.contact.mod_first_contact(Contact(firstname="11", middlename="werwer", lastname="11", nickname="hhjhj",
                               title="hj", company="jjjjj", home="hhh", address="hhh", mobile="hhh",
                               work="hhhh", fax="hhhhh", email="hhhhh", email2="hhhhh", email3="hhhh", homepage="hhhhh",
                               byear="2000", ayear="2000", phone2="11111", address2="111111", notes="11111"))
