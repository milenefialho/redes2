import socket
import math

# Configurações do servidor
HOST = '0.0.0.0'
PORT = 12345

# Função para calcular fatorial
def calcular_fatorial(n):
    return math.factorial(n)

# Função para calcular permutação
def calcular_permutacao(n, r):
    return math.perm(n, r)

# Função para calcular combinação
def calcular_combinacao(n, r):
    return math.comb(n, r)

# Função para calcular arranjo
def calcular_arranjo(n, r):
    return math.perm(n, r)  # Em Python, arranjo é o mesmo que permutação

# Função principal do servidor
def main():
    # Inicializa o socket do servidor
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen()

        print(f'Servidor TCP iniciado em {HOST}:{PORT}')

        # Loop para aceitar conexões dos clientes
        while True:
            # Aceita a conexão com o cliente
            conn, addr = server_socket.accept()
            print('Conectado com', addr)

            with conn:
                # Loop para receber e processar mensagens do cliente
                while True:
                    # Recebe a mensagem do cliente
                    requisicao = conn.recv(1024).decode()
                    if not requisicao:
                        break

                    # Processa a requisição
                    partes = requisicao.split(',')
                    operacao = partes[0]
                    argumentos = list(map(int, partes[1:]))

                    if operacao == 'fatorial':
                        resultado = calcular_fatorial(*argumentos)
                    elif operacao == 'permutacao':
                        resultado = calcular_permutacao(*argumentos)
                    elif operacao == 'combinacao':
                        resultado = calcular_combinacao(*argumentos)
                    elif operacao == 'arranjo':
                        resultado = calcular_arranjo(*argumentos)
                    else:
                        resultado = 'Operação inválida'

                    # Envia o resultado de volta para o cliente
                    conn.sendall(str(resultado).encode())

# Executa o servidor
if __name__ == '__main__':
    main()
