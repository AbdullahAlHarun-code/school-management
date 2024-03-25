import random
from faker import Faker
from .models import Fee, Fee_Category, Student

def generate_fake_fees():
    fake = Faker()

    # Fetch existing data
    students = list(Student.objects.all())
    fee_categories = list(Fee_Category.objects.all())

    # Generate fake fee data
    for _ in range(3000):  # Generate 100 fake fee records
        student = random.choice(students)
        fee_category = random.choice(fee_categories)
        fees_amount = random.randint(100, 1000)
        partial_payment = random.randint(0, fees_amount)
        voucher_id = fake.uuid4()

        Fee.objects.create(
            student=student,
            fees_category=fee_category,
            fees_amount=fees_amount,
            partial_payment=partial_payment,
            voucher_id=voucher_id
        )

    print('Fake fee data generated successfully.')

# Call the function to generate fake fees
#generate_fake_fees()
