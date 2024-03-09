import psycopg2

connect = psycopg2.connect(
    host='localhost',
    user='postgres',
    password='password',
    database='think_test_db',
)
cursor = connect.cursor()

def insert_data_into_niggers_info(name, surname, email, birthday, password):
    cursor.execute("INSERT INTO niggers_info (name, surname, email, birthday, password) VALUES (%s, %s, %s, %s, %s)",
                   (name, surname, email, birthday, password))
    connect.commit()

def update_data_into_niggers_info(id, name, surname, email, birthday, password):
    cursor.execute("UPDATE niggers_info SET name = %s, surname = %s, email = %s, birthday = %s, password = %s WHERE id = %s",
                   (name, surname, email, birthday, password, id))
    connect.commit()

def delete_data_into_niggers_info(id, name, surname, email, birthday, password):
    cursor.execute("DELETE niggers_info SET name = %s, surname = %s, email = %s, birthday = %s, password = %s WHERE id = %s",
                   (name, surname, email, birthday, password, id))
    connect.commit()

insert_data_into_niggers_info('Inchanka', 'Tida', 'dhnfujefjdfurfujvgujgfvnjrftjtifjfgnxj@gmail.com', '2024-09-03', 'lavTxa228@.comVarung999')
insert_data_into_niggers_info('Nissan', 'Tida', 'zsdffgvrgfvrstetfwerf@google.com@gmail.com', '2013-04-09', 'lavTxa228@.comVarung999')
insert_data_into_niggers_info('BMW', 'Tida', '094578545@gmail.com', '2022-10-22', 'lavTxa228@.comVarung999')
insert_data_into_niggers_info('Toyota', 'Tida', 'glglglglglglggllglglggllglglg@gmail.com', '2013-04-09', 'lavTxa228@.comVarung999')
insert_data_into_niggers_info('Barcelona', 'Tida', 'Vardan_Ghukasyan@gmail.com', '2013-04-09', 'lavTxa228@.comVarung999')
update_data_into_niggers_info(3, "jjj", "Tida", "dfrf@gmail.com", "2022-04-09", "dededfef")