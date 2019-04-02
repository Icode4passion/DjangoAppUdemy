import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','proj2.settings')


import django
django.setup()

from app2.models import User
from faker import Faker

fakgen = Faker()

def populate(N=5):
	for entry in range(N):
		fake_name = fakgen.name().split()
		fake_firstname = fake_name[0]
		fake_lastname = fake_name[1]
		fake_email = fakgen.email()

		userob = User.objects.get_or_create(first_name = fake_firstname,
											last_name = fake_lastname,
											email = fake_email)[0]


if __name__ == '__main__':
		print("Populating Names !")
		populate(20)
		print("Populating Names Complete!") 
		


