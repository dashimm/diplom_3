from faker import Faker


def generate_user_data():
    faker = Faker()
    data = {
        'email': faker.email(),
        'password': faker.password(),
        'name': faker.first_name()
        }
    return data
