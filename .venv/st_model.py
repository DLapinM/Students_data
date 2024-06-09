import psycopg2

def st_Db_Connect(db_user, db_password, db_name, db_host, db_port):
    connect_rezult = None
    flag_rezult = False
    try:
        connect_rezult = psycopg2.connect(dbname=db_name, user=db_user, host='localhost', password=db_password, port=db_port)
        flag_rezult = True
        return (flag_rezult, connect_rezult)
    except:
        connect_rezult = None
        flag_rezult = False
        return (flag_rezult, connect_rezult)

def st_Db_Disconnect(flag, connection):
    if flag:
        connection.close()
        return True
    else:
        return False

def Students_data_by_specialization_number(connection, specialization_number):
    rezult = None
    specialization_number = str(specialization_number)
    cursor = connection.cursor()
    cursor.execute('SELECT LastName AS "Фамилия", FirstName AS "Имя", FatherName AS "Отчество", SubjectName AS "Предмет", PointNumber AS "Оценка" \
                        FROM public.Students st \
                        INNER JOIN \
                        (SELECT * FROM public.Student_Subject) ss2 \
                        ON ss2.Student_Id = st.Id \
                        INNER JOIN \
                        (SELECT * FROM public.Subjects) sub \
                        ON sub.Id = ss2.Subject_Id \
                        WHERE st.SpecializationId=' + specialization_number + '\
                        ORDER BY LastName, FirstName, FatherName, subject_id')
    rezult = cursor.fetchall()
    cursor.close()
    return rezult

def Students_personal_data_by_specialization_number(connection, specialization_number):
    rezult = None
    specialization_number = str(specialization_number)
    cursor = connection.cursor()
    str_command = 'SELECT id AS "ID", LastName AS "Фамилия", FirstName AS "Имя", FatherName AS "Отчество", ' \
                  + "CASE WHEN genderismale=true THEN 'Мужской' " \
                  + "WHEN genderismale=false THEN 'Женский' END Пол, " \
                  + 'age AS "Возраст" ' \
                  + 'FROM public.Students st ' \
                  + 'WHERE (st.SpecializationId=' + specialization_number + ') ' \
                  + 'ORDER BY (LastName, FirstName, FatherName) '
    cursor.execute(str_command)
    rezult = cursor.fetchall()
    cursor.close()
    return rezult

def Subjects_by_specialization_number(connection, specialization_number):
    rezult = None
    specialization_number = str(specialization_number)
    cursor = connection.cursor()
    str_command = 'SELECT subjectname AS "Предмет" ' \
                  + 'FROM public.subjects sub ' \
                  + 'INNER JOIN ' \
                  + '(SELECT * FROM public.specialization_subject) ss2 ' \
                  + 'ON sub.id = ss2.subject_id ' \
                  + 'WHERE (ss2.specialisation_id=' + specialization_number + ') ' \
                  + 'ORDER BY (sub.id) '
    cursor.execute(str_command)
    rezult = cursor.fetchall()
    cursor.close()
    return rezult

def Students_data_by_FIO_and_specialization_number(connection, last_name, first_name, father_name, specialization_number):
    rezult = None
    specialization_number = str(specialization_number)
    cursor = connection.cursor()
    str_command = 'SELECT LastName AS "Фамилия", FirstName AS "Имя", FatherName AS "Отчество", SubjectName AS "Предмет", PointNumber AS "Оценка" ' \
                            + 'FROM public.Students st ' \
                            + 'INNER JOIN ' \
                            + '(SELECT * FROM public.Student_Subject) ss2 ' \
                            + 'ON ss2.Student_Id = st.Id ' \
                            + 'INNER JOIN ' \
                            + '(SELECT * FROM public.Subjects) sub ' \
                            + 'ON sub.Id = ss2.Subject_Id ' \
                            + "WHERE (st.SpecializationId=" + specialization_number + ") AND (st.LastName = '" + last_name + "') AND (st.FirstName = '" + first_name + "') AND (st.FatherName = '" + father_name + "') " \
                            + "ORDER BY LastName, FirstName, FatherName, subject_id"
    cursor.execute(str_command)
    rezult = cursor.fetchall()
    cursor.close()
    return rezult

def all_Specializations(connection):
    rezult = None
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM specializations \
                    ORDER BY id')
    rezult = cursor.fetchall()
    cursor.close()
    return rezult

def create_New_Student_Python (connection, lastname, firstname, fathername, genderismale, age, \
                              pointnumber_osnovi, pointnumber_algoritmi, pointnumber_git, pointnumber_html5_css, \
                              pointnumber_python_level1, pointnumber_postgresql_level1, pointnumber_python_level2, \
                              pointnumber_python_level3):
    rezult = None
    cursor = connection.cursor()
    str_command = "SELECT make_new_student_python(" \
                    + "'" + lastname + "', " \
                    + "'" + firstname + "', " \
                    + "'" + fathername + "', " \
                    + genderismale + ", " \
                    + age + ", " \
                    + pointnumber_osnovi + ", " \
                    + pointnumber_algoritmi + ", " \
                    + pointnumber_git + ", " \
                    + pointnumber_html5_css + ", " \
                    + pointnumber_python_level1 + ", " \
                    + pointnumber_postgresql_level1 + ", " \
                    + pointnumber_python_level2 + ", " \
                    + pointnumber_python_level3 \
                    + ");"
    cursor.execute(str_command)
    rezult = cursor.fetchall()
    cursor.close()
    return rezult

def create_New_Student_Java (connection, lastname, firstname, fathername, genderismale, age, \
                              pointnumber_osnovi, pointnumber_algoritmi, pointnumber_git, pointnumber_c, \
                              pointnumber_java_level1, pointnumber_postgresql_level1, pointnumber_java_level2, \
                              pointnumber_spring):
    rezult = None
    cursor = connection.cursor()
    str_command = "SELECT make_new_student_java(" \
                    + "'" + lastname + "', " \
                    + "'" + firstname + "', " \
                    + "'" + fathername + "', " \
                    + genderismale + ", " \
                    + age + ", " \
                    + pointnumber_osnovi + ", " \
                    + pointnumber_algoritmi + ", " \
                    + pointnumber_git + ", " \
                    + pointnumber_c + ", " \
                    + pointnumber_java_level1 + ", " \
                    + pointnumber_postgresql_level1 + ", " \
                    + pointnumber_java_level2 + ", " \
                    + pointnumber_spring \
                    + ");"
    cursor.execute (str_command)
    rezult = cursor.fetchall()
    cursor.close()
    return rezult

def create_New_Student_C_sharp (connection, lastname, firstname, fathername, genderismale, age, \
                              pointnumber_osnovi, pointnumber_algoritmi, pointnumber_git, pointnumber_c, \
                              pointnumber_c_sharp_level1, pointnumber_c_sharp_level2, pointnumber_postgresql_level1, \
                              pointnumber_c_sharp_level3, pointnumber_html5_css, pointnumber_c_sharp_level4, \
                                pointnumber_javascript_level1, pointnumber_javascript_level2):
    rezult = None
    cursor = connection.cursor()
    str_command = "SELECT make_new_student_c_sharp(" \
                    + "'" + lastname + "', " \
                    + "'" + firstname + "', " \
                    + "'" + fathername + "', " \
                    + genderismale + ", " \
                    + age + ", " \
                    + pointnumber_osnovi + ", " \
                    + pointnumber_algoritmi + ", " \
                    + pointnumber_git + ", " \
                    + pointnumber_c + ", " \
                    + pointnumber_c_sharp_level1 + ", " \
                    + pointnumber_c_sharp_level2 + ", " \
                    + pointnumber_postgresql_level1 + ", " \
                    + pointnumber_c_sharp_level3 + ", " \
                    + pointnumber_html5_css + ", " \
                    + pointnumber_c_sharp_level4 + ", " \
                    + pointnumber_javascript_level1 + ", " \
                    + pointnumber_javascript_level2 \
                    + ");"
    cursor.execute(str_command)
    rezult = cursor.fetchall()
    cursor.close()
    return rezult

def create_New_Student_Admin (connection, lastname, firstname, fathername, genderismale, age, \
                              pointnumber_osnovi, pointnumber_osnovi_setey, pointnumber_linux_level1, pointnumber_data_analiz, \
                              pointnumber_postgresql_level1, pointnumber_postgresql_level2, pointnumber_postgresql_level3, pointnumber_qpt):
    rezult = None
    cursor = connection.cursor()
    str_command = "SELECT make_new_student_admin(" \
                    + "'" + lastname + "', " \
                    + "'" + firstname + "', " \
                    + "'" + fathername + "', " \
                    + genderismale + ", " \
                    + age + ", " \
                    + pointnumber_osnovi + ", " \
                    + pointnumber_osnovi_setey + ", " \
                    + pointnumber_linux_level1 + ", " \
                    + pointnumber_data_analiz + ", " \
                    + pointnumber_postgresql_level1 + ", " \
                    + pointnumber_postgresql_level2 + ", " \
                    + pointnumber_postgresql_level3 + ", " \
                    + pointnumber_qpt \
                    + ");"
    cursor.execute (str_command)
    rezult = cursor.fetchall()
    cursor.close()
    return rezult

def create_New_Student_Ingener (connection, lastname, firstname, fathername, genderismale, age, \
                              pointnumber_osnovi, pointnumber_algoritmi, pointnumber_git, \
                              pointnumber_postgresql_level1, pointnumber_c_sharp_level1, pointnumber_c_sharp_level2, \
                              pointnumber_html_xml, pointnumber_c_sharp_level3, pointnumber_c_sharp_level4, pointnumber_java_level1, \
                              pointnumber_python_level1, pointnumber_oracle, pointnumber_c_plus_plus, pointnumber_html5_css_3, \
                                pointnumber_javascript_level1):
    rezult = None
    cursor = connection.cursor()
    str_command = "SELECT make_new_student_ingener(" \
                    + "'" + lastname + "', " \
                    + "'" + firstname + "', " \
                    + "'" + fathername + "', " \
                    + genderismale + ", " \
                    + age + ", " \
                    + pointnumber_osnovi + ", " \
                    + pointnumber_algoritmi + ", " \
                    + pointnumber_git + ", " \
                    + pointnumber_postgresql_level1 + ", " \
                    + pointnumber_c_sharp_level1 + ", " \
                    + pointnumber_c_sharp_level2 + ", " \
                    + pointnumber_html_xml + ", " \
                    + pointnumber_c_sharp_level3 + ", " \
                    + pointnumber_c_sharp_level4 + ", " \
                    + pointnumber_java_level1 + ", " \
                    + pointnumber_python_level1 + ", " \
                    + pointnumber_oracle + ", " \
                    + pointnumber_c_plus_plus + ", " \
                    + pointnumber_html5_css_3 + ", " \
                    + pointnumber_javascript_level1 \
                    + ");"
    cursor.execute (str_command)
    rezult = cursor.fetchall()
    cursor.close()
    return rezult

def delete_Student_Data(connection, st_id_str):
    rezult = None
    cursor = connection.cursor()
    '''
    str_command = "DELETE FROM public.student_subject " \
                  + "WHERE student_id = " + st_id_str + "; " \
                  + "DELETE FROM public.students " \
                  + "WHERE id = " + st_id_str + ";"
    '''
    str_command = "SELECT delete_student_by_id(" + st_id_str + ");"

    cursor.execute(str_command)
    cursor.close()
    return rezult