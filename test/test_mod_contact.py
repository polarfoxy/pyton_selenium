from model.contact import Contact

def test_mod_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="11", middlename="werwer", lastname="11", nickname="hhjhj",
                               title="hj", company="jjjjj", home="hhh", address="hhh", mobile="hhh",
                               work="hhhh", fax="hhhhh", email="hhhhh", email2="hhhhh", email3="hhhh", homepage="hhhhh",
                               byear="2000", ayear="2000", phone2="11111", address2="111111", notes="11111")
    app.contact.mod_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert old_contacts == new_contacts
