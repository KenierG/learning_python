from school_db import con, cur
import os
import bcrypt

status_menu = True
global status_op

nombres_tablas = [
    "countries",
    "departaments",
    "cities",
    "identification_types",
    "persons",
    "students",
    "users",
]

nombres_atributos = [
    [ "name", "abrev", "descrip" ],
    [ "name", "abrev", "descrip", "id_country" ],
    [ "name", "abrev", "descrip", "id_dep" ],
    [ "name", "abrev", "descrip" ],
    [ "first_name", "last_name", "id_ident_type", "ident_number", "id_exp_city", "address", "mobile", "id_user" ],
    [ "code", "id_person", "status" ],
    [ "email", "password", "status" ],
]

nombres_cols=[
     "name,abrev, descrip" ,
     "name, abrev, descrip, id_country" ,
     "name, abrev, descrip, id_dep" ,
     "name, abrev, descrip" ,
     "first_name, last_name, id_ident_type, ident_number, id_exp_city, address, mobile, id_user" ,
     "code, id_person, status" ,
     "email, password, status" ,
    
]

def hash_password(passwd):
    return bcrypt.hashpw(passwd.encode(), bcrypt.gensalt())

def create_data(values,cols,table,name):
    #Create a new user
    os.system('clear')

    values_query=""
    
    print(f"::: {name} Form :::")
    for value in values:
        values_query+="'"+(input(f"Your {value}: "))+"',"
    values_query = values_query[:-1]
    print(values_query)
    new_data = f'''
        INSERT INTO 
            {table} ({cols}) 
            VALUES({values_query})
    '''
    con.execute(new_data)
    con.commit()

    print(f"::: New {name} has been created sucessfully :::")
    os.system('pause')
    menu()


def menu():
    global opt
    status_opt = True
    while status_menu: 
        os.system('clear')
        print(":::::::::::::::::::::::")
        print(":::::: MAIN MENU ::::::")
        print(":::::::::::::::::::::::")
        print("[1]. Create countrie")
        print("[2]. Create departament")
        print("[3]. Create city")
        print("[4]. Create types identification")
        print("[5]. Create person")
        print("[6]. Create student")
        print("[7]. Create user")
        print("[8]. Exit")
        
        while status_opt:
            opt = input("Press an option: ")
            if opt < '1' or opt > '8':
                print(".:::::: Invalid option, try again.")
            else :
                status_opt = False

        if opt == '1':
            create_data(nombres_atributos[0], nombres_cols[0] ,nombres_tablas[0],nombres_tablas[0])
        elif opt == '2':
            create_data(nombres_atributos[1],nombres_cols[1],nombres_tablas[1],nombres_tablas[1])
        elif opt == '3':
            create_data(nombres_atributos[2],nombres_cols[2],nombres_tablas[2],nombres_tablas[2])
        elif opt == '4':
            create_data(nombres_atributos[3],nombres_cols[3],nombres_tablas[3],nombres_tablas[4])
        elif opt == '5':
            create_data(nombres_atributos[4],nombres_cols[4],nombres_tablas[4],nombres_tablas[4])
        elif opt == '6':
            create_data(nombres_atributos[5],nombres_cols[5],nombres_tablas[5],nombres_tablas[5])
        elif opt == '7':
            create_data(nombres_atributos[6],nombres_cols[6],nombres_tablas[6],nombres_tablas[6])
        else: 
            print("::: See 'u soon :::")
            exit()
    
#Call main menu
menu()

#Close connection
con.close()