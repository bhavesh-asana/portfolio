from django.db import models

# Create your models here.
from django.db import models
from django.core.validators import RegexValidator

phoneNumber_validator = RegexValidator(
    regex=r'^\+?1?\d{9,13}$',
    message="Phone number must be entered in the format: '+18123603100")


class Address(models.Model):
    street_1 = models.CharField(max_length=150, blank=True, null=True)
    street_2 = models.CharField(max_length=150, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    postalCode = models.CharField(max_length=7, blank=True, null=True)

    def __str__(self):
        return f'{self.street_1}, {self.street_2}, {self.city}, {self.state}, {self.country}, {self.postalCode}'


class Company(models.Model):
    companyName = models.CharField(max_length=255)
    phoneNumber = models.CharField(validators=[phoneNumber_validator], max_length=13, blank=True)
    location = models.OneToOneField(Address, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.companyName)


class Employee(models.Model):
    objects = None
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    phoneNumber = models.CharField(validators=[phoneNumber_validator], max_length=13, blank=False)
    primaryAddress = models.ForeignKey(Address, on_delete=models.CASCADE, blank=True, null=True,
                                       related_name='primaryAddress')
    mailingAddress = models.ForeignKey(Address, on_delete=models.CASCADE, null=True, blank=True,
                                       related_name='mailing_address')
    officeAddress = models.ForeignKey(Address, on_delete=models.CASCADE, null=True, blank=True,
                                      related_name='office_address')
    photo = models.ImageField(null=True, blank=True)
    dateOfBirth = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    socialSecurity = models.CharField(max_length=5, blank=True, null=True)
    company = models.ForeignKey(Company, related_name='company', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.firstName} {self.lastName}'


class Education(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='education', null=True, blank=True)
    schoolName = models.CharField(max_length=255)
    major = models.CharField(max_length=255)
    startDate = models.DateField(auto_now=False, auto_now_add=False)
    endDate = models.DateField(auto_now=False, auto_now_add=False)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.schoolName}'


class Passport(models.Model):
    employee = models.ForeignKey(Employee, related_name='passport', on_delete=models.CASCADE, null=True, blank=True)
    passportNumber = models.CharField(max_length=12)
    placeOfIssue = models.CharField(max_length=255)
    dateOfIssue = models.DateField(auto_now=False, auto_now_add=False)
    dateOfExpiry = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return f'{self.passportNumber}'


class Visa(models.Model):
    employee = models.ForeignKey(Employee, related_name='visa', on_delete=models.CASCADE, null=True, blank=True)
    passport = models.ForeignKey(Passport, on_delete=models.CASCADE, null=True, blank=True)
    type = models.CharField(max_length=10)
    dateOfIssue = models.DateField(auto_now=False, auto_now_add=False)
    dateOfExpiry = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return f'{self.type}'


class EmploymentAuthorization(models.Model):
    objects = None
    employee = models.ForeignKey(Employee, related_name='employmentAuthorization', on_delete=models.CASCADE, null=True,
                                 blank=True)
    type = models.CharField(max_length=255)
    dateOfValidity = models.DateField(auto_now=False, auto_now_add=False)
    dateOfExpiry = models.DateField(auto_now=False, auto_now_add=False)
    uscisNumber = models.CharField(max_length=100, unique=True)
    cardNumber = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f'{self.employee} {self.type}'


class Manager(models.Model):
    employee = models.OneToOneField(Employee, related_name='manager', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.employee.firstName} {self.employee.lastName}'


class Recruiter(models.Model):
    employee = models.OneToOneField(Employee, related_name='recruiter', on_delete=models.CASCADE, null=True, blank=True)
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.employee.firstName} {self.employee.lastName}'


class Socials(models.Model):
    employee = models.ForeignKey(Employee, related_name='socials', on_delete=models.CASCADE, blank=True, null=True)
    linkedIn = models.URLField(max_length=200, null=True, blank=True)
    instagram = models.URLField(max_length=200, null=True, blank=True)
    dice = models.URLField(max_length=200, null=True, blank=True)
    monster = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f'{self.linkedIn}'
