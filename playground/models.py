from django.db import models
import random
import string
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

class TimeStampedModel(models.Model):
    created_date = models.DateTimeField(default=timezone.now, editable=False)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Sclass(TimeStampedModel):
    name = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.name

class Fee_Category(TimeStampedModel):
    name = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.name



class Student(TimeStampedModel):
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
    )

    name = models.CharField(max_length=100, blank=False, default='')
    dob = models.DateField(null=True, blank=False)
    section = models.ForeignKey(Sclass, on_delete=models.CASCADE)
    roll_number = models.PositiveIntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    blood_group = models.CharField(blank=True, max_length=10)
    parents_phone_number = models.CharField(max_length=15)  # Assuming phone number can include characters like '+'
    admission_id = models.CharField(max_length=20, unique=True, editable=False)
    address = models.TextField(blank=True) 

    def save(self, *args, **kwargs):
        if not self.admission_id:
            # Auto-generate admission ID
            self.admission_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
    @property
    def payment_times(self):
        return self.fee_set.count()

    @property
    def total_due(self):
        total_due = sum(fee.due_payment for fee in self.fee_set.all())
        if total_due > 0:
            color = 'red'
        else:
            color = 'green'
        return {'amount': total_due, 'color': color}
    
    @property
    def due_explain(self):
        fees_info = {}
        for fee in self.fee_set.all():
            category = fee.fee_category
            if category not in fees_info:
                fees_info[category] = 0
            fees_info[category] += fee.due_payment

        breakdown = []
        for category, due in fees_info.items():
            color = 'red' if due > 0 else 'green'
            status = 'Due' if due > 0 else 'Paid'
            breakdown.append(f'{category}(<span style="color:{color}">{due}</span>) (<span style="color:{color}">{status}</span>)')

        return ' | '.join(breakdown)

class FeeSet(models.Model):
    fee_category = models.ForeignKey(Fee_Category, on_delete=models.CASCADE, verbose_name=_('Fee Category'))
    class_category = models.ForeignKey(Sclass, on_delete=models.CASCADE, verbose_name=_('Class Category'))
    fee_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('Fee Amount'))
    year = models.IntegerField(default=2024) 
    created_date = models.DateTimeField(auto_now_add=True, verbose_name=_('Created Date'))
    modified_date = models.DateTimeField(auto_now=True, verbose_name=_('Modified Date'))

    class Meta:
        verbose_name = _('Fee Set')
        verbose_name_plural = _('Fee Sets')

    def __str__(self):
        return f"{self.fee_category} - {self.class_category} ({self.year})"
     
class Fee(TimeStampedModel):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name=_('Student'))
    fee_category = models.ForeignKey(FeeSet, on_delete=models.CASCADE, verbose_name='Fee Category')
    fees_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('Fees Amount'))
    partial_payment = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('Partial Payment'))
    voucher_id = models.CharField(max_length=100, verbose_name=_('Voucher ID'))

    class Meta:
        verbose_name = _('Fee')
        verbose_name_plural = _('Fees')

    def __init__(self, *args, **kwargs):
        super(Fee, self).__init__(*args, **kwargs)
        if self.student_id:
            self._update_fee_category_choices()
        # if self.fee_category_id:
        #     self._set_fees_amount()

    # def _set_fees_amount(self):
    #     if self.fee_category_id:
    #         fee_set_instance = FeeSet.objects.get(pk=self.fee_category_id)
    #         self.fees_amount = fee_set_instance.fee_amount

    def _update_fee_category_choices(self):
        if self.student_id:
            student_section = FeeSet.objects.filter(class_category=self.student.section)
            self._meta.get_field('fee_category').queryset = student_section

    # def save(self, *args, **kwargs):
    #     if self.student_id:
    #         self._update_fee_category_choices()
    #     if self.fee_category_id:
    #         self._set_fees_amount()
    #     super(Fee, self).save(*args, **kwargs)

    @property
    def due_payment(self):
        return max(0, self.fees_amount - self.partial_payment)
    # @property
    # def get_fees_amount(self):
    #     # Retrieve the fee amount from the associated fee_category
    #     if self.fee_category:
    #         return self.fee_category.fee_amount
    #     return None
    def __str__(self):
        return f"{self.student} - {self.fee_category}"
    
    @property
    def status(self):
        # Calculate the remaining amount due after partial payment
        remaining_due = self.fees_amount - self.partial_payment
        if remaining_due > 0:
            # If there is still an amount due, return 'Due' with the remaining due amount
            return f'Due (৳{remaining_due})'
        else:
            # If no amount due, return 'Paid'
            return 'Paid'

    # Optional: Define a property for the color based on status
    @property
    def status_color(self):
        if self.status == 'Paid':
            return 'green'
        else:
            return 'red'




