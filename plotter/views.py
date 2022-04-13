import os
from django.shortcuts import render
from plotter.models import Metadata
import pandas as pd
from django.http import HttpResponse
from plotter.conections import con_ineq #para los queries
from sqlalchemy import create_engine
from django.http import HttpResponseRedirect


mi_ruta = "mysql://{}:{}@{}/{}".format(os.getenv("DB_USER_READ"), os.getenv("DB_PASSWORD_READ"),
                                       os.getenv("DB_HOST_READ"), os.getenv("DB_NAME_READ"))

engine = create_engine(mi_ruta)


def extract(request):
    con = engine.connect()
    df = pd.read_csv("/home/ytmor2/Documents/venom/Inequality_app/media/metadata.csv")
    df.to_sql(Metadata._meta.db_table, con=con, if_exists='append', index=False)
    con.close()


    return HttpResponse("hola mundo")

# Create your views here.
