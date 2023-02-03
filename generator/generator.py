import random

from faker import Faker

from data.data import Person

fake = Faker('ru_RU')
Faker.seed()


def generated_person():
    """ Генерирует данные человека (персоны) используя библиотеку Faker

    Вызывает класс Person() и кладет в него сгенерированные данные

    """
    #month_abreviated = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    month_wide = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
            'November', 'December']


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
        date_of_birth=str(random.randint(1, 31)) + " " + month_wide[random.randint(0, 11)] + " " + str(
            random.randint(1900, 2100))
    )


def generated_file():
    """ Генерирует файл с рандомным именем используя random.randint()"""

    path = f"/media/user/10B05902B058EFA8/Py_proj/py/myapp/demoqa.com/file{random.randint(0, 999)}.txt"

    file = open(path, 'w+')
    file.write(f'Hello by this number {random.randint(0, 999)}')
    file.close()
    return file.name, path


def generate_subject():
    subject = {
        1: 'Hindi',
        2: 'English',
        3: 'Maths',
        4: 'Physics',
        5: 'Chemistry',
        6: 'Biology',
        7: 'Computer Science',
        8: 'Commerce',
        9: 'Accounting',
        10: 'Economics',
        12: 'Social Studies',
        13: 'History',
        14: 'Civics'
    }
    return subject.get(random.randint(1, 14))


def generate_state_and_city():
    state_list = ['NCR', 'Uttar Pradesh', 'Haryana', 'Rajasthan']
    state_and_city = {
        'NCR': {
            1: 'Delhi',
            2: 'Gurgaon',
            3: 'Noida'
        },
        'Uttar Pradesh': {
            1: 'Agra',
            2: 'Lucknow',
            3: 'Merrut'
        },

        'Haryana': {
            1: 'Karnal',
            2: 'Panipat'
        },
        'Rajasthan':
        {
            1: 'Jaipur',
            2: 'Jaiselmer',
        }
    }

    gen_state_name = state_list[random.randint(0, 3)]
    gen_city = state_and_city.get(gen_state_name)
    city = gen_city.get(random.randint(1, len(list(gen_city))))
    return gen_state_name, city
