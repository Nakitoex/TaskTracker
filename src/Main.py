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


def mostrar_tarefa(numero, tarefa):
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


# ---------- Funções de leitura e validação ----------

def mostrar_menu():
    titulo_secao("MENU PRINCIPAL")
    linha_esquerda("[1] Cadastrar nova tarefa")
    linha_esquerda("[2] Visualizar tarefas cadastradas")
    linha_esquerda("[3] Modificar uma tarefa")
    linha_esquerda("[4] Excluir uma tarefa")
    linha_esquerda("[5] Pesquisar tarefas por prioridade")
    linha_esquerda("[6] Sair da aplicação")
    borda("-")


def ler_titulo(atual=None):
    while True:
        if atual is None:
            titulo = input("  > Título (obrigatório): ").strip()
        else:
            titulo = input("  > Título [" + atual + "]: ").strip()
            if titulo == "":
                return atual  # Enter mantém o valor atual

        if titulo == "":
            mostrar_erro("O título não pode ser vazio. Tente novamente.")
        else:
            return titulo


def ler_prioridade(atual=None):
    while True:
        texto = "  > Prioridade (Alta / Média / Baixa)"
        if atual is not None:
            texto = texto + " [" + atual + "]"
        prioridade = input(texto + ": ").strip().capitalize()

        if prioridade == "" and atual is not None:
            return atual  # Enter mantém o valor atual
        elif prioridade == "Alta" or prioridade == "Baixa":
            return prioridade
        elif prioridade == "Média" or prioridade == "Media":
            return "Média"
        else:
            mostrar_erro("Prioridade inválida. Digite Alta, Média ou Baixa.")


def ler_status(atual):
    while True:
        status = input("  > Status (Pendente / Concluída) [" + atual + "]: ").strip().capitalize()

        if status == "":
            return atual  # Enter mantém o valor atual
        elif status == "Pendente":
            return "Pendente"
        elif status == "Concluída" or status == "Concluida":
            return "Concluída"
        else:
            mostrar_erro("Status inválido. Digite Pendente ou Concluída.")


def ler_numero_tarefa(lista_tarefas, acao):
    """Pede o número da tarefa e devolve o índice na lista (ou None se cancelar)."""
    while True:
        entrada = input("  > Número da tarefa a " + acao + " (0 para cancelar): ").strip()

        if not entrada.isdigit():
            mostrar_erro("Digite apenas números.")
            continue

        numero = int(entrada)
        if numero == 0:
            return None
        if 1 <= numero <= len(lista_tarefas):
            return numero - 1

        mostrar_erro("Tarefa inexistente. Escolha um número entre 1 e " + str(len(lista_tarefas)) + ".")


def lista_esta_vazia(lista_tarefas):
    if len(lista_tarefas) == 0:
        print()
        mostrar_aviso("Nenhuma tarefa cadastrada no momento. A lista está vazia.")
        return True
    return False


# ---------- Funções do programa ----------

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

    if lista_esta_vazia(lista_tarefas):
        return

    numero = 1
    for tarefa in lista_tarefas:
        mostrar_tarefa(numero, tarefa)
        numero = numero + 1

    print()
    print("  Total de tarefas: " + str(len(lista_tarefas)))


def modificar_tarefa(lista_tarefas):
    titulo_secao("MODIFICAR TAREFA")

    if lista_esta_vazia(lista_tarefas):
        return

    # Mostra a lista para o usuário escolher qual modificar
    numero = 1
    for tarefa in lista_tarefas:
        mostrar_tarefa(numero, tarefa)
        numero = numero + 1

    print()
    indice = ler_numero_tarefa(lista_tarefas, "modificar")
    if indice is None:
        mostrar_aviso("Modificação cancelada.")
        return

    tarefa = lista_tarefas[indice]

    print()
    mostrar_aviso("Pressione ENTER em qualquer campo para manter o valor atual.")
    print()

    tarefa["titulo"] = ler_titulo(tarefa["titulo"])

    descricao = input("  > Descrição [" + tarefa["descricao"] + "]: ").strip()
    if descricao != "":
        tarefa["descricao"] = descricao

    tarefa["prioridade"] = ler_prioridade(tarefa["prioridade"])

    data_limite = input("  > Data limite [" + tarefa["data_limite"] + "]: ").strip()
    if data_limite != "":
        tarefa["data_limite"] = data_limite

    tarefa["status"] = ler_status(tarefa["status"])

    print()
    mostrar_sucesso("Tarefa modificada com sucesso!")


def excluir_tarefa(lista_tarefas):
    titulo_secao("EXCLUIR TAREFA")

    if lista_esta_vazia(lista_tarefas):
        return

    numero = 1
    for tarefa in lista_tarefas:
        mostrar_tarefa(numero, tarefa)
        numero = numero + 1

    print()
    indice = ler_numero_tarefa(lista_tarefas, "excluir")
    if indice is None:
        mostrar_aviso("Exclusão cancelada.")
        return

    titulo = lista_tarefas[indice]["titulo"]
    confirmacao = input("  > Tem certeza que deseja excluir \"" + titulo + "\"? (s/n): ").strip().lower()

    if confirmacao == "s":
        lista_tarefas.pop(indice)
        print()
        mostrar_sucesso("Tarefa excluída com sucesso!")
    else:
        print()
        mostrar_aviso("Exclusão cancelada.")


def pesquisar_por_prioridade(lista_tarefas):
    titulo_secao("PESQUISAR POR PRIORIDADE")

    if lista_esta_vazia(lista_tarefas):
        return

    prioridade = ler_prioridade()

    encontradas = 0
    numero = 1
    for tarefa in lista_tarefas:
        if tarefa["prioridade"] == prioridade:
            mostrar_tarefa(numero, tarefa)  # mantém o número original da tarefa
            encontradas = encontradas + 1
        numero = numero + 1

    print()
    if encontradas == 0:
        mostrar_aviso("Nenhuma tarefa com prioridade " + prioridade + " foi encontrada.")
    else:
        print("  Tarefas com prioridade " + prioridade + ": " + str(encontradas))


def main():
    tarefas = []
    opcao = ""

    mostrar_banner()

    while opcao != "6":
        mostrar_menu()
        opcao = input("  Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_tarefa(tarefas)
        elif opcao == "2":
            visualizar_tarefas(tarefas)
        elif opcao == "3":
            modificar_tarefa(tarefas)
        elif opcao == "4":
            excluir_tarefa(tarefas)
        elif opcao == "5":
            pesquisar_por_prioridade(tarefas)
        elif opcao == "6":
            print()
            borda("=")
            linha_centro("Encerrando o TaskTracker. Até logo!")
            borda("=")
        else:
            print()
            mostrar_erro("Opção inválida. Digite um número de 1 a 6.")


main()
