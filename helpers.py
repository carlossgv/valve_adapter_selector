import sqlite3
from sqlite3 import Error
import os.path

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path, check_same_thread=False)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

def get_adapter(brand, serie, size, act_type, act_size):

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "postgres://umegczflkjlthm:994a074c6a9844cfae6294a00b433acfb856241465441ae360467da2494886a6@ec2-50-19-26-235.compute-1.amazonaws.com:5432/det01m93m70fln
")
    print(db_path)

    db = create_connection(db_path)
    # db = create_connection("Bray_Database.db")

    # CONEXION CON BASE DE DATOS PARA CONSEGUIR DATOS DE VALVULAS (SIRVE PARA TODAS LAS MARCAS)
    val_data = db.execute("SELECT PN, BRAND, NAME, MIN(SIZE), VMCODE FROM VALVES "
                          "WHERE BRAND = ? AND SERIE = ? AND SIZE = ?",
                          (brand.upper(), serie, size))

    for row in val_data:
        print(row)
        val_pn = row[0]
        vmcode = row[4]


    # DEPENDIENDO LA MARCA ES DIFERENTE LA FORMA DE CONSEGUIR EL MONTAJE
    # PARA BRAY
    if brand.upper() == "BRAY":
        act_data = db.execute("SELECT * FROM ACTUATORS "
                              "WHERE TYPE = ? AND SIZE = ?",
                              (act_type, act_size))



        for row in act_data:
            adapter_codes = row[5]
            print(row)

        print(vmcode)
        print(adapter_codes)

        if vmcode not in adapter_codes or None:
            return ("Actuator can't be mounted","")
        elif vmcode + "0" in adapter_codes:
            return ("Adapter not required, direct mounting","")
        else:
            for i in range(len(adapter_codes)):
                if adapter_codes[i] == vmcode:
                    required_adapter = vmcode + adapter_codes[i + 1]
                    print(required_adapter)

                    sleeve_data = db.execute("SELECT PN FROM ACCESORIES WHERE NAME LIKE ?",
                                             ('%'+required_adapter,))

                    for row in sleeve_data:
                        sleeve_pn = row[0]

                    return (f'Adapter required: {required_adapter}', f'P/N: {sleeve_pn}')

    # PARA FLOW-TEK
    elif brand.upper() == "FLOW-TEK":

        if act_type.upper() == "HANDLE":
            return ("Ball valves have handles included","")
        elif act_type.upper() == "GEAR OPERATOR":
            return ("No information available for gear operators, contact factory","")

        mounting = ''

        if act_type.upper() == "ELECTRIC":
            act_data = db.execute("SELECT (%s) FROM KITELEC WHERE PN = ?" % ("`" + act_size + "`"),
                                  (val_pn,))

            for row in act_data:
                mounting = row[0]
                print(mounting)

            if mounting == '' or mounting == None:
                return ("Actuator can't be mounted","")
            else:
                return (f"Mounting Kit required: {mounting}","")

        elif act_type.upper() == "PNEUMATIC":
            act_data = db.execute("SELECT (%s) FROM KITPNEU WHERE PN = ?" % ("`" + act_size + "`"),
                                  (val_pn,))

            for row in act_data:
                mounting = row[0]

            if mounting == '' or mounting == None:
                return ("Actuator can't be mounted","")
            else:
                return (f"Mounting Kit required: {mounting}","")
