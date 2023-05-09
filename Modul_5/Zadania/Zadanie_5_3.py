import random
from faker import Faker

fake = Faker()

class Person:
    def __init__(self, first_name, last_name, company, occupation, email):
        self.first_name = first_name
        self.last_name = last_name
        self.company = company
        self.occupation = occupation
        self.email = email
        
    @property
    def name_length(self):
        return f"{len(self.first_name)} {len(self.last_name)} {self.first_name} {self.last_name}"
    
class BaseContact(Person):
    def __init__(self, first_name, last_name, phone, email):
        super().__init__(first_name, last_name, None, None, email)  # usuwamy company i occupation
        self.phone = phone
        
    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.phone}  {self.email}'
        
    def contact(self):
        print(f'Wybieram numer {self.phone} i dzwonię do {self.first_name} {self.last_name}') 
        
class BusinessContact(BaseContact):
    def __init__(self, first_name, last_name, phone, email, occupation, company, work_phone):
        super().__init__(first_name, last_name, phone, email)
        self.occupation = occupation
        self.company = company
        self.work_phone = work_phone
        
    def __str__(self):
        return f'{self.first_name}  {self.last_name}  {self.phone}  {self.email}  {self.occupation}  {self.company}  {self.work_phone}'
        
    def contact(self):
        print(f'Wybieram numer {self.work_phone} i dzwonię do {self.first_name} {self.last_name}') 
        
def create_contact(num_contacts, contact_type):
    contacts = []
    for i in range(num_contacts):
        first_name = fake.first_name()
        last_name = fake.last_name()
        phone = fake.phone_number()
        email = fake.email()
        if contact_type == "BaseContact":
            contact = BaseContact(first_name, last_name, phone, email)
        elif contact_type == "BusinessContact":
            occupation = fake.job()
            company = fake.company()
            work_phone = fake.phone_number()
            contact = BusinessContact(first_name, last_name, phone, email, occupation, company, work_phone)
        else:
            raise ValueError("Invalid contact type")
        contacts.append(contact)
    return contacts

base_contacts = create_contact(5, "BaseContact")
print("-----Kontakty podstawowe-----")
for contact in base_contacts:
    print(contact)
    print(contact.name_length)
    contact.contact()
    print("-----")
    
business_contacts = create_contact(5, "BusinessContact")
print("\n-----Kontakty biznesowe-----")
for contact in business_contacts:
    print(contact)
    print(contact.name_length)
    contact.contact()
    print("-----")
