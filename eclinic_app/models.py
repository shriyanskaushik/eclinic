from asyncio.windows_events import NULL
from django.db import models

# Create your models here.
class Locality(models.Model):
    pin_code = models.CharField(max_length = 8)
    latitude = models.FloatField(null = True, default = NULL)
    longitude = models.FloatField(null = True, default = NULL)
    landmark = models.CharField(max_length = 25)

class Assistant(models.Model):
    username = models.CharField(max_length = 50, unique = True)
    name = models.CharField(max_length= 50)
    phone_number = models.CharField(max_length = 10)
    dob = models.DateField(null = True, default = NULL)
    locality_id = models.IntegerField()

class Patient(models.Model):
    MALE = 1
    FEMALE = 2

    gender_choices = (
        (MALE, 'male'),
        (FEMALE, 'female')
    )
    username = models.CharField(max_length = 50)
    name = models.CharField(max_length = 50)
    phone_number = models.CharField(max_length = 10)
    dob = models.DateField(null = True, defaul = NULL)
    locality_id = models.IntegerField()
    gender = models.PositiveIntegerField(choices = gender_choices)

class Hospital(models.Model):
    name = models.CharField(max_length = 50)
    locality_id = models.PositiveIntegerField(null = True)
    phone_number = models.CharField(max_length=10)
    email_id = models.EmailField(null=True, default=NULL)

class Doctor(models.Model):
    username = models.CharField(max_length = 50)
    name = models.CharField(max_length = 50)
    phone_number = models.CharField(max_length = 10)
    dob = models.DateField(null = True, defaul = NULL)
    email_id = models.EmailField(null=True, default=NULL)
    speciality = models.CharField(max_length=25)
    hospital_id = models.PositiveIntegerField(null=True, default=NULL)

class Pharmacy(models.Model):
    username = models.CharField(max_length = 50)
    name = models.CharField(max_length = 50)
    phone_number = models.CharField(max_length = 10)
    dob = models.DateField(null = True, defaul = NULL)
    email_id = models.EmailField(null=True, default=NULL)
    manager = models.CharField(null=True, default=NULL)
    locality_id = models.PositiveIntegerField(null=True, default=NULL)

class DiagnosticLab(models.Model):
    username = models.CharField(max_length = 50)
    name = models.CharField(max_length = 50)
    phone_number = models.CharField(max_length = 10)
    dob = models.DateField(null = True, defaul = NULL)
    email_id = models.EmailField(null=True, default=NULL)
    manager = models.CharField(null=True, default=NULL)
    locality_id = models.PositiveIntegerField(null=True, default=NULL)

class PharmacyExtended(models.Model):
    pharmacy_id = models.PositiveIntegerField()
    rating = models.FloatField()
    opening = models.TimeField()
    closing = models.TimeField()

class DiagExtended(models.Model):
    diag_id = models.PositiveIntegerField()
    rating = models.FloatField()
    opening = models.TimeField()
    closing = models.TimeField()

class DoctorExtended(models.Model):
    doctor_id = models.PositiveIntegerField()
    rating = models.FloatField()
    languages_known = models.CharField()
    year_of_experience = models.FloatField()

class Test(models.Model):
    diag_id = models.PositiveIntegerField()
    test_name = models.CharField()
    price = models.FloatField()

class PatientRecords(models.Model):

    DOCTOR_APPOINTMENT = 1
    MEDICINES = 2
    DIAGONOSTIC_TEST = 3

    purpose_choice = (
        (DOCTOR_APPOINTMENT, 'doctor'),
        (MEDICINES, 'medicines'),
        (DIAGONOSTIC_TEST, 'diagonostic_test')
    )
    patient_id = models.PositiveIntegerField()
    date_time = models.DateTimeField()
    purpose = models.PositiveSmallIntegerField(choices=purpose_choice)

class Payment(models.Model):
    CASH = 1
    DEBIT_CARD = 2
    CREDIT_CARD = 3
    UPI = 4

    payment_choice = (
        (CASH, 'cash'),
        (DEBIT_CARD, 'debit_card'),
        (CREDIT_CARD, 'credit_card')
        (UPI, 'upi')
    )
    amount = models.FloatField()
    discount = models.FloatField()
    net_amount = models.FloatField()
    payment_type = models.PositiveSmallIntegerField(choices=payment_choice)

class FAQ(models.Model):
    DOCTOR = 1
    PHARMACY = 2
    DIAGONOSTIC = 3

    user_type_choice = (
        (DOCTOR, 'doctor'),
        (PHARMACY, 'pharmacy'),
        (DIAGONOSTIC, 'diagonostic')
    )
    question = models.CharField()
    answer = models.CharField()
    user_type = models.PositiveSmallIntegerField(choices = user_type_choice)

class DoctorFeedback(models.Model):
    doctor_id = models.PositiveIntegerField()
    patient_id = models.PositiveBigIntegerField()
    rating = models.FloatField()
    review = models.CharField(max_length=500)

class PharmacyFeedback(models.Model):
    pharma_id = models.PositiveIntegerField()
    patient_id = models.PositiveBigIntegerField()
    rating = models.FloatField()
    review = models.CharField(max_length=500)

class DiagonosticFeedback(models.Model):
    diag_id = models.PositiveIntegerField()
    patient_id = models.PositiveBigIntegerField()
    rating = models.FloatField()
    review = models.CharField(max_length=500)