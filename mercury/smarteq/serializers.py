from rest_framework import serializers
from .models import Address, Employee, Identity, Socials, Education, Company, \
    Passport, Visa, WorkAuthorization


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    officeAddress = AddressSerializer()

    class Meta:
        model = Company
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


class WorkAuthorizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkAuthorization
        fields = '__all__'


class IdentitySerializer(serializers.ModelSerializer):
    education = EducationSerializer(many=True)
    company = CompanySerializer(many=True)
    passport = PassportSerializer(many=True)
    visa = VisaSerializer(many=True)
    workAuthorization = WorkAuthorizationSerializer(many=True)

    class Meta:
        model = Identity
        fields = '__all__'


class SocialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Socials
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    identity = IdentitySerializer()
    socials = SocialsSerializer(many=True)
    primaryAddress = AddressSerializer()
    mailingAddress = AddressSerializer()

    class Meta:
        model = Employee
        fields = '__all__'
