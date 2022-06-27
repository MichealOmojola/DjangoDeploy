from django import forms

class ApprovalForm(forms.Form):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female')
    ]
    MARRIED_CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No')
    ]
    GRADUATED_CHOICES = [
        ('Graduate', 'Graduate'),
        ('Not_Graduate', 'Not_Graduate')
    ]
    SELFEMPLOYED_CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No')
    ]
    PROPERTY_CHOICES = [
        ('Rural', 'Rural'),
        ('Semiurban', 'Semiurban'),
        ('Urban', 'Urban')
    ]
    CREDIT_HISTORY_CHOICES = [
        ('0', 0),
        ('1', 1),
        ('2', 2),
        ('3', 3)
    ]

    firstname = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Enter Firstname'}))
    lastname = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Enter Lastname'}))
    Dependents = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Enter Number of Dependents'}))
    ApplicantIncome = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Enter Monthly Gross Income'}))
    CoapplicantIncome = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Enter Co-Applicant Monthly Gross Income'}))
    LoanAmount = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Enter Loan Amount'}))
    Loan_Amount_Term = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Enter Term in Months'}))
    Credit_History = forms.ChoiceField(choices=CREDIT_HISTORY_CHOICES)
    Gender = forms.ChoiceField(choices=GRADUATED_CHOICES)
    Married = forms.ChoiceField(choices=MARRIED_CHOICES)
    Education = forms.ChoiceField(choices=GRADUATED_CHOICES)
    Self_Employed = forms.ChoiceField(choices=SELFEMPLOYED_CHOICES)
    Property_Area = forms.ChoiceField(choices=PROPERTY_CHOICES)