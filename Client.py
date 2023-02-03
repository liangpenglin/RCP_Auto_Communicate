# 客户端，用来问问题的！
import socket

local_ip = ' 192.168.110.240'
local_port = 43200

def Client():
    tcp_client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    tcp_client.connect((local_ip,local_port))
    while True:
        word = input('enter:')
        word_new = word.encode('utf-8')
        if word_new == 'bye':
            tcp_client.close()
            break
        else:
            tcp_client.send(word_new)
        recv_data = tcp_client.recv(1024)
        if recv_data =='error':
            print('Error!Please input others!')
        print('Receive from client:%s' % recv_data.decode('utf-8'))


if __name__ == '__main__':
    Client()
