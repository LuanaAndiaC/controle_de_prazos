# main.py
# Projeto: Controle de Prazos
# Autor: Luana Andia da Costa

def mostrar_menu():
    print("\n=== Controle de Prazos ===")
    print("1. Adicionar tarefa")
    print("2. Ver tarefas")
    print("3. Sair")

def adicionar_tarefa(tarefas):
    nome = input("Nome da tarefa: ")
    prazo = input("Prazo (dd/mm/aaaa): ")
    tarefas.append({"nome": nome, "prazo": prazo, "status": "Pendente"})
    print(f"Tarefa '{nome}' adicionada com sucesso!")

def ver_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return
    for i, tarefa in enumerate(tarefas, start=1):
        print(f"{i}. {tarefa['nome']} - Prazo: {tarefa['prazo']} - Status: {tarefa['status']}")

def main():
    tarefas = []
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            adicionar_tarefa(tarefas)
        elif opcao == "2":
            ver_tarefas(tarefas)
        elif opcao == "3":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
