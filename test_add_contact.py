# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="wtwetw", middlename="werwerwer", lastname="erwrwerewr", nickname="hhjhjjj",
                            title="hhjjkjj", company="jjjjjj", home="hhhhhh", address="hhhhh", mobile="hhhhhh",
                            work="hhhhhh", fax="hhhhh", email="hhhhh", email2="hhhhh", email3="hhhh", homepage="hhhhh",
                            byear="2000", ayear="2000", phone2="11111", address2="111111", notes="11111"))
    app.logout()

