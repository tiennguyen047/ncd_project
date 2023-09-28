import psycopg2

conn = psycopg2.connect(database="test_db",
                        host="127.0.0.1",
                        user="postgres",
                        password="nqt123",
                        port="5432")

conn.autocommit = True
cursor = conn.cursor()

sql = '''CREATE TABLE vnstock(employee_id int NOT NULL,\
employee_name char(20),\
employee_email varchar(30), employee_salary float);'''

cursor.execute(sql)
conn.commit()
conn.close()

postgres_create_table = '''CREATE TABLE {}(exchange char(20) NOT NULL,\
                                    price float,\
                                    industryID varchar(30),\
                                    industry varchar(30),\
                                    industryEn varchar(30),\
                                    establishedYear varchar(30),\
                                    noEmployees varchar(30),\
                                    noShareholders varchar(30),\
                                    foreignPercent varchar(30),\
                                    website varchar(30),\
                                    stockRating varchar(30),\
                                    deltaInWeek varchar(30),\
                                    deltaInMonth varchar(30),\
                                    deltaInYear varchar(30),\
                                    outstandingShare varchar(30),\
                                    issueShare varchar(30),\
                                    companyType varchar(30),\
                                    ticker varchar(30),\
                                    industryID varchar(30),\
                                    industryIDv2 float);'''