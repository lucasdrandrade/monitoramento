# issues:   § clear

import socket 
import json

host_name = socket.gethostname()
host_ip = "192.168.1.66"
#print(host_ip)
#HOST = socket.gethostname() 
HOST, PORT= host_ip , 8089

def escrita_json(data, path='C:/Users/ldg/Desktop/UFSC/EEL7802/monitoramento/projeto_monitoramento/dataBase/Themometric_mesures.json'):
    '''
    Função que faz a escrita do arquivo de temperatura.
    '''
    with open(path, 'w', encoding='utf-8') as outfile:
        outfile.write(data)

def get_Host_name_IP():
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        print("Hostname :  ",host_name)
        print("IP : ",host_ip)
    except:
        print("Unable to get Hostname and IP")

def server(HOST, PORT):
    print("[SERVER INFO] Aguardando conexão")

# ---------- CONEXAO SOCKET TCP ---------- #
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT)) 
    server_socket.listen(10) 

    # ACEITA A COMUNICAÇÂO
    (serverSocket, (address,port))= server_socket.accept() 
    print(f"\nConnection from {address} has been estabilished in {port}!\n")

    while True: 

    # ENVIA MENSAGEM AO CLIENTE
        msg_to_client = "Comunicação com o cliente iniciada"
        serverSocket.send(bytes(msg_to_client, "utf-8"))

    # RECEBE E DECODIFICA MENSAGEM DO CLIENTE
        msg_from_client = serverSocket.recv(1024)
        msg_from_client = msg_from_client.decode('utf-8')

        print("\nReceived from the Client: {}\n".format(msg_from_client))
        print("\nSent to the Client:     {}\n".format(msg_to_client))

        escrita_json(data=msg_from_client)
    serverSocket.close()


server(HOST, PORT) 