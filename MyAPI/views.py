from django.shortcuts import render
# from .forms import MyForm
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from django.core import serializers
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.contrib import messages
from .forms import ApprovalForm
from .models import approvals
from .serializers import approvalSerializers
import os
import pickle
# from sklearn.externals import joblib
import json
import numpy as np
import pandas as pd
from keras import backend as K
# from .make_pickle_packable import make_keras_picklable

import joblib

# from unpickleload import make_keras_picklable

import tensorflow as tf


# @tf.function
# def predict(model, df):
#     return model.predict(x=df,verbose=0)



# Create your views here.

class ApprovalsView(viewsets.ModelViewSet):
    queryset = approvals.objects.all()
    serializer_class = approvalSerializers

dir_path = os.path.dirname(os.path.realpath(__file__))

model_address = f'{dir_path}/loan_model.pkl'
scaler_address = f'{dir_path}/scaler.pkl'

# model_address = 'loan_model.joblib'
# scaler_address = 'scaler.joblib'

def ohevalue(df):
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

# @api_view(["POST"])
def approvereject(unit):



    try:
        # mdl = joblib.load(model_address)
        # scalers = joblib.load(scaler_address)

        # joblib.load(filename, mmap_mode=None)
        # joblib.load(filename, mmap_mode=None)


        with open(model_address, "rb") as input_file:
            mdl = pickle.load(input_file)
        with open(scaler_address, "rb") as input_file:
            scalers = pickle.load(input_file)
        # mdl = joblib.load(model_address)
        # scalers = joblib.load(scaler_address)

        # print(model_address)

        # mydata = request.data
        # unit = np.array(list(mydata.values()))
        # unit = unit.reshape(1, -1)
        scalers.fit(unit)
        X=scalers.transform(unit)
        # y_pred=mdl.predict(X)
        y_pred=mdl(X)
        # y_pred=predict(mdl, X)
        y_pred=(y_pred > 0.45)
        # newdf = pd.DataFrame(y_pred, columns=['Status'])
        # newdf = newdf.replace({True:'Approved', False:'Rejected'})
        # if y_pred == 'Approved':
        #     return 'You are eligible for a loan.'
        #     # return JsonResponse(f'You are eligible for a loan.', safe=False)
        # else:
        #     return 'Sorry! You are not eligible for a loan.'
        #     # return JsonResponse(f'You are eligible for a loan.', safe=False)
        newdf=pd.DataFrame(y_pred, columns=['Status'])
        newdf=newdf.replace({True:'Approved', False:'Rejected'})
        K.clear_session()
        return (newdf.values[0][0],X[0])
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
            df = pd.DataFrame(myDict, index = [0])
            answer = approvereject(ohevalue(df))[0]
            # print(approvereject(ohevalue(df)))
            Xscalers = approvereject(ohevalue(df))[1]
            messages.success(request, 'Application Status: {}'.format(answer))

            # print(approvereject(ohevalue(df)))
            # print(ohevalue(df))
            # print(firstname, lastname, Dependents, Married, Property_Area)

    form=ApprovalForm()
    return render(request, 'myform/cxform.html', {'form':form})