import json

opcoes = {
    1: "dinheiro",
    2: "pix",
    3: "credito",
    4: "debito"
}

nomes_meses = {
    "01": "Janeiro",
    "02": "Fevereiro",
    "03": "Março",
    "04": "Abril",
    "05": "Maio",
    "06": "Junho",
    "07": "Julho",
    "08": "Agosto",
    "09": "Setembro",
    "10": "Outubro",
    "11": "Novembro",
    "12": "Dezembro"
}

def salvar_vendas(meses):
    """
    Salva as vendas em um arquivo JSON.
    """
    with open("vendas.json", "w") as arquivo:
        json.dump(meses, arquivo, indent=4)

def carregar_vendas():
    """
    Carrega as vendas de um arquivo JSON.
    """

    try:
        with open("vendas.json", "r") as arquivo:
            return json.load(arquivo)

    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def ler_valor(mensagem):
    """
    Lê um valor do usuário e garante que seja um número válido.
    """
    while True:
        valor = input(mensagem)
        valor = valor.replace(",", ".")  # Substitui vírgula por ponto

        try:
            valor = float(valor)
            if valor < 0:
                print("Valor inválido! Digite um número positivo.")
                continue


            return valor
        except ValueError:
            print("Valor inválido! Digite um número.")

def adicionar_fechamento(meses):
    """
    Adiciona o fechamento de um dia
    """

    chave = selecionar_mes(meses)

    if chave is None:
        return

    dia = int(input("Digite o dia do fechamento (DD): "))

    if dia < 1 or dia > 31:
        print("Data inválida! Digite um número entre 1 e 31.")
        return

    dia = str(dia).zfill(2)

    if dia in meses[chave]:
        print("Esse dia já possui fechamento cadastrado!")
        return

    dinheiro = ler_valor("Digite o valor em dinheiro: R$ ")
    pix = ler_valor("Digite o valor em PIX: R$ ")
    credito = ler_valor("Digite o valor em cartão de crédito: R$ ")
    debito = ler_valor("Digite o valor em cartão de débito: R$ ")

    total = dinheiro + pix + credito + debito
    meses[chave][dia] = {
         "dinheiro": dinheiro,
         "pix": pix,
         "credito": credito,
         "debito": debito
     }

    salvar_vendas(meses)
    print(f"Fechamento do dia {dia} do mês {chave} cadastrado com sucesso!")
    print(f"Total do dia: R$ {total:.2f}")

def mostrar_resumo(meses):
    """
    Mostra o resumo de um mês
    """

    chave = selecionar_mes(meses)

    if chave is None:
        return

    total_dinheiro = 0
    total_pix = 0
    total_credito = 0
    total_debito = 0

    for dia in meses[chave]:
        fechamento = meses[chave][dia]

        total_dinheiro += fechamento["dinheiro"]
        total_pix += fechamento["pix"]
        total_credito += fechamento["credito"]
        total_debito += fechamento["debito"]

    total_cartao = total_credito + total_debito
    total_mes = total_pix + total_dinheiro + total_cartao

    print(f"========== RESUMO {chave} ==========\n\n")
    print(f"Dinheiro: R${total_dinheiro:.2f}")
    print(f"Pix: R${total_pix:.2f}")
    print(f"Crédito: R${total_credito:.2f}")
    print(f"Débito: R${total_debito:.2f}\n\n")
    print("-------------------------------------")
    print(f"Total cartões: R${total_cartao:.2f}\n")
    print("-------------------------------------")
    print(f"Total do Mês: R${total_mes:.2f}")

def resumo_diario(meses):
    chave = selecionar_mes(meses)

    if chave is None:
        return

    dia = int(input("Digite o dia: "))

    if dia < 1 or dia > 31:
        print("Dia inválido!")
        return

    dia = str(dia).zfill(2)

    if dia not in meses[chave]:
        print("Não existe fechamento cadastrado para esse dia!")
        return

    fechamento = meses[chave][dia]

    dinheiro = fechamento["dinheiro"]
    pix = fechamento["pix"]
    credito = fechamento["credito"]
    debito = fechamento["debito"]

    total_cartao = credito + debito
    total_dia = dinheiro + pix + total_cartao

    print(f"========== RESUMO {dia}/{chave} ==========\n\n")
    print(f"Dinheiro: R${dinheiro:.2f}")
    print(f"Pix: R${pix:.2f}")
    print(f"Crédito: R${credito:.2f}")
    print(f"Débito: R${debito:.2f}\n\n")
    print("-------------------------------------")
    print(f"Total cartões: R${total_cartao:.2f}\n")
    print("-------------------------------------")
    print(f"Total do Dia: R${total_dia:.2f}")

def editar_fechamento(meses):
    """
    Edita os valores de um fechamento já cadastrado
    """

    chave = selecionar_mes(meses)

    if chave is None:
        return

    dia = int(input("Digite o dia: "))

    if dia < 1 or dia > 31:
        print("Dia inválido!")
        return

    dia = str(dia).zfill(2)

    if dia not in meses[chave]:
        print("Não existe fechamento cadastrado para esse dia!")
        return

    fechamento = meses[chave][dia]

    print("========= FECHAMENTO ATUAL =========")
    print(f"1- Dinheiro: R${fechamento['dinheiro']:.2f}")
    print(f"2- Pix: R${fechamento['pix']:.2f}")
    print(f"3- Crédito: R${fechamento['credito']:.2f}")
    print(f"4- Débito: R${fechamento['debito']:.2f}")
    print("5- Cancelar")

    try:
        opcao = int(input("Por favor, escolha uma opção: (1-5)"))

    except ValueError:

        print("Digite apenas números!")
        return

    if opcao == 5:
        print("Cancelando...\nPronto!")
        return

    if opcao not in opcoes:
        print("Opção Inválida!")
        return

    campo = opcoes[opcao]

    novo_valor = ler_valor("Por favor, digite o novo valor: R$ ")

    fechamento[campo] = novo_valor

    salvar_vendas(meses)
    print("Fechamento atualizado com sucesso!")

def excluir_fechamento(meses):
    """
    Exclui o fechamento de um dia cadastrado
    """

    chave = selecionar_mes(meses)

    if chave is None:
        return
    
    dia = int(input("Digite o dia: "))

    if dia < 1 or dia > 31:
        print("Dia inválido!")
        return

    dia = str(dia).zfill(2)

    if dia not in meses[chave]:
        print("Não existe fechamento cadastrado para esse dia!")
        return

    fechamento = meses[chave][dia]

    print(f"========== Fechamento {dia}/{chave} ==========\n")
    print(f"Dinheiro: R${fechamento['dinheiro']:.2f}")
    print(f"Pix: R${fechamento['pix']:.2f}")
    print(f"Crédito: R${fechamento['credito']:.2f}")
    print(f"Débito: R${fechamento['debito']:.2f}\n")

    confirmacao = input("Tem certeza que deseja excluir esse fechamento? (S/N): ").strip().lower()

    if confirmacao.lower() == "s":
        del meses[chave][dia]
        salvar_vendas(meses)
        print("Fechamento excluído com sucesso!")

    else:
        print("Operação cancelada!")
        return

def selecionar_mes(meses):
    """
    Mostra os meses cadastrados e retorna o mês escolhido.
    """

    if not meses:
        print("Nenhum mês cadastrado!")
        return

    lista_meses = list(meses.keys())

    for numero, chave_mes in enumerate(lista_meses, start=1):
        mes, ano = chave_mes.split("-")
        nome_mes = nomes_meses[mes]
        print(f"{numero} - {nome_mes}/{ano}")

    try:
        opcao = int(input("Escolha um mês: "))

    except ValueError:
        print("Digite apenas números!")
        return

    if opcao < 1 or opcao > len(lista_meses):
        print("Mês inválido!")
        return

    mes_escolhido = lista_meses[opcao - 1]
    return mes_escolhido