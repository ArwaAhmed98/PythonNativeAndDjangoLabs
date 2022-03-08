import re
import psycopg2
from psycopg2 import Error
def closeDBconn(cursor,connection):
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
class Person():
    def __int__(self,fullName,money,sleepMod,healthRate):
        self.fullName=fullName
        self.money=money
        self.sleepMod=sleepMod
        if (self.healthRate > 0 and self.healthRate <= 100):###########################################
            self.healthRate=healthRate
    def sleep(self,hours):
        if(hours==7):
            self.sleepMod="happy"
        elif(hours>7):
            self.sleepMod="lazy"
        else:
            self.sleepMod="tired"

    def eat(self,meals):
        if(meals==3):
            self.healthRate=100
        elif(meals==2):
            self.healthRate=75
        elif(meals==1):
            self.healthRate=50

    def buy(self,items):
        if(items==1):
            self.money=self.money-1



class Employee(Person):
    # def VerifyEmail(self,email):

    counter=0
    def __init__(self,id,healthRate,email,workmood,salary,is_manager):
        self.id=id
        patrn = r'^[a-z0-9]+[\._]?[ a-z0-9]+[@]\w+[. ]\w{2,3}$'
        result = re.match(patrn,email)
        if result:
            self.email = email
        else:

            raise ValueError("wrong format for email")
        self.workmood=workmood
        if (salary >= 1000):
            self.salary = salary
        self.is_manager=is_manager
        Employee.counter+=1
        if(healthRate not in range(1,100) ):
            raise ValueError("range value error ")
        self.healthRate=healthRate
    def work(self,hours):
        if(hours==8):
            self.workmood="happy"
        elif(hours>8):
            self.workmood="lazy"
        else:
            self.workmood="tired"


    def sendemail(self,to,subject,bodyReciever):
        if(self.VerifyEmail(to) and self.VerifyEmail(bodyReciever)):
            try:
                file=open("myemail.txt","w")
                file.write("this is my emiail")
            except IOError:
                print("cannot send email")
            else:
                print("email sent succ")
            finally:
                file.close()

    def insert(self,Emp):
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="office")
            cursor = connection.cursor()

            postgres_insert_query = """ INSERT INTO emp (id, healthRate, email , workmood , salary , is_manager) VALUES (%s,%s,%s,%s,%s,%s)"""
            record_to_insert = (Emp.id,Emp.healthRate, '%Emp.email', Emp.workmood,Emp.salary,Emp.is_manager)
            cursor.execute(postgres_insert_query, record_to_insert)

            connection.commit()
            count = cursor.rowcount
            print(count, "Record inserted successfully into office table")

        except (Exception, psycopg2.Error) as error:
            print("Failed to insert record into mobile table", error)
        finally:
            closeDBconn(cursor,connection)

    def delet(self,Emp):
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="office")

            cursor = connection.cursor()

            # Update single record now
            sql_delete_query = """Delete from emp where id = %s"""
            cursor.execute(sql_delete_query, (Emp.id,))
            connection.commit()
            count = cursor.rowcount
            print(count, "Record deleted successfully ")

        except (Exception, psycopg2.Error) as error:
            print("Error in Delete operation", error)
        finally:
            closeDBconn(cursor,connection)
    def print(self,empid):
        Myquery='SELECT * FROM emp where id={};'.format(empid)
        try:
            # Connect to an existing database
            connection = psycopg2.connect(user="postgres",
                                          password="",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="office")

            # Create a cursor to perform database operations
            cursor = connection.cursor()
            # Print PostgreSQL details
            print("PostgreSQL server information")
            print(connection.get_dsn_parameters(), "\n")
            # Executing a SQL query
            cursor.execute(Myquery)
            # Fetch result
            record = cursor.fetchall()
            print("OUTPUT of select is ", record, "\n")

        except (Exception, Error) as error:
            print("Error while connecting to PostgreSQL", error)
        # finally:
        #     if (connection):
        #         cursor.close()
        #         connection.close()
        #         print("PostgreSQL connection is closed")


class office(Employee):
    def __init__(self,name,emps):
        self.name=name
        self.emps=emps

    def getAllEmps(self):
        return Employee.counter #3dad el emps

    def getEmpID(self,Empid):
        Employee.print(Empid)

    def hire(self,Employee):
        Employee.insert(Employee)
    def fire(self,Employee):
        Employee.delet(Employee)

q=0
while(q==0):
    I=input("For add new emp press 'add' for exist press q")
    if(I=='q'):
        q==1
        quit()
    MGR=True
    NOR=True
    if(I=='add'):


        id = int(input("please enter the id to be hired "))
        name=input("please enter the name to be hired ")

        MGR=(input("IF you want the emp to be mngr press 'm'"))
        NOR=(input("IF you want the emp to be Normal press 'n'"))
        if(MGR=='m'):
            MGR=True
        else:
            MGR=False
        if(NOR=='n'):
            NOR=True
        else:
            NOR=False
        emp = Employee(id,90,'arwa@gmail.com',8,2000,MGR or NOR)
# emp.insert(emp)
        offic = office(emp,name)
# offic.hire(emp)
        offic.hire(emp)
# offic.print(3)