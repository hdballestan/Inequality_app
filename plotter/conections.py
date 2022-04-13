import os
import pymysql


error_message = "Ocurrió un error al conectar: "

def con_ineq() -> pymysql.Connection:
    try:
        conexion = pymysql.connect(host=os.getenv("DB_HOST_READ"),
                                   user=os.getenv("DB_USER_READ"),
                                   password=os.getenv("DB_PASSWORD_READ"),
                                   database=os.getenv("DB_NAME_READ"))
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print(error_message, e)
    return conexion