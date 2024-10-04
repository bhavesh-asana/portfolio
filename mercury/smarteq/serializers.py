from rest_framework import serializers
from .models import Address, Socials, Education, Passport, Visa, EmploymentAuthorization, Employee, Manager, Recruiter, Company


class AddressSerializer(serializers.ModelSerializer):
  class Meta:
    model = Address
    fields = '__all__'

class CompanySerializer(serializers.ModelSerializer):
  class Meta:
    model = Company
    fields = '__all__'

class EducationSerializer(serializers.ModelSerializer):
  class Meta:
    model = Education
    fields = '__all__'


class PassportSerializer(serializers.ModelSerializer):
  class Meta:
    model = Passport
    fields = '__all__'

class VisaSerializer(serializers.ModelSerializer):
  passport = PassportSerializer()
  class Meta:
    model = Visa
    fields = '__all__'

    
class EmploymentAuthorizationSerializer(serializers.ModelSerializer):
  class Meta:
    model = EmploymentAuthorization
    fields = '__all__'

class ManagerSerializer(serializers.ModelSerializer):
  class Meta:
    model = Manager
    fields = '__all__'

class RecruiterSerializer(serializers.ModelSerializer):
  manager = ManagerSerializer()
  class Meta:
    model = Recruiter
    fields = '__all__'

class SocialsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Socials
    fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
  primaryAddress = AddressSerializer()
  mailingAddress = AddressSerializer()
  officeAddress = AddressSerializer()
  company = CompanySerializer()
  education = EducationSerializer(many=True)
  passport = PassportSerializer(many=True)
  visa = VisaSerializer(many=True)
  employmentAuthorization = EmploymentAuthorizationSerializer(many=True)
  manager = ManagerSerializer()
  recruiter = RecruiterSerializer()
  socials = SocialsSerializer(many=True)
  class Meta:
    model = Employee
    fields = ['firstName', 'lastName', 'phoneNumber', 'dateOfBirth', 'primaryAddress', 'mailingAddress', 'officeAddress', 'photo', 'company', 'education', 'passport', 'visa', 'employmentAuthorization', 'manager', 'recruiter', 'socials']