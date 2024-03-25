import random
from faker import Faker
from django.utils import timezone
from .models import Student, Sclass

fake = Faker()



def generate_fake_students():
    sclass_instances = Sclass.objects.all()
    for _ in range(2000):
        name = fake.name()
        dob = fake.date_of_birth(minimum_age=18, maximum_age=25)
        section = random.choice(sclass_instances)
        roll_number = fake.random_int(min=1, max=1000)
        gender = random.choice(['male', 'female'])
        blood_group = random.choice(['A+', 'A-', 'B+', 'B-', 'O+', 'O-', 'AB+', 'AB-'])
        parents_phone_number = fake.phone_number()
        address = fake.address()

        Student.objects.create(
            name=name,
            dob=dob,
            section=section,
            roll_number=roll_number,
            gender=gender,
            blood_group=blood_group,
            parents_phone_number=parents_phone_number,
            address=address
        )

# Call the function to generate fake students
#generate_fake_students()
