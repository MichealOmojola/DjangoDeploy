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
        ('1', 1)
    ]

    firstname = forms.CharField(label='FIRST NAME', max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Enter Firstname'}))
    lastname = forms.CharField(label='LAST NAME', max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Enter Lastname'}))
    Dependents = forms.IntegerField(label='NUMBER OF DEPENDANTS', widget=forms.TextInput(attrs={'placeholder': 'Enter Number of Dependents'}))
    ApplicantIncome = forms.IntegerField(label="APPLICANT'S INCOME", widget=forms.TextInput(attrs={'placeholder': 'Enter Monthly Gross Income'}))
    LoanAmount = forms.IntegerField(label="LOAN AMOUNT", widget=forms.TextInput(attrs={'placeholder': 'Enter Loan Amount'}))
    Loan_Amount_Term = forms.IntegerField(label='LOAN TENOR', widget=forms.TextInput(attrs={'placeholder': 'Enter Loan Tenor'}))
    Credit_History = forms.ChoiceField(label='CREDIT HISTORY', choices=CREDIT_HISTORY_CHOICES)
    Gender = forms.ChoiceField(label='GENDER', choices=GENDER_CHOICES)
    Married = forms.ChoiceField(label='MARITAL STATUS', choices=MARRIED_CHOICES)
    Education = forms.ChoiceField(label='EDUCATION', choices=GRADUATED_CHOICES)
    Self_Employed = forms.ChoiceField(label='EMPLOYMENT STATUS', choices=SELFEMPLOYED_CHOICES)
    Property_Area = forms.ChoiceField(label='RESIDENTIAL AREA', choices=PROPERTY_CHOICES)