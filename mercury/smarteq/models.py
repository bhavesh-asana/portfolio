from django.db import models
from django.core.validators import RegexValidator

phoneNumber_validator = RegexValidator(
    regex=r'^\+?1?\d{9,13}$',
    message="Phone number must be entered in the format: '+1 (XXX) XXX-XXXX")


class Address(models.Model):
    street_1 = models.CharField(max_length=150, blank=True, null=True)
    street_2 = models.CharField(max_length=150, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    postalCode = models.CharField(max_length=7, blank=True, null=True)

    def __str__(self):
        return f'{self.street_1}, {self.street_2}, {self.city}, {self.state}, {self.country} - {self.postalCode}'


class Employee(models.Model):
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    phoneNumber = models.CharField(validators=[phoneNumber_validator], max_length=13, blank=False)
    personalEmail = models.EmailField(null=True, blank=True)
    primaryAddress = models.ForeignKey(Address, related_name='primaryAddress', on_delete=models.CASCADE, blank=True,
                                       null=True)
    mailingAddress = models.ForeignKey(Address, related_name='mailingAddress', on_delete=models.CASCADE, blank=True,
                                       null=True)
    """
        Links:
        1-1: Identity
        1-M: Socials
    """

    def __str__(self):
        return f'{self.firstName}, {self.lastName}'


class Identity(models.Model):
    employee = models.OneToOneField(Employee, related_name='identity', on_delete=models.CASCADE)
    profilePhoto = models.ImageField(null=True, blank=True)
    dateOfBirth = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    socialSecurity = models.CharField(max_length=5, blank=True, null=True)
    """
        Links:
        1-M : Education
        1-M : Company
        1-M : Passport
        1-M : Visa
        1-M : WorkAuthorization
    """

    def __str__(self):
        return f'Identity - {self.employee.firstName}, {self.employee.lastName}'


class Socials(models.Model):
    employee = models.ForeignKey(Employee, related_name='socials', on_delete=models.CASCADE, blank=True, null=True)
    linkedIn = models.URLField(max_length=200, null=True, blank=True)
    instagram = models.URLField(max_length=200, null=True, blank=True)
    dice = models.URLField(max_length=200, null=True, blank=True)
    monster = models.URLField(max_length=200, null=True, blank=True)

    # TODO: check for more field outs
    def __str__(self):
        return f'{self.employee.firstName}'


class Education(models.Model):
    identity = models.ForeignKey(Identity, on_delete=models.CASCADE, related_name='education', null=True, blank=True)
    schoolName = models.CharField(max_length=255, null=True, blank=True)
    major = models.CharField(max_length=255, null=True, blank=True)
    startDate = models.DateField(auto_now=False, auto_now_add=False)
    endDate = models.DateField(auto_now=False, auto_now_add=False)
    cityOfSchool = models.CharField(max_length=255, null=True, blank=True)
    stateOfSchool = models.CharField(max_length=255, null=True, blank=True)
    countryOfSchool = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f'{self.schoolName}'


class Company(models.Model):
    identity = models.ForeignKey(Identity, on_delete=models.CASCADE, related_name='company', null=True, blank=True)
    companyName = models.CharField(max_length=255)
    designation = models.CharField(max_length=256, null=True, blank=True)
    startDate = models.DateField(auto_now=False, auto_now_add=False, null=True)
    endDate = models.DateField(auto_now=False, auto_now_add=False, null=True)
    phoneNumber = models.CharField(validators=[phoneNumber_validator], max_length=13, blank=True)
    officeAddress = models.ForeignKey(Address, related_name='officeAddress', on_delete=models.CASCADE, blank=True,
                                      null=True)

    def __str__(self):
        return str(self.companyName)


class Passport(models.Model):
    identity = models.ForeignKey(Identity, on_delete=models.CASCADE, related_name='passport', null=True, blank=True)
    passportNumber = models.CharField(max_length=12, null=True, blank=True)
    placeOfIssue = models.CharField(max_length=255, null=True, blank=True)
    countryIssued = models.CharField(max_length=255, null=True, blank=True)
    dateOfIssue = models.DateField(auto_now=False, auto_now_add=False)
    dateOfExpiry = models.DateField(auto_now=False, auto_now_add=False)

    """
        Links:
        1-M : Visa
    """

    def __str__(self):
        return f'{self.passportNumber}'


class Visa(models.Model):
    identity = models.ForeignKey(Identity, on_delete=models.CASCADE, related_name='visa', null=True, blank=True)
    passport = models.ForeignKey(Passport, on_delete=models.CASCADE, null=True, blank=True)
    gatedCountry = models.CharField(max_length=256, blank=True, null=True)
    typeOfVisa = models.CharField(max_length=10)
    dateOfIssue = models.DateField(auto_now=False, auto_now_add=False)
    dateOfExpiry = models.DateField(auto_now=False, auto_now_add=False)
    """
            Links:
            1-M : WorkAuthorization
        """

    def __str__(self):
        return f'{self.typeOfVisa}'


class WorkAuthorization(models.Model):
    identity = models.ForeignKey(Identity, related_name='workAuthorization', on_delete=models.CASCADE, null=True,
                                 blank=True)
    visa = models.ForeignKey(Visa, related_name='visa', on_delete=models.CASCADE, null=True, blank=True)
    typeOfAuthorization = models.CharField(max_length=255)
    dateOfValidity = models.DateField(auto_now=False, auto_now_add=False)
    dateOfExpiry = models.DateField(auto_now=False, auto_now_add=False)
    uscisNumber = models.CharField(max_length=100, unique=True)
    cardNumber = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f'{self.typeOfAuthorization}'
