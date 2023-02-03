# 服务端，用来回答问题的！

import socket
import sqlite3
import re

local_ip = ' 192.168.110.240'
local_port = 43200
tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_server.bind((local_ip, local_port))
tcp_server.listen(16)
print('Wait for connection')
current_client_socket, client_addr = tcp_server.accept()
print('Waiting for message')
print(client_addr)
match_word = ''

def ans_ques(ask):
    global match_word
    ask_lower = ask.lower()
    con = sqlite3.connect('ask_answer.db')
    cur = con.cursor()
    sql_1 = 'select ask from communicate'
    answer_all = cur.execute(sql_1)
    for i in answer_all:
        if re.match(ask_lower,i[0]) ==None:
            continue
        else:
            match_word = re.match(ask_lower+r'(.*)',i[0]).group()
            sql_2 = """select answer from communicate where ask = \"""" + match_word + """\";"""
            word = cur.execute(str(sql_2))
            print(re.match(ask_lower+r'(.*)',i[0]).group())
            con.commit()
            return word

def Server():

        while True:
            try:
                global match_word
                recv_data = current_client_socket.recv(1024)
                print('Receive from client:%s'%recv_data.decode('utf-8'))
                word = ([i for i in ans_ques(recv_data.decode('utf-8'))])
                if recv_data.decode('utf-8') =='bye':
                    current_client_socket.sendall('Welcom to ues it next time!'.encode('utf-8'))
                    tcp_server.close()
                    return
                current_client_socket.sendall(bytes(match_word.encode('utf-8')+word[0][0].encode('utf-8')))
            except:
                current_client_socket.sendall('error'.encode('utf-8'))
                print('您输入的值有误，请重新输入')

Server()