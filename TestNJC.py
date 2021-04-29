import pyodbc 
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=JUPITER2;'
                      'Database=EmployeeDet;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute("Insert into EmployeeData values('emp7','Gangadhar',31,20000,'Siddapura',9737648970)")
cursor.execute('SELECT * FROM EmployeeData')

for row in cursor:
    print(row)



