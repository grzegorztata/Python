class Person:
    def __init__(self, first_name, last_name, company, occupation, email):
        self.first_name = first_name
        self.last_name = last_name
        self.company = company
        self.occupation = occupation
        self.email = email

wduda = Person(first_name="Wisława", last_name="Duda", company="Infinite Wealth Planners", occupation="Elektryk", email="WislawaDuda@rhyta.com")
jkucharski = Person(first_name="Jacek", last_name="Kucharski", company="Big Star Markets", occupation="Operator kamery", email="JacekKucharski@jourrapide.com")
wnowak = Person(first_name="Walenty", last_name="Nowak", company="Total Quality", occupation="Architekt", email="WalentyNowak@jourrapide.com")
dczarnecka = Person(first_name="Dorota", last_name="Czarnecka", company="Creative Wealth", occupation="Farmaceutka", email="DorotaCzarnecki@jourrapide.com")
mpiotrowski = Person(first_name="Maksymilian", last_name="Piotrowski", company="Pro Star", occupation="Serwisant", email="MaksymilianPiotrowski@jourrapide.com")

people = []

people.append(wduda)
people.append(jkucharski)
people.append(wnowak)
people.append(dczarnecka)
people.append(mpiotrowski)

for person in people:
    print(str(person.first_name), str(person.last_name), ", Email: " + str(person.email))