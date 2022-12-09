import random

from faker import Faker

from data.data import Person

fake = Faker('ru_RU')
Faker.seed()


def generated_person():
    """ Генерирует данные человека (персоны) используя библиотеку Faker

    Вызывает класс Person() и кладет в него сгенерированные данные

    """
    month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    yield Person(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        email=fake.email(),
        age=random.randint(18, 65),
        salary=random.randint(400, 1000),
        department=fake.company(),
        full_name=fake.first_name() + " " + fake.last_name() + " " + fake.middle_name(),
        current_address=fake.address(),
        permanent_address=fake.address(),
        phone_number=str(random.randint(1111111111, 9999999999)),
        date_of_birth=str(random.randint(1, 31)) + " " + month[random.randint(0, 11)] + " " + str(random.randint(1900, 2100))
    )


def generated_file():
    """ Генерирует файл с рандомным именем используя random.randint()"""

    path = f"/home/user/py/myapp/demoqa.com/file{random.randint(0, 999)}.txt"

    file = open(path, 'w+')
    file.write(f'Hello by this number {random.randint(0, 999)}')
    file.close()
    return file.name, path
