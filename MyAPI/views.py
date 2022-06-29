from django.shortcuts import render
# from .forms import MyForm
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.contrib import messages
from .forms import ApprovalForm
from .models import approvals
from .serializers import approvalSerializers
import os
import pickle
# from sklearn.externals import joblib
import pandas as pd
from keras import backend as K
# from .make_pickle_packable import make_keras_picklable
# from .unpickleload import *
import joblib

# from unpickleload import make_keras_picklable

# Create your views here.
class ApprovalsView(viewsets.ModelViewSet):
    queryset = approvals.objects.all()
    serializer_class = approvalSerializers

dir_path = os.path.dirname(os.path.realpath(__file__))

model_address = f'{dir_path}/loan_model.pkl'
scaler_address = f'{dir_path}/scaler.pkl'

def read_pickle(address):
    data = pickle.load(open(address,'rb'))
    return data

ohe_col = ['Dependents',
            'ApplicantIncome',
            'CoapplicantIncome',
            'LoanAmount',
            'Loan_Amount_Term',
            'Credit_History',
            'Gender_Female',
            'Gender_Male',
            'Married_No',
            'Married_Yes',
            'Education_Graduate',
            'Education_Not_Graduate',
            'Self_Employed_No',
            'Self_Employed_Yes',
            'Property_Area_Rural',
            'Property_Area_Semiurban',
            'Property_Area_Urban']

def myPreprocessor(myDict):
    df = pd.DataFrame(myDict, index = [0])
    cat_columns = ['Gender', 'Married', 'Education', 'Self_Employed', 'Property_Area']
    df_processed = pd.get_dummies(df, columns=cat_columns)
    newdict = {}
    for i in ohe_col:
        if i in df_processed.columns:
            newdict[i] = df_processed[i].values
        else:
            newdict[i] = 0
    newdf = pd.DataFrame(newdict)

    return newdf

# with open(model_address, "rb") as input_file:
#     mdl = pickle.load(input_file)
# with open(scaler_address, "rb") as input_file:
#     scalers = pickle.load(input_file)


# @api_view(["POST"])
def approvereject(unit):
    try:
        mdl = read_pickle(model_address)
        scalers = read_pickle(scaler_address)
        scalers.fit(unit)
        X=scalers.transform(unit)
        y_pred=mdl(X)
        y_pred=(y_pred > 0.45)
        newdf=pd.DataFrame(y_pred, columns=['Status'])
        result=newdf.replace({True:'Approved', False:'Rejected'}).values[0][0]
        K.clear_session()
        return result
    except ValueError as e:
        return (e.args[0])


def cxcontact(request):
    if request.method=='POST':
        form=ApprovalForm(request.POST)
        if form.is_valid():
            firstname=form.cleaned_data['firstname']
            lastname=form.cleaned_data['lastname']
            Dependents=form.cleaned_data['Dependents']
            ApplicantIncome=form.cleaned_data['ApplicantIncome']
            CoapplicantIncome=form.cleaned_data['CoapplicantIncome']
            LoanAmount=form.cleaned_data['LoanAmount']
            Loan_Amount_Term=form.cleaned_data['Loan_Amount_Term']
            Credit_History=form.cleaned_data['Credit_History']
            Gender=form.cleaned_data['Gender']
            Married=form.cleaned_data['Married']
            Education=form.cleaned_data['Education']
            Self_Employed=form.cleaned_data['Self_Employed']
            Property_Area=form.cleaned_data['Property_Area']
            myDict = (request.POST).dict()
            df = myPreprocessor(myDict)
            answer = approvereject(df)
            messages.success(request, 'Application Status: {}'.format(answer))

    form=ApprovalForm()
    return render(request, 'myform/cxform.html', {'form':form})