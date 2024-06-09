import psycopg2
import st_model

def get_Students_By_Specialization(flag, connection, specialization_number):
    rezult = None
    if flag == True:
        rezult = st_model.Students_data_by_specialization_number(connection, specialization_number)
        pass
    return rezult

def get_Students_Personal_Data_By_Specialization_Number(flag, connection, specialization_number):
    rezult = None
    if flag == True:
        rezult = st_model.Students_personal_data_by_specialization_number(connection, specialization_number)
        pass
    return rezult

def get_Subjects_by_specialization_number(flag, connection, specialization_number):
    rezult = None
    if flag == True:
        rezult = st_model.Subjects_by_specialization_number(connection, specialization_number)
        pass
    return rezult

def get_Students_data_by_FIO_and_specialization_number(flag, connection, last_name, first_name, father_name, specialization_number):
    rezult = None
    if flag == True:
        rezult = st_model.Students_data_by_FIO_and_specialization_number(connection, last_name, first_name, father_name, specialization_number)
        pass
    return rezult

def get_All_Specialization(flag, connection):
    rezult = None
    if flag == True:
        rezult = st_model.all_Specializations(connection)
        pass
    return rezult

def get_NameString_From_String(str):
    str_new = ""
    i = 0
    for sym in str:
        if sym.isalpha():
            if i == 0:
                sym = sym.upper()
                pass
            else:
                sym = sym.lower()
                pass
            str_new += sym
            i += 1
            pass
        pass
    return str_new

def make_NewStudentPython(flag, connection, lastname, firstname, fathername, genderismale, age, \
                              pointnumber_osnovi, pointnumber_algoritmi, pointnumber_git, pointnumber_html5_css, \
                              pointnumber_python_level1, pointnumber_postgresql_level1, pointnumber_python_level2, \
                              pointnumber_python_level3):
    flag2 = False
    rezult = False
    if flag == True:
        try:
            st_model.create_New_Student_Python(connection, lastname, firstname, fathername, genderismale, age, \
                              pointnumber_osnovi, pointnumber_algoritmi, pointnumber_git, pointnumber_html5_css, \
                              pointnumber_python_level1, pointnumber_postgresql_level1, pointnumber_python_level2, \
                              pointnumber_python_level3)
            print("Метод с SQL запросом отработал.")
            flag2 = True
        except Exception as e:
            print(e)
            flag2 = False
        pass
    if ((flag == True)and(flag2 == True)):
        rezult = True
    else:
        rezult = False
    return rezult

def make_NewStudentJava(flag, connection, lastname, firstname, fathername, genderismale, age, \
                              pointnumber_osnovi, pointnumber_algoritmi, pointnumber_git, pointnumber_c, \
                              pointnumber_java_level1, pointnumber_postgresql_level1, pointnumber_java_level2, \
                              pointnumber_spring):
    flag2 = False
    rezult = False
    if flag == True:
        try:
            st_model.create_New_Student_Java(connection, lastname, firstname, fathername, genderismale, age, \
                              pointnumber_osnovi, pointnumber_algoritmi, pointnumber_git, pointnumber_c, \
                              pointnumber_java_level1, pointnumber_postgresql_level1, pointnumber_java_level2, \
                              pointnumber_spring)
            flag2 = True
        except Exception as e:
            print(e)
            flag2 = False
        pass
    if ((flag == True) and (flag2 == True)):
        rezult = True
    else:
        rezult = False
    return rezult

def make_NewStudentCSharp (flag, connection, lastname, firstname, fathername, genderismale, age, \
                              pointnumber_osnovi, pointnumber_algoritmi, pointnumber_git, pointnumber_c, \
                              pointnumber_c_sharp_level1, pointnumber_c_sharp_level2, pointnumber_postgresql_level1, \
                              pointnumber_c_sharp_level3, pointnumber_html5_css, pointnumber_c_sharp_level4, \
                                pointnumber_javascript_level1, pointnumber_javascript_level2):
    flag2 = False
    rezult = False
    if flag == True:
        try:
            st_model.create_New_Student_C_sharp (connection, lastname, firstname, fathername, genderismale, age, \
                              pointnumber_osnovi, pointnumber_algoritmi, pointnumber_git, pointnumber_c, \
                              pointnumber_c_sharp_level1, pointnumber_c_sharp_level2, pointnumber_postgresql_level1, \
                              pointnumber_c_sharp_level3, pointnumber_html5_css, pointnumber_c_sharp_level4, \
                                pointnumber_javascript_level1, pointnumber_javascript_level2)
            flag2 = True
        except Exception as e:
            print(e)
            flag2 = False
        pass
    if ((flag == True) and (flag2 == True)):
        rezult = True
    else:
        rezult = False
    return rezult

def make_NewStudentAdmin (flag, connection, lastname, firstname, fathername, genderismale, age, \
                              pointnumber_osnovi, pointnumber_osnovi_setey, pointnumber_linux_level1, pointnumber_data_analiz, \
                              pointnumber_postgresql_level1, pointnumber_postgresql_level2, pointnumber_postgresql_level3, pointnumber_qpt):
    flag2 = False
    rezult = False
    if flag == True:
        try:
            st_model.create_New_Student_Admin (connection, lastname, firstname, fathername, genderismale, age, \
                              pointnumber_osnovi, pointnumber_osnovi_setey, pointnumber_linux_level1, pointnumber_data_analiz, \
                              pointnumber_postgresql_level1, pointnumber_postgresql_level2, pointnumber_postgresql_level3, pointnumber_qpt)
            flag2 = True
        except Exception as e:
            print(e)
            flag2 = False
        pass
    if ((flag == True) and (flag2 == True)):
        rezult = True
    else:
        rezult = False
    return rezult

def make_NewStudentIngener (flag, connection, lastname, firstname, fathername, genderismale, age, \
                              pointnumber_osnovi, pointnumber_algoritmi, pointnumber_git, \
                              pointnumber_postgresql_level1, pointnumber_c_sharp_level1, pointnumber_c_sharp_level2, \
                              pointnumber_html_xml, pointnumber_c_sharp_level3, pointnumber_c_sharp_level4, pointnumber_java_level1, \
                              pointnumber_python_level1, pointnumber_oracle, pointnumber_c_plus_plus, pointnumber_html5_css_3, \
                                pointnumber_javascript_level1):
    flag2 = False
    rezult = False
    if flag == True:
        try:
            st_model.create_New_Student_Ingener (connection, lastname, firstname, fathername, genderismale, age, \
                              pointnumber_osnovi, pointnumber_algoritmi, pointnumber_git, \
                              pointnumber_postgresql_level1, pointnumber_c_sharp_level1, pointnumber_c_sharp_level2, \
                              pointnumber_html_xml, pointnumber_c_sharp_level3, pointnumber_c_sharp_level4, pointnumber_java_level1, \
                              pointnumber_python_level1, pointnumber_oracle, pointnumber_c_plus_plus, pointnumber_html5_css_3, \
                                pointnumber_javascript_level1)
            flag2 = True
        except Exception as e:
            print(e)
            flag2 = False
        pass
    if ((flag == True) and (flag2 == True)):
        rezult = True
    else:
        rezult = False
    return rezult

def deleteStudentData (flag, connection, st_id_str):
    flag2 = False
    rezult = False
    if flag == True:
        try:
            st_model.delete_Student_Data(connection, st_id_str)
            flag2 = True
        except Exception as e:
            print(e)
            flag2 = False
        pass
    if ((flag == True) and (flag2 == True)):
        rezult = True
    else:
        rezult = False
    return rezult