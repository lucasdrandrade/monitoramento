# issues:   § clear 
import logging
import time, threading
import socket
import json

json_file = r'/home/pi/projetos/monitoramento/projeto_monitoramento/dataBase/themometric_mesures.json' 

def leitura_json(file):
    '''
    Função que faz a leitura do arquivo de resultados.
    '''
    with open(file, encoding='utf-8') as fh:
        arquivo = json.load(fh)
    logging.info('arquivo carregado')
    return arquivo


def enviar_arquivo_socket(file, server_socket):

    #bytes_Data = str(file).encode('utf-8')
    bytes_Data = json.dumps(file, ensure_ascii=False).encode('utf-8')
    byte_size = len(bytes_Data)
    print(byte_size)
    numStr = str(byte_size)
    
    numStrFill = numStr.zfill(7)
    print(numStrFill)
    logging.debug(numStrFill)
    server_socket.send((str(numStrFill)+"\r\n\r\n\r\nTermoDrone").encode('utf-8'))

    logging.debug(f"[SOCKET SEND] {byte_size}")

    # REVISAR
    #string_to_send = json.dumps(file, ensure_ascii=False)
    print(type(bytes_Data))
    #print(str(string_to_send))

    server_socket.send(bytes_Data)#.encode('utf-8')

def client(HOST, PORT):
    
    # ---------- heartbeat message ---------- #
    mensagem = "cliente_TESTE"

# ---------- CONEXAO SOCKET TCP ---------- #
#--------------- build do objeto socket ---------------# 
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.connect((HOST, PORT))

    while True: 
        try:
        #---Receive data from the server ---------------# 
            received = conn.recv(1024)
            received = received.decode("utf-8")
            print("\nReceived from the Server: {}\n".format(received))

        #--- sending conf file to the server ---------------# 

            conn.sendall(bytes(mensagem,encoding="utf-8"))
            print("\nSent to the Server:     {}\n".format(mensagem))
        except Exception as e:
    #conn.close()
            print(e)
            print("\n")

    conn.close()


if __name__ == '__main__':
    host_name = socket.gethostname()

    HOST, PORT = "192.168.1.66" , 8089
    
    # ---------- heartbeat message ---------- #
    mensagem = "cliente_teste_mensagem"
    # ---------- CONEXAO SOCKET TCP ---------- #

    #--------------- build do objeto socket ---------------# 
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.connect((HOST, PORT))
#---Receive data from the server ---------------# 
    received = conn.recv(1024)
    received = received.decode("utf-8")
    print("\nReceived from the Server: {}\n".format(received))

#--- sending conf file to the server ---------------# 

    conn.sendall(bytes(mensagem,encoding="utf-8"))
    print("\nSent to the Server:     {}\n".format(mensagem))
    while True: 
        try:

            arquivo = leitura_json(file = json_file)
            print(arquivo)
            enviar_arquivo_socket(arquivo, conn)

            #---Receive data from the server ---------------# 
            received_2 = conn.recv(1024)
            received_2 = received_2.decode("utf-8")
            print("\nReceived from the Server: {}\n".format(received_2))


        except Exception as e:
    #conn.close()
            print(e)
            print("\n")
        time.sleep(1)
    conn.close()