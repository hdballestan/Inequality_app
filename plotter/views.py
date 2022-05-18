import os
import pandas as pd
from django.core import serializers
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse
from sqlalchemy import create_engine
from plotter.conections import con_ineq
from plotter.models import Data
from plotter.models import Metadata


def dashboard(request):
    return render(request, 'dashboard.html', {})


mi_ruta = "mysql://{}:{}@{}/{}".format(os.getenv("DB_USER_READ"), os.getenv("DB_PASSWORD_READ"),
                                       os.getenv("DB_HOST_READ"), os.getenv("DB_NAME_READ"))

engine = create_engine(mi_ruta)


def home(*args, **kwargs):
    return HttpResponseRedirect(reverse('admin:index'))


def extract(request):
    con = engine.connect()
    df1 = pd.read_csv(os.getenv("DATA"), delimiter=",")
    df1.to_sql(Data._meta.db_table, con=con, if_exists='append', index=False)
    df2 = pd.read_csv(os.getenv("METADATA"), delimiter=",")
    df2.to_sql(Metadata._meta.db_table, con=con, if_exists='append', index=False)
    con.close()
    return HttpResponse("hola mundo")


# def clean(request):
#     con = con_ineq()
#     cursor = con.cursor()
#     table1 = Data.objects.model._meta.db_table
#     sql1 = "DELETE FROM {}".format(table1)
#     cursor.execute(sql1)
#     cursor.execute("COMMIT")
#     table2 = Metadata.objects.model._meta.db_table
#     sql2 = 'DELETE FROM {}'.format(table2)
#     cursor.execute(sql2)
#     cursor.execute("COMMIT")
#     con.close()
#     return HttpResponse("la base a sido reiniciada")


def process(request):
    dataset = Data.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)
