from faker import Faker
fake = Faker(locale='en_CA')
AOS_Url = 'https://advantageonlineshopping.com/#/'
AOS_title = '\xa0Advantage Shopping'
AOS_register = 'https://advantageonlineshopping.com/#/register'
new_username = f'{fake.user_name()[:8]}{fake.pyint(111,999)}'
new_password = fake.password() [:12]
email = fake.email()
first_name = fake.first_name()
last_name = fake.last_name()
full_name = f'{first_name} {last_name}'
phone_number1 = fake.phone_number()
city = fake.city()
province = fake.province_abbr()
postcode = fake.postcode_in_province()
address = fake.street_address()
description = fake.sentence(nb_words=10)
order_number = ""
