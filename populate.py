import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE','throttlelab.settings')
django.setup()

from assignment.models import User,ActivityPeriod
from faker import Faker
from random import randint,shuffle
from datetime import timedelta
from django.utils import timezone

fake=Faker()



def populate(n):
    for i in range(n):
        
        name = fake.name()
        email = fake.email()
        tz = fake.timezone()

        if (User.objects.filter(email = email).exists()):
            pass
        else:

            start_time = fake.date_time_this_decade(before_now=True, after_now=False,  tzinfo=timezone.get_current_timezone())

            user_record = User.objects.create(real_name = name,email = email,
                                        tz = tz ,is_active = True)
            user_record.set_password("soumen123")
            user_record.save()

            act1 = ActivityPeriod(user = user_record,start_time = start_time,end_time = start_time + timedelta(hours=5))
            act1.save()

            act2 = ActivityPeriod(user = user_record,start_time = start_time,end_time = start_time + timedelta(hours=3))
            act2.save()

            act3 = ActivityPeriod(user = user_record,start_time = start_time,end_time = start_time + timedelta(hours=1))
            act3.save()



populate(10)
