import socket

# Configurações do servidor
HOST = 'servidor'
PORT = 12345

# Função para enviar requisições ao servidor e receber resultados
def enviar_requisicao(requisicao):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))
        client_socket.sendall(requisicao.encode())
        resultado = client_socket.recv(1024).decode()
    return resultado

# Função principal do cliente
def main():
    while True:
        # Menu de opções
        print("Escolha uma operação:")
        print("1. Fatorial")
        print("2. Permutação")
        print("3. Combinação")
        print("4. Arranjo")
        print("5. Sair")

        opcao = input("Opção: ")

        if opcao == '1':
            n = int(input("Digite o número para calcular o fatorial: "))
            requisicao = f"fatorial,{n}"
            resultado = enviar_requisicao(requisicao)
            print(f"O fatorial de {n} é {resultado}")
        elif opcao == '2':
            n = int(input("Digite o valor de n para calcular a permutação: "))
            r = int(input("Digite o valor de r para calcular a permutação: "))
            requisicao = f"permutacao,{n},{r}"
            resultado = enviar_requisicao(requisicao)
            print(f"A permutação de {n} elementos tomados {r} a {r} é {resultado}")
        elif opcao == '3':
            n = int(input("Digite o valor de n para calcular a combinação: "))
            r = int(input("Digite o valor de r para calcular a combinação: "))
            requisicao = f"combinacao,{n},{r}"
            resultado = enviar_requisicao(requisicao)
            print(f"A combinação de {n} elementos tomados {r} a {r} é {resultado}")
        elif opcao == '4':
            n = int(input("Digite o valor de n para calcular o arranjo: "))
            r = int(input("Digite o valor de r para calcular o arranjo: "))
            requisicao = f"arranjo,{n},{r}"
            resultado = enviar_requisicao(requisicao)
            print(f"O arranjo de {n} elementos tomados {r} a {r} é {resultado}")
        elif opcao == '5':
            print("Encerrando o programa cliente.")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

# Executa o cliente
if __name__ == '__main__':
    main()
