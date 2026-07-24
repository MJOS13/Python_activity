<!DOCTYPE html>
<html>
  <head>
    <link rel="stylesheet" href="https://pyscript.net/releases/2024.1.1/core.css" />
    <script type="module" src="https://pyscript.net/releases/2024.1.1/core.js"></script>
  </head>
  <body>
    <h1>My Python Web Page</h1>
    
    <script type="py" src="./script.py" config='{"files": ["./script.py"]}'></script>
  </body>
</html>

# ==========================================
# APLICAÇÃO DE REGISTO E LOGIN DE UTILIZADOR
# ==========================================

# Tuplo com as opções fixas do menu
OPCOES_MENU = ("1", "2")

# Dicionário para armazenar os dados do utilizador
utilizador = {
    "username": "",
    "password": "",
    "tentativas": 0,
    "bloqueada": False
}

# Lista para guardar o histórico das tentativas de login
historico_logins = []


def registar_utilizador():
    # Processo de boas-vindas e registo do utilizador.#
    print("\n--- REGISTO DE UTILIZADOR ---")
    print("Seja bem-vindo(a)!")
    
    username = input("Introduza o seu username: ").strip()
    password = input("Introduza a sua password: ").strip()
    
    # Armazena os dados no dicionário
    utilizador["username"] = username
    utilizador["password"] = password
    utilizador["tentativas"] = 0
    utilizador["bloqueada"] = False
    
    print("\nRegisto efetuado com sucesso!")


def efetuar_login():
    """Gere o processo de autenticação e controlo de tentativas."""
    print("\n--- LOGIN ---")
    
    # Verificar se a conta está bloqueada antes de tentar o login
    if utilizador["bloqueada"]:
        print("A sua conta está bloqueada devido a 2 tentativas incorretas consecutivas.")
        return

    # Verificar se o utilizador já efetuou o registo
    if not utilizador["username"]:
        print("Nenhum utilizador registado ainda. Por favor, reinicie a aplicação.")
        return

    # Loop para controlar até 2 tentativas de login
    while utilizador["tentativas"] < 2:
        user_input = input("Username: ").strip()
        pass_input = input("Password: ").strip()

        # Validação dos dados introduzidos
        if user_input == utilizador["username"] and pass_input == utilizador["password"]:
            print("\nBem-vindo de volta!")
            utilizador["tentativas"] = 0  # Reinicia o contador em caso de sucesso
            historico_logins.append("Sucesso")
            return
        else:
            utilizador["tentativas"] += 1
            historico_logins.append("Insucesso")
            print("Dados inválidos.")
            
            # Notifica quantas tentativas restam
            tentativas_restantes = 2 - utilizador["tentativas"]
            if tentativas_restantes > 0:
                print(f"Resta-lhe {tentativas_restantes} tentativa(s).\n")

    # Se atingiu 2 tentativas falhadas, bloqueia a conta
    if utilizador["tentativas"] >= 2:
        utilizador["bloqueada"] = True
        print("\nAtingiu o limite de 2 erros consecutivos. A sua conta foi bloqueada!")


def apresentar_menu():
    """Exibe o menu principal e valida a opção escolhida."""
    while True:
        print("\n====================")
        print("   MENU PRINCIPAL   ")
        print("====================")
        print(f"{OPCOES_MENU[0]}. Login")
        print(f"{OPCOES_MENU[1]}. Sair")
        
        opcao = input("Escolha uma opção: ").strip()
        
        # Validação da opção do menu
        if opcao in OPCOES_MENU:
            return opcao
        else:
            print("Opção inválida! Por favor, escolha 1 ou 2.")


def main():
    """Função principal que coordena o fluxo do programa."""
    # Fase inicial: Registo obrigatório
    registar_utilizador()
    
    # Loop do menu principal
    while True:
        opcao = apresentar_menu()
        
        if opcao == OPCOES_MENU[0]:  # Opção 1: Login
            efetuar_login()
        elif opcao == OPCOES_MENU[1]:  # Opção 2: Sair
            print("\nObrigado por utilizar a nossa aplicação. Até breve!")
            break


# Execução do programa
if __name__ == "__main__":
    main()
