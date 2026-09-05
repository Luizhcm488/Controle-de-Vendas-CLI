from cadastro_mes import cadastrar_mes
from funcoes import (
    carregar_vendas,
    adicionar_fechamento,
    mostrar_resumo,
    resumo_diario,
    excluir_fechamento,
    editar_fechamento,
)

opcoes = ["Cadastrar Mês", "Adicionar Fechamento", "Resumo Mensal", "Resumo Diário", "Editar Fechamento", "Excluir Fechamento", "Sair"]
meses = carregar_vendas()

while True:
    print("\n========== Controle de Vendas ==========\n")
    for numero, nome_opcao in enumerate(opcoes, start=1):
        print(f"{numero}- {nome_opcao}")

    try:
        opcao = int(input(f"Por favor, escolha uma opção (1-{len(opcoes)}): "))

    except ValueError:
        print("Digite apenas números!")
        continue

    if opcao < 1 or opcao > len(opcoes):
        print("Opção Inválida!")
        continue

    if opcao == len(opcoes):
        print("Saindo...\nPronto!")
        break

    elif opcao == 1:
        cadastrar_mes(meses)

    elif opcao == 2:
        adicionar_fechamento(meses)

    elif opcao == 3:
        mostrar_resumo(meses)

    elif opcao == 4:
        resumo_diario(meses)

    elif opcao == 5:
        editar_fechamento(meses)

    elif opcao == 6:
        excluir_fechamento(meses)