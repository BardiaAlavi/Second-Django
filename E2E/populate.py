import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'E2E.settings')


import django

django.setup()

from django.contrib.auth.models import User
from faker import Faker

fakegen=Faker()

def populate(N=1000):

    for i in range(N):

        fake_email=fakegen.unique.email()
        fake_user=fakegen.unique.user_name()
        user=User.objects.get_or_create(username=fake_user, email=fake_email)[0]

if __name__=='__main__':

    print('start to work')
    populate()
    print('DONE!')
