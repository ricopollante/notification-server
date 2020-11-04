import mysql.connector
import time
import requests
import threading
import socket
import time

# class TCPserver:
#     def __init__(self,ip):
#         self.ip = ip
#         self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
#         self.sock.bind((self.ip,5080))
#         self.sock.listen(10)
       
#         while True:
#             self.conn, self.addr = self.sock.accept()
#             print("SERVER STARTED")
#             print(self.conn, self.addr)
            
#             db_conn = mysql.connector.connect(
#             host="localhost",
#             user="admin",
#             password="iam100%pureROOT",
#             database="cnmdb"
#             )
#             mycursor = db_conn.cursor()
#             mycursor.execute("SELECT * from notifications")
#             result = mycursor.fetchall()
#             for result in result:
#                 print(result)
#                 try:
#                     self.conn.sendall(str(result[0]).encode())
#                     self.conn.close()
#                     time.sleep(1)
#                     query = str("DELETE from notifications where id=") + str(result[0])
#                     mycursor.execute(query)
#                     db_conn.commit()
#                 except Exception as error:
#                     print(error)

#             db_conn.close()

            

            
    
        

# TCPserver("127.0.0.1")

# def http(description):
#     data = {
#         'description' : description
#     }
#     http_req = requests.post("http://127.0.0.1:5091/add_client", data=data)



while True:
    db_conn = mysql.connector.connect(
    host="localhost",
    user="admin",
    password="iam100%pureROOT",
    database="cnmdb"
    )
    mycursor = db_conn.cursor()
    mycursor.execute("SELECT * from notifications")
    result = mycursor.fetchall()
    for result in result:
        print(result)
        try:
            #http(result[4])
            query = str("DELETE from notifications where id=") + str(result[0])
            mycursor.execute(query)
            db_conn.commit()
        except:
            pass

    db_conn.close()
