from datetime import datetime

def registrar_entrada_saida(nome_funcionario):
    agora = datetime.now()
    hora_formatada = agora.strftime('%d/%m/%Y %H:%M:%S')

    with open('ponto.txt', 'a') as arquivo:
        arquivo.write(f'{nome_funcionario} - {hora_formatada}\n')
    
    print(f'Registrado: {nome_funcionario} - {hora_formatada}')

def visualizar_registros():
    try:
        with open('ponto.txt', 'r') as arquivo:
            registros = arquivo.readlines()
            if registros:
                print("Registros de ponto:")
                for registro in registros:
                    print(registro.strip())
            else:
                print("Nenhum registro encontrado.")
    except FileNotFoundError:
        print("Nenhum registro encontrado.")

def menu():
    while True:
        print("\nSistema de Ponto Eletrônico")
        print("1. Registrar Entrada/Saída")
        print("2. Visualizar Registros")
        print("3. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome_funcionario = input("Digite o nome do funcionário: ")
            registrar_entrada_saida(nome_funcionario)
        elif opcao == '2':
            visualizar_registros()
        elif opcao == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")

if _name_ == "_main_":
    menu()