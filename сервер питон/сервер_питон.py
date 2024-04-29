# coding=windows-1251

import mimetypes
import os
import socket
from time import ctime
import shutil
import math

SERVER = "127.0.0.1"
PORT = 8080

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((SERVER, PORT))
server.listen(10)
print("����� ���������� �� ������!")
print("��� ������ �� �������...")
#clientConnection, address = server.accept()
#clientConnection.send("You are connected".encode("utf-8"))


def err(num):
    if num == 1:
        clientConnection.send("������ �����������".encode("utf-8"))
    elif num == 2:
        clientConnection.send("������������� ������".encode("utf-8"))
    elif num == 3:
        clientConnection.send("�� ������� ������������.".encode("utf-8"))

def login(user, password):                              #������� ��� �������� ������ � ������
    with open('passwords.txt', encoding='utf-8') as file:
        list_users = file.read().splitlines()
    file.close()
    for i in list_users:
        u = i.split(' ')[0]
        p = i.split(' ')[1]
        if (str(u) == str(user)) & (str(p) == str(password)):
            return True
    return False

def kvadrat(a, b, c):
    D = (b ** 2) - (4 * a * c)
    if D > 0:
        if a != 0:
            x1 = (-b + math.sqrt(D)) / (2 * a)
            x2 = (-b - math.sqrt(D)) / (2 * a)
            str1 = str(x1) 
            str2 = str(x2)
            kvadr = str1 + " " + str2
        else:
            kvadr = "��� �� ���������� ���������."
    elif D == 0:
        x = -b / (2 * a)
        kvadr = str(x)
    else:
        kvadr = "������ ���"
    return kvadr

LOGIN = False
dir = os.path.abspath(os.curdir)
user = ""
a_store = b_store = c_store = -100
while True:
    while LOGIN is False:
        clientConnection, address = server.accept()
        print("����������� ������:" ,address)
        clientConnection.send("�� ����������.\n��� ����������� ������ ���������������."
                              "\n�������: LOGIN user pass - ����� LOGIN �������� ��� ����� � ������".encode("utf-8"))
        log = clientConnection.recv(1024)
        log = log.decode("utf-8")
        data = log.split(' ')[0]                                    #���������� ���� ������ �����, �� ���� LOGIN
        try:
            if data == "LOGIN":
                user = log.split(' ')[1]                            #�����
                password = log.split(' ')[2]                        #������
                LOGIN = login(user, password)                        #��������� �� ������� � ���� ������ ������ � ������
                if LOGIN is False:
                    err(1)
                else:
                    LOGIN = True
                    clientConnection.send("�� ������������".encode("utf-8"))
                    print("������������ " + str(user) + " �������������.")
            else:
                err(1)
        except BaseException:
            err(1)

    while LOGIN is True:
        s = clientConnection.recv(1024)
        s = s.decode("utf-8")
        data = s.split(' ')[0]
        try:
            if data == "STORE":                     #���������� ������������
                a_store = (int)(s.split(' ')[1])
                b_store = (int)(s.split(' ')[2])
                c_store = (int)( s.split(' ')[3])
                result = "������������ ��������."
                clientConnection.send(result.encode("utf-8"))
            elif data == "SOLVE" and s.split(' ')[1] == "WITH":
                if(not(a_store == -100 and b_store == -100 and c_store == -100)):
                    result = kvadrat(a_store, b_store, c_store)
                    clientConnection.send(result.encode("utf-8"))
                else:
                    err(3)
            elif data == "SOLVE":
                a = s.split(' ')[1]
                b = s.split(' ')[2]
                c = s.split(' ')[3]
                if (a.isdigit() and b.isdigit() and c.isdigit()):
                    a = (int)(s.split(' ')[1])
                    b = (int)(s.split(' ')[2])
                    c= (int)( s.split(' ')[3])
                    result = kvadrat(a, b, c)
                    clientConnection.send(result.encode("utf-8"))
            else:
                err(2)
        except BaseException:
            err(2)
        if s == "EXIT":
            print("������ " + str(user) + " ����������")
            clientConnection.close()
            LOGIN = False
            
