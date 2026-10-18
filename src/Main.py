LARGURA = 60


# ---------- Funções de desenho (só cuidam da aparência) ----------

def borda(caractere="-"):
    print("+" + caractere * (LARGURA - 2) + "+")


def linha_centro(texto=""):
    print("|" + texto.center(LARGURA - 2) + "|")


def linha_esquerda(texto=""):
    print("| " + texto.ljust(LARGURA - 4) + " |")


def titulo_secao(texto):
    print()
    borda("-")
    linha_centro(texto)
    borda("-")


def mostrar_banner():
    borda("=")
    linha_centro()
    linha_centro("T A S K T R A C K E R")
    linha_centro()
    linha_centro("Gerenciador de tarefas pelo terminal")
    borda("=")


def mostrar_erro(mensagem):
    print("  [ERRO] " + mensagem)


def mostrar_sucesso(mensagem):
    print("  [OK] " + mensagem)


def mostrar_aviso(mensagem):
    print("  [!] " + mensagem)


# ---------- Funções do programa ----------

def mostrar_menu():
    titulo_secao("MENU PRINCIPAL")
    linha_esquerda("[1] Cadastrar nova tarefa")
    linha_esquerda("[2] Visualizar tarefas cadastradas")
    linha_esquerda("[3] Sair da aplicação")
    borda("-")


def ler_titulo():
    while True:
        titulo = input("  > Título (obrigatório): ").strip()
        if titulo == "":
            mostrar_erro("O título não pode ser vazio. Tente novamente.")
        else:
            return titulo


def ler_prioridade():
    while True:
        prioridade = input("  > Prioridade (Alta / Média / Baixa): ").strip().capitalize()
        if prioridade == "Alta" or prioridade == "Baixa":
            return prioridade
        elif prioridade == "Média" or prioridade == "Media":
            return "Média"
        else:
            mostrar_erro("Prioridade inválida. Digite Alta, Média ou Baixa.")


def cadastrar_tarefa(lista_tarefas):
    titulo_secao("CADASTRO DE NOVA TAREFA")

    titulo = ler_titulo()
    descricao = input("  > Descrição: ").strip()
    prioridade = ler_prioridade()
    data_limite = input("  > Data limite (ex: 20/10/2026): ").strip()

    if descricao == "":
        descricao = "Sem descrição"
    if data_limite == "":
        data_limite = "Não informada"

    tarefa = {
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "data_limite": data_limite,
        "status": "Pendente"
    }

    lista_tarefas.append(tarefa)
    print()
    mostrar_sucesso("Tarefa cadastrada com sucesso!")


def visualizar_tarefas(lista_tarefas):
    titulo_secao("TAREFAS CADASTRADAS")

    if len(lista_tarefas) == 0:
        print()
        mostrar_aviso("Nenhuma tarefa cadastrada no momento. A lista está vazia.")
        return

    numero = 1
    for tarefa in lista_tarefas:
        print()
        borda("-")
        print("| TAREFA " + str(numero))
        borda("-")
        print("| Título      : " + tarefa["titulo"])
        print("| Descrição   : " + tarefa["descricao"])
        print("| Prioridade  : " + tarefa["prioridade"])
        print("| Data limite : " + tarefa["data_limite"])
        print("| Status      : " + tarefa["status"])
        borda("-")
        numero = numero + 1

    print()
    print("  Total de tarefas: " + str(len(lista_tarefas)))


def main():
    tarefas = []
    opcao = ""

    mostrar_banner()

    while opcao != "3":
        mostrar_menu()
        opcao = input("  Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_tarefa(tarefas)
        elif opcao == "2":
            visualizar_tarefas(tarefas)
        elif opcao == "3":
            print()
            borda("=")
            linha_centro("Encerrando o TaskTracker. Até logo!")
            borda("=")
        else:
            print()
            mostrar_erro("Opção inválida. Digite 1, 2 ou 3.")


main()