import os
from django.shortcuts import render
from plotter.models import Metadata
from plotter.models import Data
import pandas as pd
from django.http import HttpResponse
from plotter.conections import con_ineq
from sqlalchemy import create_engine
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
import numpy as np


mi_ruta = "mysql://{}:{}@{}/{}".format(os.getenv("DB_USER_READ"), os.getenv("DB_PASSWORD_READ"),
                                       os.getenv("DB_HOST_READ"), os.getenv("DB_NAME_READ"))

engine = create_engine(mi_ruta)


def home(*args, **kwargs):
    return HttpResponseRedirect(reverse('admin:index'))


def extract(request):
    con = engine.connect()
    df1 = pd.read_csv("/home/ballesta/Documents/Psico/Inequality_app/media/data.csv", delimiter=",")
    df1.to_sql(Data._meta.db_table, con=con, if_exists='append', index=False)
    df2 = pd.read_csv("/home/ballesta/Documents/Psico/Inequality_app/media/metadata.csv", delimiter=",")
    df2.to_sql(Metadata._meta.db_table, con=con, if_exists='append', index=False)
    con.close()
    return HttpResponse("hola mundo")


def clean(request):
    con = con_ineq()
    cursor = con.cursor()
    table1 = Data.objects.model._meta.db_table
    sql1 = "DELETE FROM {}".format(table1)
    cursor.execute(sql1)
    cursor.execute("COMMIT")
    table2 = Metadata.objects.model._meta.db_table
    sql2 = 'DELETE FROM {}'.format(table2)
    cursor.execute(sql2)
    cursor.execute("COMMIT")
    con.close()
    return HttpResponse("la base a sido reiniciada")


def process(request):
    dt = pd.DataFrame.from_records(Data.objects.all().values())
    dt = dt.fillna(0)
    dt.loc[:, ~dt.columns.isin(['id', 'country_id', 'country_name', 'indicator_name', 'indicator_code'])]
    df = dt.mean().tolist()

    return redirect("/admin/")
