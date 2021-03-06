from model.contact import Contact


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        self.get_contact()
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.get_contact()
        self.contact_cache = None

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.get_contact()
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def mod_contact_by_index(self, contact, index):
        wd = self.app.wd
        self.get_contact()
        wd.find_elements_by_css_selector("[src='icons/pencil.png']")[index].click()
        self.fill_contact_form(contact)
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def mod_first_contact(self):
        self.mod_contact_by_index(0)

    def get_contact(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("addressbook/") and len(wd.find_elements_by_xpath("//input[@value='Send e-Mail']")) > 0):
            wd.get("http://localhost/addressbook/")

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("home", contact.home)
        self.change_field_value("address", contact.address)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email2", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        self.change_field_value("byear", contact.byear)
        self.change_field_value("ayear", contact.ayear)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[16]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[16]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[10]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[10]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[11]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[11]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[9]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[9]").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def count(self):
        wd = self.app.wd
        self.get_contact()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.get_contact()
            self.contact_cache = []
            for element in wd.find_elements_by_css_selector("[name = entry]"):
                id = element.find_element_by_name("selected[]").get_attribute("value")
                text = element.find_element_by_xpath("./td[2]").text
                texts = element.find_element_by_xpath("./td[3]").text
                self.contact_cache.append(Contact(id=id, lastname=text, firstname=texts))
        return list(self.contact_cache)

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()




