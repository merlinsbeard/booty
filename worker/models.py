from django.db import models
from datetime import date

def calculate_age(born):
    today = date.today()
    age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
    return age

class Agency(models.Model):
    agency = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.agency

    def total_workers(self):
        return self.worker_set.count()

class Mall(models.Model):
    mall = models.CharField(max_length=200, unique=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.mall



class Worker(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    OTHER = 'O'
    SEX_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other')
        )
    MARITAL_STATUS_CHOICES = (
        ('Single', 'Single'),
        ('Married', 'Married')
        )

    firstname               = models.CharField(max_length=150)
    middlename              = models.CharField(max_length=150)
    lastname               = models.CharField(max_length=150)
    date_of_birth           = models.DateField()
    present_address         = models.TextField()
    sex                     = models.CharField(choices=SEX_CHOICES, max_length=1)
    height                  = models.CharField(max_length=10)
    weight                  = models.CharField(max_length=10)
    security_license_number = models.CharField(max_length=200)
    date_issued             = models.DateField()
    date_of_expiration      = models.DateField()
    marital_status          = models.CharField(max_length=7, choices=MARITAL_STATUS_CHOICES)
    agency                  = models.ForeignKey(Agency)
    date_added              = models.DateTimeField(auto_now_add=True)
    date_updated            = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.firstname + ' ' + self.middlename + ' ' + self.lastname

    def age(self):
        age_now = calculate_age(self.date_of_birth)
        return age_now

    def full_name(self):
        a = self.firstname + ' ' + self.middlename + ' ' + self.lastname
        return str(a)

    def get_mall(self):
        mall = self.mallworker.mall.__str__()
        return mall


class MallWorker(models.Model):
    mall = models.ForeignKey(Mall)
    worker = models.OneToOneField(Worker)
    date_started = models.DateField()

    def __str__(self):
        # return str(self.pk)
        return self.worker.full_name() + self.mall.mall

class Spouse(models.Model):
    worker = models.ForeignKey(Worker)
    spouse_name             = models.CharField(max_length=200)
    spouse_bday             = models.DateField()
    spouse_occupation       = models.CharField(max_length=200)
    spouse_address          = models.TextField()

    def __str__(self):
        return self.worker.full_name() + ' ' + self.spouse_name

class Children(models.Model):
    worker = models.ForeignKey(Worker)
    name = models.CharField(max_length=200)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.worker.full_name() + ' ' + self.name

class School(models.Model):
    CHOICES = (
        ('Elementary','Elementary'),
        ('High School','High School'),
        ('College',' College'),
        ('Vocational','Vocational')
            )
    worker = models.ForeignKey(Worker)
    category = models.CharField(max_length=12,choices=CHOICES)
    school_name = models.CharField(max_length=200)
    year_graduated = models.DateField()

    def __str__(self):
        return self.worker.full_name() + '' + self.category

class Seminar(models.Model):
    worker = models.ForeignKey(Worker)
    name = models.CharField(max_length=200)
    conducted_by = models.CharField(max_length=200)
    date_started = models.DateField()
    date_finished = models.DateField()

    def __str__(self):
        return self.worker.full_name() + ' ' + self.name

class Employment(models.Model):
    worker = models.ForeignKey(Worker)
    place = models.CharField(max_length=200)
    position = models.CharField(max_length=50)
    date_started = models.DateField()
    date_finished = models.DateField()

    def __str__(self):
        return self.worker.full_name() + ' ' + self.place
