from dataclasses import dataclass


@dataclass
class Person:
    """
    Класс для представления человека

    Атрибутты:
    _________
        first_name:  = None - Имя человека
        last_name: str = None - Фамилия человека
        email: str = None - Email
        age: int = None - Возраст человека
        salary: int = None - Зарплата человека
        department: str = None - Где работает человек (компания, отдел)
        full_name: str = None - ФИО человека
        current_address: str = None - Текущий адресс человека
        permanent_address: str = None - Постоянный адресс человека
        phone_number: str = None
        date_of_birth: str = None

    """

    first_name: str = None
    last_name: str = None
    email: str = None
    age: int = None
    salary: int = None
    department: str = None
    full_name: str = None
    current_address: str = None
    permanent_address: str = None
    phone_number: str = None
    date_of_birth: str = None
