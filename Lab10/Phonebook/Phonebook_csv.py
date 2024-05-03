import psycopg2
from example_config.config import load_config  # Импорт функции load_config из указанного пути

conn = psycopg2.connect(
    host='localhost',
    dbname='phonebook',
    user='postgres',
    password='1234'
)


#курсор
cur = conn.cursor()

#Удаление чтобы как олень по 20 раз не удалять вручную
cur.execute('DROP TABLE phone_book')
# потвреждение удаления
conn.commit()

#table
cur.execute("""CREATE TABLE phone_book (
            name VARCHAR(255),
            phone_number VARCHAR(15) PRIMARY KEY
            
);
""")

conn.commit()


import csv

filename = '/Users/yerbolkobegen/Desktop/GitHub/PP2/Lab10/PhoneBook/phone.csv'

with open(filename, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        name, phone_number = row
           
            
            
            #чтобы было внутри цикла 
        # new students
        cur.execute(f"""INSERT INTO phone_book (name, phone_number) VALUES
                    ('{name}', '{phone_number}');
        """)

        conn.commit()
