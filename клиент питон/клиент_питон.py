# coding=windows-1251

import socket

SERVER = "127.0.0.1"
PORT = 8080

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#�������� ������
client.connect((SERVER, PORT))#���������� ������� � �������
data = client.recv(1024)#����� ��� ��������� ������ �� ����������� ������ � ������ �� � ����
print(data.decode('utf-8'))

flag = False
help_msg = "\n������ ������"\
           "\nSTORE A B C - ��������� ������������"\
           "\nSOLVE WITH- ������ ��������� � ����� ��������������"\
           "\nSOLVE A B C - ������ ��������� � ��������� ��������������"\
           "\nHELP - �������� ������� � ��������"\
           "\nEXIT - �����\n"

while flag is False:
    flag = input()
    if flag == "EXIT":
        break
    if flag == "HELP":
        print(help_msg)

    client.send(flag.encode('utf-8'))
    d = client.recv(1024)
    d = d.decode('utf-8')
    print(d)

    if d == "�� ������������":
        print("\n" + help_msg)
        flag = True
    else:
        flag = False

if flag is True:
    while True:
        msg = input()
        if msg == "EXIT":
            print("�� ����� ������!")
            client.send(msg.encode('utf-8'))
            break
        if msg == "HELP":
            print(help_msg)
        else:
            client.send(msg.encode('utf-8'))
            result = client.recv(1024)
            print(result.decode('utf-8'))

client.close()