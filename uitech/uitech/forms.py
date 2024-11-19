# forms.py
from django import forms
from .models import CandidateRequirement, InternshipStudents

class CandidateRequirementForm(forms.ModelForm):
    class Meta:
        model = CandidateRequirement
        fields = '__all__'
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'inp1 w-100 mb-3', 'required': True}),
            'designation': forms.TextInput(attrs={'class': 'inp1 w-100 mb-3', 'required': True}),
            'phone': forms.TextInput(attrs={'class': 'inp2 w-100 mb-3', 'required': True}),
            'company_name': forms.TextInput(attrs={'class': 'inp2 w-100 mb-3', 'required': True}),
            'website': forms.URLInput(attrs={'class': 'inp1 w-100 mb-3', 'required': True}),
            'email': forms.EmailInput(attrs={'class': 'inp1 w-100 mb-3', 'required': True}),
            'domain': forms.TextInput(attrs={'class': 'inp2 w-100 mb-3', 'required': True}),
            'experience': forms.Select(attrs={'id': 'lang', 'class': 'w-100 mb-3', 'required': True}),
            'positions': forms.NumberInput(attrs={'class': 'inp1 w-100 mb-3', 'min': 1, 'required': True}),
            'salary': forms.TextInput(attrs={'class': 'inp2 w-100 mb-3', 'required': True}),
            'location': forms.TextInput(attrs={'class': 'inp1 w-100 mb-3', 'required': True}),
            'job_description': forms.FileInput(attrs={'class': 'inp1 w-100'}),
            'profile_pic': forms.FileInput(attrs={'class': 'inp1 w-100'}),
            'message': forms.Textarea(attrs={'class': 'message w-100 mb-3', 'rows': 3}),
            'note': forms.Textarea(attrs={'class': 'message w-100 mb-3', 'rows':2}),
        }

class InternshipStudentsForm(forms.ModelForm):
    class Meta:
        model = InternshipStudents
        fields = '__all__'
        widget = {
            'full_name': forms.TextInput(attrs={'class': 'inp1 w-100 mb-3', 'required': True}),
            'course': forms.TextInput(attrs={'class': 'inp2 w-100 mb-3', 'required': True}),
            'profile_pic': forms.FileInput(attrs={'class': 'inp1 w-100'}),
        }



class InternshipForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your name'})
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'})
    )
    phone = forms.CharField(
        max_length=15,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your phone number'})
    )
    passout_year = forms.CharField(
        max_length=4,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter year of passout'})
    )
    graduation = forms.ChoiceField(
        choices=[('Select', '--Select--'), ('B.Tech', 'B.Tech'), ('Degree', 'Degree'), ('Other', 'Other')],
        required=True
    )
    course = forms.ChoiceField(
        choices=[
            ('Select', '--Select--'), ('C Language', 'C Language'), ('C++', 'C++'),
            ('Front-End technologies', 'Front-End technologies'), ('Python', 'Python'),
            ('Java', 'Java'), ('Node', 'Node'), ('Digital Marketing', 'Digital Marketing'), ('Other', 'Other')
        ],
        required=True
    )
    duration = forms.ChoiceField(
        choices=[('Select', '--Select--'), ('2 Months', '2 Months'), ('4 Months', '4 Months'), ('6 Months', '6 Months')],
        required=True
    )
    gender = forms.ChoiceField(
        choices=[('Select', '--Select--'), ('Male', 'Male'), ('Female', 'Female')],
        required=True
    )
    source = forms.ChoiceField(
        choices=[
            ('Select', '--Select--'), ('Instagram', 'Instagram'), ('Facebook', 'Facebook'),
            ('LinkedIn', 'LinkedIn'), ('YouTube', 'YouTube'), ('Other', 'Other')
        ],
        required=True
    )
    terms = forms.BooleanField(
        required=True,
        widget=forms.CheckboxInput(attrs={'class': 'custom-checkbox'}),
        error_messages={'required': 'You must agree to the terms and conditions.'}
    )



class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=15, required=False)
    subject = forms.ChoiceField(choices=[
        ('General Inquiry', 'General Inquiry'),
        ('Support', 'Support'),
        ('Feedback', 'Feedback'),
        ('Other', 'Other')
    ])
    message = forms.CharField(widget=forms.Textarea, required=False)
    