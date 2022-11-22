import random

from data.data import Person
from faker import Faker

fake = Faker('ru_RU')
Faker.seed()


def generated_person():
    yield Person(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        age=random.randint(18, 65),
        salary=random.randint(400, 1000),
        department=fake.company(),
        full_name=fake.first_name() + " " + fake.last_name() + " " + fake.middle_name(),
        email=fake.email(),
        current_address=fake.address(),
        permanent_address=fake.address()
    )
