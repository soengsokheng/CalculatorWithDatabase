import psycopg2
conn = psycopg2.connect(
        database = "postgres",
        user = "postgres",
        password = "heng",
        host = "localhost",
        port = "5432"
    )
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS casio (num1 INTEGER, oper VARCHAR, num2 INTEGER, result INTEGER)")
num1 = int(input("Enter num1: "))
oper = input("Enter operator: ")
num2 = int(input("Enter num2: "))

cur.execute("SELECT * FROM casio WHERE num1 = %s AND oper = %s AND num2 = %s",(num1,oper,num2))
row = cur.fetchone()

if row is None:
    cur.execute("INSERT INTO casio (num1,oper,num2,result) VALUES (%s,%s,%s,0)",(num1,oper,num2))
    conn.commit()
    row = (num1, oper, num2, 0)
    
result = row[3]

if (oper == "+"):
    result = num1+num2
elif (oper == "-"):
    result = num1-num2
elif (oper == "*"):
    result = num1*num2
elif (oper == "/"):
    result = num1/num2
else:
    print("Invalid Operator")
print(result)
cur.execute("UPDATE casio SET result = %s WHERE num1 = %s AND oper = %s AND num2 = %s", (result, num1, oper, num2))
conn.commit()
cur.close()
conn.close()
