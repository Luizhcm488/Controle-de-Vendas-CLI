from funcoes import salvar_vendas

def cadastrar_mes(meses):
    """
    Cadastra um novo mês no sistema.
    """

    try:

        mes = int(input("Digite numero do mês que deseja cadastrar: "))

    except ValueError:
        print("Digite apenas números!")
        return


    if mes < 1 or mes > 12:
        print("Esse mês não existe! Digite um número entre 1 e 12.")
        return

    ano = int(input("Digite o ano do mês que deseja cadastrar: "))

    #zfill() adiciona zeros à esquerda do número, caso ele tenha menos de 2 dígitos
    #entretanto só funciona com strings, por isso é necessário converter o número para string antes de chamar a função zfill()
    chave = f"{str(mes).zfill(2)}-{ano}"

    if chave in meses:
        print("Mês já cadastrado!")
        return

    meses[chave] = {}
    salvar_vendas(meses)
    print(f"Mês {chave} cadastrado com sucesso!")