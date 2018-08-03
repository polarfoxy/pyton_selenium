# -*- coding: utf-8 -*-
from model.contact import Contact



def test_add_contact(app):
    app.contact.create(Contact(firstname="wtwetw", middlename="werwerwer", lastname="erwrwerewr", nickname="hhjhjjj",
                               title="hhjjkjj", company="jjjjjj", home="hhhhhh", address="hhhhh", mobile="hhhhhh",
                               work="hhhhhh", fax="hhhhh", email="hhhhh", email2="hhhhh", email3="hhhh", homepage="hhhhh",
                               byear="2000", ayear="2000", phone2="11111", address2="111111", notes="11111"))

