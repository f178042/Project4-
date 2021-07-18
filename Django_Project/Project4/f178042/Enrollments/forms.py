from django import forms
from Enrollments.models import Enrollment
class EnrollmentFrom(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = "__all__"
