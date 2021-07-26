import datetime
import mysql.connector
from plyer import notification
conn=mysql.connector.connect(host='localhost',user='root',password='mahi',database='practice')
my_cursor=conn.cursor()
dt=datetime.datetime.now()
def notice (a) :
    notification.notify(
 			title = "**your reminder**",
 			message =a,
 			timeout= 10
 			)
while(1) :
    x=int(input("if you want to add messege enter 1 else enter 0"))
    if x==1:
        mes=input("write reminder")
        d=int(input('enter date'))
        m=int(input('enter month'))
        y=int(input('enter year'))
        h=int(input('enter hour'))
        mi=int(input('enter minute'))
        da=datetime.datetime(y,m,d,h,mi)
        query="insert into project(note,crux) values(%s,%s)"
        values=(mes,da)
        my_cursor.execute(query,values)
        x=0
    else :
        query="select * from project"
        my_cursor.execute(query)
        for a,b in my_cursor :
            if(dt==b) :
                notice(a)
         







    


