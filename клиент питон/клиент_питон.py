# coding=windows-1251

import socket

SERVER = "127.0.0.1"
PORT = 8080

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#создание сокета
client.connect((SERVER, PORT))#подключаем клиента к серверу
data = client.recv(1024)#метод для получения байтов из клиентского сокета и записи их в файл
print(data.decode('utf-8'))

flag = False
help_msg = "\nСписок команд"\
           "\nSTORE A B C - запомнить коэффициенты"\
           "\nSOLVE WITH- решить уравнение с этими коэффициентами"\
           "\nSOLVE A B C - решить уравнение с заданными коэффициентами"\
           "\nHELP - получить справку о командах"\
           "\nEXIT - выход\n"

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

    if d == "Вы авторизованы":
        print("\n" + help_msg)
        flag = True
    else:
        flag = False

if flag is True:
    while True:
        msg = input()
        if msg == "EXIT":
            print("До новых встреч!")
            client.send(msg.encode('utf-8'))
            break
        if msg == "HELP":
            print(help_msg)
        else:
            client.send(msg.encode('utf-8'))
            result = client.recv(1024)
            print(result.decode('utf-8'))

client.close()