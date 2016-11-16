import csv
import MySQLdb

mydb = MySQLdb.connect(host='128.199.91.4',
    user='veeresh',
    passwd='veer@123',
    db='kvn')

cursor = mydb.cursor()

insert_data = 'INSERT INTO calls_made(Name,Project_name,Language,Phone_num,Unique_id,Call_slot,Call_status,Drop_reason,Gestational,Call_Date_Time,Call_Duration,Organization) VALUES ("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")'


csv_data = csv.reader(file('fin_calls_made.csv'))
csv_data.next()
for row in csv_data:
    _Name = row[0]
    _Project_name = row[1]
    _Language = row[2]
    _Phone_num = row[3]
    _Unique_id = row[4]
    _Call_slot = row[5]
    _Call_status = row[6]
    _Drop_reason = row[7]
    _Gestational = row[8]
    _Call_Date_Time = row[9]
    _Call_Duration = row[10]
    _Organization = row[11]

    

    query = insert_data%(_Name,_Project_name,_Language,_Phone_num,_Unique_id,_Call_slot,_Call_status,_Drop_reason,_Gestational,_Call_Date_Time,_Call_Duration,_Organization)
    print query
    cursor.execute(query)


mydb.commit()
cursor.close()
print "Done"