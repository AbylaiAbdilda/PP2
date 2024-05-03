import psycopg2
import csv

def check_number(phone):
    phone=str(phone)
    if phone[:2]=='87' or phone[:2]=='+7':
        return True
    else:
        return False

def limit(cursor):
    print('сколько пользователей вы хотите вывести')
    x=input()
    cursor.execute('create or replace function limit_(count_ int) RETURNS TABLE( 	name varchar, 	phone int  ) as $$ begin  return query select * from contacts limit count_; end $$ language plpgsql; ')
    cursor.execute('select * from limit_(%s)',(int(x),))
    records = cursor.fetchall()
    for i in records:
        print(i)

def multiadd(conn,cursor):
    cursor.execute('SELECT * FROM contacts')  
    records = cursor.fetchall()
    not_cor=[]
    with open('C:\\pp2\\11labtest\\sample.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for i in csv_reader:
            check=True
            for j in records:
                if i[1]== j[1]:
                    check=False
                    break
            if not check_number(i[0]):
                not_cor.append(i)
                check=False
            if check:
                cursor.execute('CREATE or replace FUNCTION new_acc(new_name varchar, new_phone integer) RETURNS void AS   $BODY$       BEGIN         INSERT INTO contacts(name,phone)         VALUES(new_name,new_phone);       END;  $BODY$   LANGUAGE "plpgsql" VOLATILE ')
                cursor.execute('select new_acc(%s,%s)',(i[0],i[1]))
                conn.commit()
            else:
                cursor.execute('create or replace procedure add_contacts(old_name varchar(255),new_number int ) language plpgsql as $$ begin   update contacts  set phone = new_number   where name=old_name;  end;$$;')
                cursor.execute('CALL add_contacts(%s,%s)',(i[0],i[1]))
                conn.commit()
                # postgres_insert_query = """ INSERT INTO contacts (user_id,last_name,first_name,phone_number) VALUES (%s,%s,%s,%s)"""
                # record_to_insert = (i[0], i[1], i[2], i[3])
                # cursor.execute(postgres_insert_query, record_to_insert)
                # conn.commit()
    if not_cor:
        print('неверные данные')
        print(not_cor)

    return True


def pattern(cursor):
    print('введите начало шаблона имени')
    y=input()
    cursor.execute('SELECT * FROM contacts')
    print('все совпадения')
    records=cursor.fetchall()
    for i in records:
        if i[1][:len(y)]==y:
            print(i)
    return True


def delete(conn,cursor):
    print('удаление по номеру 1, по имени 2')
    x=input()
    if x == '1':
        x=int(input())
        cursor.execute('create or replace procedure delete_(   old_name integer ) language plpgsql as $$ begin   delete from contacts  where phone=old_name; end;$$; ')
        cursor.execute('call delete_(%s)',(x,))
        conn.commit()
    else:
        x=input()
        cursor.execute('create or replace procedure delete_(   old_name varchar(255) ) language plpgsql as $$ begin   delete from contacts  where name=old_name; end;$$; ')
        cursor.execute('call delete_(%s)',(x,))
        conn.commit()
    print("Удаление произошло успешно")

def update(conn,cursor):
    print('Введите ID контакта которогo хотите обновить')
    x=int(input())

    print('что вы хотите обновить?')

    print('имя,фамилие,номер')
    y=input()

    print('введите на что хотите изменить')
    z=input()

    if y=='имя':
        sql_update_query = """Update contacts set first_name = %s where user_id = %s"""
        cursor.execute(sql_update_query, (z, x))
        conn.commit()

    elif y=='фамилия':
        sql_update_query = """Update contacts set last_name = %s where user_id = %s"""
        cursor.execute(sql_update_query, (z, x))
        conn.commit()

    else:
        sql_update_query = """Update contacts set phone_number = %s where user_id = %s"""
        cursor.execute(sql_update_query, (z, x))
        conn.commit()

    print('УСПЕШНО!')

def show(cursor):
    print('только номера')
    cursor.execute('create or replace function onlynumbers() RETURNS TABLE(	phone int ) as $$ begin  return query select contacts.phone from contacts; end $$ language plpgsql;  select *from onlynumbers();')
    show=cursor.fetchall()
    print(show)
    print('имя и номер')
    cursor.execute('create or replace function ALL_() RETURNS TABLE( 	name varchar, 	phone int ) as $$ begin  return query select * from contacts; end $$ language plpgsql;  select *from ALL_();')
    show=cursor.fetchall()
    print(show)

def add(conn,cursor):
    print('имя и номер пользователя')
    z=input().split()
    old_name=z[0]
    new_number=int(z[1])
    cursor.execute('select phone from contacts where name=%s',(old_name,))
    show=cursor.fetchall()
    if show:
        cursor.execute('create or replace procedure add_contacts(old_name varchar(255),new_number int ) language plpgsql as $$ begin   update contacts  set phone = new_number   where name=old_name;  end;$$;')
        cursor.execute('CALL add_contacts(%s,%s)',(old_name,new_number))
        conn.commit()
    else:
        cursor.execute('CREATE or replace FUNCTION new_acc(new_name varchar, new_phone integer) RETURNS void AS   $BODY$       BEGIN         INSERT INTO contacts(name,phone)         VALUES(new_name,new_phone);       END;  $BODY$   LANGUAGE "plpgsql" VOLATILE ')
        cursor.execute('select new_acc(%s,%s)',(old_name,new_number))
        conn.commit()

    print( "УСПЕШНО!")


conn = psycopg2.connect("dbname=postgres user=postgres password=1234")
cursor = conn.cursor()
while True:
    choose=input("Выберите что вы хотите сделать:\n1:Добавить контакт\n2:Удалить контакт\n3:Показать контакты\n4:Обновить контакт\n5:Шаблон\n6:mutliadd\n7:limit\n8:create table\n")
    if choose == '2':
        delete(conn,cursor)
    elif choose == '1':
        add(conn,cursor)
    elif choose=='3':
        show(cursor)
    elif choose=='4':
        update(conn,cursor)
    elif choose == '5':
        pattern(cursor)
    elif choose=='6':
        multiadd(conn,cursor)
    elif choose=='7':
        limit(cursor)
    elif choose=='exit':
        break

