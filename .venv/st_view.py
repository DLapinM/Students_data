import psycopg2
import st_model
import st_controller
import tabulate

def input_Connection_Data():
    print("Запущена процедура ввода данных для подключения к базе данных.")
    print("Введите имя пользователя: ")
    username = input()
    print("Введите пароль: ")
    password = input()
    print("Введите имя базы данных: ")
    db_name = input()
    print("Введите хост: ")
    host = input()
    flag = True
    port_str = None
    port = 0
    while flag == True:
        print("Введите порт: ")
        port_str = input()
        try:
            port = int(port_str)
            flag = False
        except:
            print("Ошибка ввода данных порта. Должно быть введено целое число.")
    return (username, password, db_name, host, port)

def connect_To_Db(connect_data):
    connection_rezult = st_model.st_Db_Connect(connect_data[0], connect_data[1], connect_data[2], connect_data[3], connect_data[4])
    connection_flag = connection_rezult[0]
    connection = connection_rezult[1]
    if connection_flag:
        print("Подключение к базе данных выполнено.")
    else:
        print("Ошибка подключения к базе данных.")
    return (connection_flag, connection)

def disconnect_From_Db(connection_rezult):
    connection_flag = connection_rezult[0]
    connection = connection_rezult[1]
    disconnection_flag = st_model.st_Db_Disconnect(connection_flag, connection)
    if disconnection_flag:
        print("Отключение от базы данных выполнено.")
    else:
        print("Ощибка отключения от базы данных.")

def print_Strings(output_rezult):
    for el in output_rezult:
        print(el)

def print_Info(output_rezult):
    rezult = tabulate.tabulate(output_rezult)
    print(rezult)

def input_Specialisation_Number():
    rezult = None
    flag1 = True
    while flag1 == True:
        print("Вам необходимо ввести номер специализации.")
        print("0 - Python-разработчик")
        print("1 - Java-разработчик")
        print("2 - .Net-разработчик на языке C#")
        print("3 - Администратор PostgreSQL")
        print("4 - Инженер-программист")
        print("Введите номер специализации: ")
        sp_num_str = input()
        if (sp_num_str == "0") or (sp_num_str == "1") or (sp_num_str == "2") or (sp_num_str == "3") or (sp_num_str == "4"):
            print("Ввод данных принят.")
            if sp_num_str == "0":
                print('Выбрана специализация "Python-разработчик":')
            elif sp_num_str == "1":
                print('Выбрана специализация "Java-разработчик":')
            elif sp_num_str == "2":
                print('Выбрана специализация ".Net-разработчик на языке C#":')
            elif sp_num_str == "3":
                print('Выбрана специализация "Администратор PostgreSQL":')
            elif sp_num_str == "4":
                print('Выбрана специализация "Инженер-программист":')
            flag1 = False
            rezult = sp_num_str
        else:
            print("Ошибка ввода данных. Вы должны указать целое число от 0 до 4.")
    return rezult

def input_Age():
    st_age_str = None
    flag1 = True
    while flag1 == True:
        print("Введите возраст студента: ")
        st_age_str = input()
        try:
            st_age = int(st_age_str)
            if ((st_age >= 14) and (st_age <= 120)):
                st_age_str = str(st_age)
                flag1 = False
            else:
                flag1 = True
        except:
            flag1 = True
        if flag1 == False:
            print("Ввод данных принят.")
        else:
            print("Ошибка ввода данных. Вы должны указать целое число от 14 до 120.")
    return st_age_str

def input_Gender():
    gender_str = None
    flag1 = True
    while flag1 == True:
        print("Укажите пол студента (1 - мужской, 0 - женский): ")
        gender_str_first = input()
        if (gender_str_first == "0") or (gender_str_first == "1"):
            if gender_str_first == "0":
                gender_str = "FALSE"
            else:
                gender_str = "TRUE"
            flag1 = False
            print("Ввод данных принят.")
        else:
            flag1 = True
            print("Ошибка ввода данных. Вы должны указать целое число от 0 до 1.")
    return gender_str

def input_Point(name_of_subject):
    point_str = None
    flag1 = True
    while flag1 == True:
        print('Введите оценку студента по предмету "' + name_of_subject + '": ')
        point_str_first = input()
        if (point_str_first == "2") or (point_str_first == "3") or (point_str_first == "4") or (point_str_first == "5"):
            point_str = point_str_first
            flag1 = False
            print("Ввод данных принят.")
        else:
            flag1 = True
            print("Ошибка ввода данных. Вы должны указать целое число от 2 до 5.")
    return point_str

def input_Student_ID():
    flag1 = True
    st_id_str = None
    while (flag1 == True):
        print("Введите ID студента для удаления записей о нём: ")
        st_id_str = input()
        try:
            st_id = int(st_id_str)
            st_id_str = str(st_id)
            flag1 = False
        except:
            print("Ошибка. Необходимо ввести целое число.")
            flag1 = True
    return st_id_str

def delete_All_Data_About_Student(connection_rezult):
    flag = False
    print("")
    print("Запущена процедура удаления всех данных о студенте по его ID.")
    st_id_str = input_Student_ID()
    try:
        flag = st_controller.deleteStudentData(connection_rezult[0], connection_rezult[1], st_id_str)
    except:
        flag = False
    if flag == True:
        print("Процедура удаления данных о студенте успешно завершена")
    else:
        print("Ошибка. Данные о студенте не удалены.")
    return flag

def output_Students_By_specialization(connection_rezult):
    print("")
    print("Запущена процедура вывода информации о студентах и их оценках по предметам в зависимости от специализации.")
    sp_num_str = input_Specialisation_Number()
    print("")
    if sp_num_str == "0":
        print('Вывод информации о студентах и их оценках по специализации "Python-разработчик":')
    elif sp_num_str == "1":
        print('Вывод информации о студентах и их оценках по специализации "Java-разработчик":')
    elif sp_num_str == "2":
        print('Вывод информации о студентах и их оценках по специализации ".Net-разработчик на языке C#":')
    elif sp_num_str == "3":
        print('Вывод информации о студентах и их оценках по специализации "Администратор PostgreSQL":')
    elif sp_num_str == "4":
        print('Вывод информации о студентах и их оценках по специализации "Инженер-программист":')
    students_info = st_controller.get_Students_By_Specialization(connection_rezult[0], connection_rezult[1], sp_num_str)
    print_Info(students_info)
    return students_info

def output_Students_Personal_Data_By_Specialization(connection_rezult):
    print("")
    print("Запущена процедура вывода личных данных студентов в зависимости от их специализации.")
    sp_num_str = input_Specialisation_Number()
    print("")
    if sp_num_str == "0":
        print('Вывод личных данных студентов по специализации "Python-разработчик":')
    elif sp_num_str == "1":
        print('Вывод личных данных студентов по специализации "Java-разработчик":')
    elif sp_num_str == "2":
        print('Вывод личных данных студентов по специализации ".Net-разработчик на языке C#":')
    elif sp_num_str == "3":
        print('Вывод личных данных студентов по специализации "Администратор PostgreSQL":')
    elif sp_num_str == "4":
        print('Вывод личных данных студентов по специализации "Инженер-программист":')
    students_info = st_controller.get_Students_Personal_Data_By_Specialization_Number(connection_rezult[0], connection_rezult[1], sp_num_str)
    print_Info(students_info)
    return students_info

def output_Subjects_by_specialization_number(connection_rezult):
    print("")
    print("Запущена процедура вывода названий предметов в зависимости от их принадлежности к определённой специализации.")
    sp_num_str = input_Specialisation_Number()
    print("")
    if sp_num_str == "0":
        print('Вывод названий предметов, относящихся к специальности "Python-разработчик":')
    elif sp_num_str == "1":
        print('Вывод названий предметов, относящихся к специальности "Java-разработчик":')
    elif sp_num_str == "2":
        print('Вывод названий предметов, относящихся к специальности ".Net-разработчик на языке C#":')
    elif sp_num_str == "3":
        print('Вывод названий предметов, относящихся к специальности "Администратор PostgreSQL":')
    elif sp_num_str == "4":
        print('Вывод названий предметов, относящихся к специальности "Инженер-программист":')
    subjects_info = st_controller.get_Subjects_by_specialization_number(connection_rezult[0], connection_rezult[1], sp_num_str)
    print_Info(subjects_info)
    return subjects_info

def output_Students_data_by_FIO_and_specialization_number(connection_rezult):
    print("")
    print("Запущена процедура вывода информации о студентах и их оценках по предметам в зависимости от Ф.И.О. и специализации.")
    print("Введите фамилию студента: ")
    last_name = input()
    last_name = st_controller.get_NameString_From_String(last_name)
    print("Введите имя студента: ")
    first_name = input()
    first_name = st_controller.get_NameString_From_String(first_name)
    print("Введите отчество студента: ")
    father_name = input()
    father_name = st_controller.get_NameString_From_String(father_name)
    sp_num_str = input_Specialisation_Number()
    print("")
    if sp_num_str == "0":
        print('Вывод информации о студентах и их оценках по Ф.И.О. "' + last_name + ' ' + first_name + ' ' + father_name + '" и специализации "Python-разработчик":')
    elif sp_num_str == "1":
        print('Вывод информации о студентах и их оценках по Ф.И.О. "' + last_name + ' ' + first_name + ' ' + father_name + '" и специализации "Java-разработчик":')
    elif sp_num_str == "2":
        print('Вывод информации о студентах и их оценках по Ф.И.О. "' + last_name + ' ' + first_name + ' ' + father_name + '" и специализации ".Net-разработчик на языке C#":')
    elif sp_num_str == "3":
        print('Вывод информации о студентах и их оценках по Ф.И.О. "' + last_name + ' ' + first_name + ' ' + father_name + '" и специализации "Администратор PostgreSQL":')
    elif sp_num_str == "4":
        print('Вывод информации о студентах и их оценках по Ф.И.О. "' + last_name + ' ' + first_name + ' ' + father_name + '" и специализации "Инженер-программист":')

    students_info = st_controller.get_Students_data_by_FIO_and_specialization_number(connection_rezult[0], connection_rezult[1], last_name, first_name, father_name, sp_num_str)
    print_Info(students_info)
    return students_info

def output_all_specializations(connection_rezult):
    print("")
    print("Запущена процедура вывода информации о всех специализациях по которым ведётся обучение.")
    specializations_info = st_controller.get_All_Specialization(connection_rezult[0], connection_rezult[1])
    print_Info(specializations_info)
    return specializations_info

def input_Student_Python_Data(connection_rezult):
    rez_f = False
    print("Введите фамилию студента: ")
    lastname = input()
    lastname = st_controller.get_NameString_From_String(lastname)
    print("Введите имя студента: ")
    firstname = input()
    firstname = st_controller.get_NameString_From_String(firstname)
    print("Введите отчество студента: ")
    fathername = input()
    fathername = st_controller.get_NameString_From_String(fathername)
    genderismale = input_Gender()
    age = input_Age()
    pointnumber_osnovi = input_Point("Основы программирования и БД")
    pointnumber_algoritmi = input_Point("Алгоритмы")
    pointnumber_git = input_Point("Git")
    pointnumber_html5_css = input_Point("HTML 5 и CSS 3")
    pointnumber_python_level1 = input_Point("Python (уровень 1)")
    pointnumber_postgresql_level1 = input_Point("PostgreSQL (уровень 1)")
    pointnumber_python_level2 = input_Point("Python (уровень 2)")
    pointnumber_python_level3 = input_Point("Python (уровень 3)")

    rez_f = st_controller.make_NewStudentPython (connection_rezult[0], connection_rezult[1], lastname, firstname, fathername, genderismale, age, \
                              pointnumber_osnovi, pointnumber_algoritmi, pointnumber_git, pointnumber_html5_css, \
                              pointnumber_python_level1, pointnumber_postgresql_level1, pointnumber_python_level2, \
                              pointnumber_python_level3)
    return rez_f

def input_Student_Java_Data(connection_rezult):
    rez_f = False
    print("Введите фамилию студента: ")
    lastname = input()
    lastname = st_controller.get_NameString_From_String(lastname)
    print("Введите имя студента: ")
    firstname = input()
    firstname = st_controller.get_NameString_From_String(firstname)
    print("Введите отчество студента: ")
    fathername = input()
    fathername = st_controller.get_NameString_From_String(fathername)
    genderismale = input_Gender()
    age = input_Age()
    pointnumber_osnovi = input_Point("Основы программирования и БД")
    pointnumber_algoritmi = input_Point("Алгоритмы")
    pointnumber_git = input_Point("Git")
    pointnumber_c = input_Point("C")
    pointnumber_java_level1 = input_Point("Java (уровень 1)")
    pointnumber_postgresql_level1 = input_Point("PostgreSQL (уровень 1)")
    pointnumber_java_level2 = input_Point("Java (уровень 2)")
    pointnumber_spring = input_Point("Spring")

    rez_f = st_controller.make_NewStudentJava (connection_rezult[0], connection_rezult[1], lastname, firstname, fathername, genderismale, age, \
                                               pointnumber_osnovi, pointnumber_algoritmi, pointnumber_git, pointnumber_c, \
                                               pointnumber_java_level1, pointnumber_postgresql_level1, pointnumber_java_level2, \
                                               pointnumber_spring)
    return rez_f

def input_Student_CSharp_Data(connection_rezult):
    rez_f = False
    print("Введите фамилию студента: ")
    lastname = input()
    lastname = st_controller.get_NameString_From_String(lastname)
    print("Введите имя студента: ")
    firstname = input()
    firstname = st_controller.get_NameString_From_String(firstname)
    print("Введите отчество студента: ")
    fathername = input()
    fathername = st_controller.get_NameString_From_String(fathername)
    genderismale = input_Gender()
    age = input_Age()
    pointnumber_osnovi = input_Point("Основы программирования и БД")
    pointnumber_algoritmi = input_Point("Алгоритмы")
    pointnumber_git = input_Point("Git")
    pointnumber_c = input_Point("C")
    pointnumber_c_sharp_level1 = input_Point("C# (уровень 1)")
    pointnumber_c_sharp_level2 = input_Point("C# (уровень 2)")
    pointnumber_postgresql_level1 = input_Point("PostgreSQL (уровень 1)")
    pointnumber_c_sharp_level3 = input_Point("C# (уровень 3)")
    pointnumber_html5_css = input_Point("HTML 5 и CSS 3")
    pointnumber_c_sharp_level4 = input_Point("C# (уровень 4)")
    pointnumber_javascript_level1 = input_Point("JavaScript (уровень 1)")
    pointnumber_javascript_level2 = input_Point("JavaScript (уровень 2)")

    rez_f = st_controller.make_NewStudentCSharp (connection_rezult[0], connection_rezult[1], lastname, firstname, fathername, genderismale, age, \
                                                 pointnumber_osnovi, pointnumber_algoritmi, pointnumber_git, pointnumber_c, \
                                                 pointnumber_c_sharp_level1, pointnumber_c_sharp_level2, pointnumber_postgresql_level1, \
                                                 pointnumber_c_sharp_level3, pointnumber_html5_css, pointnumber_c_sharp_level4, \
                                                 pointnumber_javascript_level1, pointnumber_javascript_level2)
    return rez_f

def input_Student_Admin(connection_rezult):
    rez_f = False
    print("Введите фамилию студента: ")
    lastname = input()
    lastname = st_controller.get_NameString_From_String(lastname)
    print("Введите имя студента: ")
    firstname = input()
    firstname = st_controller.get_NameString_From_String(firstname)
    print("Введите отчество студента: ")
    fathername = input()
    fathername = st_controller.get_NameString_From_String(fathername)
    genderismale = input_Gender()
    age = input_Age()
    pointnumber_osnovi = input_Point("Основы программирования и БД")
    pointnumber_osnovi_setey = input_Point("Основы сетей")
    pointnumber_linux_level1 = input_Point("Linux (уровень 1)")
    pointnumber_data_analiz = input_Point("Анализ данных на SQL")
    pointnumber_postgresql_level1 = input_Point("PostgreSQL (уровень 1)")
    pointnumber_postgresql_level2 = input_Point("PostgreSQL (уровень 2)")
    pointnumber_postgresql_level3 = input_Point("PostgreSQL (уровень 3)")
    pointnumber_qpt = input_Point("QPT - PostgreSQL")

    rez_f = st_controller.make_NewStudentAdmin (connection_rezult[0], connection_rezult[1], lastname, firstname, fathername, genderismale, age, \
                                                pointnumber_osnovi, pointnumber_osnovi_setey, pointnumber_linux_level1, pointnumber_data_analiz, \
                                                pointnumber_postgresql_level1, pointnumber_postgresql_level2, pointnumber_postgresql_level3, pointnumber_qpt)
    return rez_f

def input_Student_Ingener(connection_rezult):
    rez_f = False
    print("Введите фамилию студента: ")
    lastname = input()
    lastname = st_controller.get_NameString_From_String(lastname)
    print("Введите имя студента: ")
    firstname = input()
    firstname = st_controller.get_NameString_From_String(firstname)
    print("Введите отчество студента: ")
    fathername = input()
    fathername = st_controller.get_NameString_From_String(fathername)
    genderismale = input_Gender()
    age = input_Age()
    pointnumber_osnovi = input_Point("Основы программирования и БД")
    pointnumber_algoritmi = input_Point("Алгоритмы")
    pointnumber_git = input_Point("Git")
    pointnumber_postgresql_level1 = input_Point("PostgreSQL (уровень 1)")
    pointnumber_c_sharp_level1 = input_Point("C# (уровень 1)")
    pointnumber_c_sharp_level2 = input_Point("C# (уровень 2)")
    pointnumber_html_xml = input_Point("HTML и XML")
    pointnumber_c_sharp_level3 = input_Point("C# (уровень 3)")
    pointnumber_c_sharp_level4 = input_Point("C# (уровень 4)")
    pointnumber_java_level1 = input_Point("Java (уровень 1)")
    pointnumber_python_level1 = input_Point("Python (уровень 1)")
    pointnumber_oracle = input_Point("Oracle")
    pointnumber_c_plus_plus = input_Point("C++")
    pointnumber_html5_css_3 = input_Point("HTML 5 и CSS 3")
    pointnumber_javascript_level1 = input_Point("JavaScript (уровень 1)")

    rez_f = st_controller.make_NewStudentIngener (connection_rezult[0], connection_rezult[1], lastname, firstname, fathername, genderismale, age, \
                                                      pointnumber_osnovi, pointnumber_algoritmi, pointnumber_git, \
                                                      pointnumber_postgresql_level1, pointnumber_c_sharp_level1, pointnumber_c_sharp_level2, \
                                                      pointnumber_html_xml, pointnumber_c_sharp_level3, pointnumber_c_sharp_level4, pointnumber_java_level1, \
                                                      pointnumber_python_level1, pointnumber_oracle, pointnumber_c_plus_plus, pointnumber_html5_css_3, \
                                                      pointnumber_javascript_level1)
    return rez_f

def input_Student_Data(connection_rezult):
    rez_f = False
    print("")
    print("Запущена процедура добавления сведений о новом студенте в базу данных.")
    print("Укажите специализацию, по которой обучается студент.")

    st_specialization = input_Specialisation_Number()
    try:
        if st_specialization == "0":
            rez_f = input_Student_Python_Data(connection_rezult)
        elif st_specialization == "1":
            rez_f = input_Student_Java_Data(connection_rezult)
        elif st_specialization == "2":
            rez_f = input_Student_CSharp_Data(connection_rezult)
        elif st_specialization == "3":
            rez_f = input_Student_Admin(connection_rezult)
        elif st_specialization == "4":
            rez_f = input_Student_Ingener(connection_rezult)
        else:
            rez_f = False
    except Exception as e:
        print(e)
        rez_f = False
    if rez_f:
        print("Сведения о студенте успешно добавлены в базу данных.")
    else:
        print("Ошибка. Сведения о студенте не добавлены в базу данных.")
    return rez_f



def main_Db_Menu(connection_rezult):
    flag0 = True
    while flag0 == True:
        print("")
        print('Вы находитесь в главном меню управления базой данных "students".')
        flag = True
        while flag == True:
            print("Выберите нужный пункт меню.")
            print("0 - Вывод на экран списка названий всех специализаций по которым ведётся обучение.")
            print("1 - Вывод на экран Ф.И.О. всех студентов одной определённой специализации, а также их оценок по всем предметам данной специализации.")
            print("2 - Вывод на экран студентов и их оценок, которые обучаются на определённой специализации и имеют определённое Ф.И.О.")
            print("3 - Вывести на экран личные данные (кроме оценок) всех студентов определённой специализации.")
            print("4 - Вывести на экран список всех предметов определённой специализации.")
            print("5 - Добавить в базу данных сведения о новом студенте.")
            print("6 - Удалить данные студента, о котором уже имеются сведения в базе данных.")
            print("7 - Выход")
            menu_number = input()
            if (menu_number == "0") or (menu_number == "1") or (menu_number == "2") or (menu_number == "3") \
                    or (menu_number == "4") or (menu_number == "5") or (menu_number == "6") or (menu_number == "7"):
                print("Ввод данных принят.")
                if menu_number == "0":
                    print('Выбран пункт меню "0 - Вывод на экран списка названий всех специализаций по которым ведётся обучение."')
                    info_0 = output_all_specializations(connection_rezult)
                    pass
                elif menu_number == "1":
                    print('Выбран пункт меню "1 - Вывод на экран Ф.И.О. всех студентов одной определённой специализации, а также их оценок по всем предметам данной специализации."')
                    info_1 = output_Students_By_specialization(connection_rezult)
                    pass
                elif menu_number == "2":
                    print('Выбран пункт меню "2 - Вывод на экран студентов и их оценок, которые обучаются на определённой специализации и имеют определённое Ф.И.О."')
                    info_2 = output_Students_data_by_FIO_and_specialization_number(connection_rezult)
                    pass
                elif menu_number == "3":
                    print('Выбран пункт меню "3 - Вывести на экран личные данные (кроме оценок) всех студентов определённой специализации."')
                    info_3 = output_Students_Personal_Data_By_Specialization(connection_rezult)
                    pass
                elif menu_number == "4":
                    print('Выбран пункт меню "4 - Вывести на экран список всех предметов определённой специализации."')
                    info_4 = output_Subjects_by_specialization_number(connection_rezult)
                    pass
                elif menu_number == "5":
                    print('Выбран пункт меню "5 - Добавить в базу данных сведения о новом студенте."')
                    info_5 = input_Student_Data(connection_rezult)
                    pass
                elif menu_number == "6":
                    print('Выбран пункт меню "6 - Удалить все записи о студенте."')
                    info_6 = delete_All_Data_About_Student(connection_rezult)
                    pass
                elif menu_number == "7":
                    print('Выбран пункт меню "7 - Выход"')
                    flag0 = False
                    pass
                flag = False
            else:
                print("Ошибка ввода данных. Вы должны указать целое число от 0 до 7.")
        pass


connect_data = input_Connection_Data()
connection_rezult = connect_To_Db(connect_data)

if connection_rezult[0]:
    main_Db_Menu(connection_rezult)
    disconnect_From_Db(connection_rezult)