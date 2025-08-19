import json
import os
from random import randint
from time import sleep
from datetime import datetime
import datetime

#region  /Save|Load/

def save(arquivo, dados):
    print("Salvando os dados...")
    try:
        with open(arquivo, "w") as file:
            json.dump(dados, file, indent=4)
        print("Dados Salvos com Sucesso")
    except Exception as e:
        print(f"Erro ao salvar os dados: {e}")

def load(arquivo):
    try:
        with open(arquivo, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


#endregion

#region /Funções do Estoque/

def cadastrar_produto(vEstoque):

    codigo = validarcodigo(vEstoque)
    nome = input("Digite o nome do produto: ")
    print("Preço de Venda:", end="")
    preco_venda = validarfloatnumeros()
    print("Preço de Compra:", end="")
    preco_compra = validarfloatnumeros()
    print("Quantidade no Estoque:", end="")
    quantidade_estoque = validarintnumeros()
    fornecedor = input("Digite o nome do fornecedor: ")
    print("Data Validade:", end="")
    data_validade = validadordata()
    print("Data Entrada:", end="")
    data_entrada = validadordata()
    Tempo_para_venda = data_validade - data_entrada
    Tempo_em_estoque = data_validade - datetime.datetime.now().date()

    vEstoque[codigo] = {

        "produto" : nome,
        "precoVenda" : preco_venda,
        "precoCompra" : preco_compra,
        "qtd_estoque" : quantidade_estoque,
        "fornecedor" : fornecedor,
        "data_validade" : str(data_validade),
        "data_entrada" : str(data_entrada),
        "Tempo_para_venda" : str(Tempo_para_venda),
        "Tempo_em_estoque" : str(Tempo_em_estoque),
        "Vendas" : 0

    }

    os.makedirs("Estoque", exist_ok=True)
    caminho_arquivo = os.path.join("Estoque", "estoque.json")
    save(caminho_arquivo, vEstoque)
    print("Produto cadastrado com sucesso")

def alterar_dados_produtos(vEstoque,codigo):
    codigo = buscar_produto(vEstoque,codigo)
    if codigo == None:
        print("Produto não encontrado.")
        return 0;
    else:

        print("Produto encontrado.")

        print("=" * 30)
        print("Você deseja alterar:\n\t 1 - Nome\n\t 2 - Preço de Venda\n\t 3 - Preço de Compra\n\t 4 - Quantidade em Estoque\n\t 5 - Fornecedor\n\t 6 - Data de Validade\n\t 7 - Data de Entrada")
        print("=" * 30)

        opcao = opcoes()
        match opcao:
            case "1":
                vEstoque[codigo]["produto"] = input("Digite o nome do produto: ")
                print("Nome alterado com sucesso!")

            case "2":
                vEstoque[codigo]["precoVenda"] = validarfloatnumeros()
                print("Preço de Venda alterado com sucesso!")

            case "3":
                vEstoque[codigo]["precoCompra"] = validarfloatnumeros()
                print("Preço de Compra alterado com sucesso!")

            case "4":
                vEstoque[codigo]["qtd_estoque"] = validarintnumeros()
                print("Quantidade em Estoque alterado com sucesso!")

            case "5":
                vEstoque[codigo]["fornecedor"] = input("Digite o nome do fornecedor: ")
                print("Fornecedor alterado com sucesso!")

            case "6":
                vEstoque[codigo]["data_validade"] = validadordata()
                print("Data de Validade alterado com sucesso!")

            case "7":
                vEstoque[codigo]["data_entrada"] = validadordata()
                print("Data de Entrada alterado com sucesso!")
            
            case _:
                print("Opção inválida")
                sleep(1)

        save("Estoque/estoque.json", vEstoque)
        sleep(1)

def remover_produto(vEstoque,codigo):
    chave = buscar_produto(vEstoque,codigo)
    if chave == None:
        print("Produto não encontrado.")
        return 0;
    else:
        print("Produto encontrado.")
        del vEstoque[chave]
        print("Produto removido com sucesso!")
        save("Estoque/estoque.json", vEstoque)
        sleep(1)

def buscar_produto(vEstoque,codigo):
    if codigo in vEstoque:
        return codigo
    else:
        return None

def verificador_estoque(vEstoque):
    for i, estoque in vEstoque.items():
        if estoque['qtd_estoque'] <= 0:
            print(f"Produto: {estoque['produto']}")
            print("Situação: Fora de Estoque")
            print("-" * 30)
        elif estoque['qtd_estoque'] <= 10:
            print(f"Produto: {estoque['produto']}")
            print("Situação: Pouco Estoque")
            print(f"Estoque: {estoque['qtd_estoque']}")
            print("-" * 30)
        else:
            print(f"Produto: {estoque['produto']}")
            print("Situação: Em Estoque")
            print(f"Estoque: {estoque['qtd_estoque']}")
            print("-" * 30)

def imprimir_estoque(vEstoque):
    texto = "Estoque de Produtos\n"
    texto += "=" * 30 + "\n"
    for codigo, produto in vEstoque.items():
        texto += f"Código: {codigo}\n"
        texto += f"Nome: {produto['produto']}\n"
        texto += f"Preço de Venda: {produto['precoVenda']}\n"
        texto += f"Preço de Compra: {produto['precoCompra']}\n"
        texto += f"Quantidade em Estoque: {produto['qtd_estoque']}\n"
        texto += f"Fornecedor: {produto['fornecedor']}\n"
        texto += f"Data de Validade: {produto['data_validade']}\n"
        texto += f"Data de Entrada: {produto['data_entrada']}\n"
        texto += f"Tempo para Venda: {produto['Tempo_para_venda']}\n"
        texto += f"Tempo em Estoque: {produto['Tempo_em_estoque']}\n"
        texto += "=" * 30 + "\n"

    os.makedirs("Relatorios_Estoque", exist_ok=True)
    caminho_arquivo = os.path.join("Relatorios_Estoque", "estoque.txt")
    try:
        with open(caminho_arquivo, "w") as arquivo:
            arquivo.write(texto)
        print("Estoque gerado com sucesso")
    except Exception as e:
        print(f"Erro ao gerar o estoque: {e}")

    print("Deseja Visualizar o Estoque? (S/N)")
    op = opcoes_sn()

    if op.upper() == "S":
        with open(caminho_arquivo, "r") as arquivo:
            print(arquivo.read())
    else:
        print("Voltando ao menu...")
        sleep(1)

#endregion

#region /Fuções do Caixa/

def empresa(vEstoque):
    vEmpresa = {

        "caixa" : 0,
        "vendastotais" : 0,
        "variedadeprodutos" : len(vEstoque)
    }

    os.makedirs("Empresa", exist_ok=True)
    caminho_arquivo = os.path.join("Empresa", "empresa.json")
    save(caminho_arquivo, vEmpresa)

def listar_produtos_venda(vEstoque):

    for codigo, produto in vEstoque.items():
        print(f"Código: {codigo}")
        print(f"Nome: {produto['produto']}")
        print(f"Preço de Venda: {produto['precoVenda']}")
        print(f"Quantidade em Estoque: {produto['qtd_estoque']}")

def comprar_produto(vEstoque, vEmpresa, codigo):
    chave = buscar_produto(vEstoque,codigo)
    if chave == None:
        print("Produto não encontrado.")
        return 0;

    else:
        while True:

            print("Produto encontrado.")
            print("=" * 30)
            print(f"Produto: {vEstoque[chave]['produto']}")
            print(f"Preço de Venda: {vEstoque[chave]['precoCompra']}")
            print(f"Fornecedor: {vEstoque[chave]['fornecedor']}")
            print("=" * 30)
            print("Deseja comprar este produto? (S/N)")

            op = opcoes_sn()

            if op.upper() == "N":
                print("Voltando ao menu...")
                sleep(1)
                break

            quantidade = validarintnumeros()
            valortotal = vEstoque[chave]['precoCompra'] * quantidade

            if quantidade <= 0:
                print("Quantidade inválida.")
                continue

            else:
                if valortotal > vEmpresa["caixa"]:
                    print("Caixa insuficiente.")
                    continue

                else:
                    vEstoque[chave]['qtd_estoque'] += quantidade
                    vEmpresa['caixa'] -= valortotal

                    nota_fiscal(vEstoque[chave], quantidade, "compra")

                    print("Produto comprado Com Sucesso!")
                    save("estoque.json", vEstoque)
                    save("empresa.json", vEmpresa)
                    sleep(1)
                    break

def vender_produto(vEstoque, vEmpresa, codigo):
    chave = buscar_produto(vEstoque,codigo)
    if chave == None:
        print("Produto não encontrado.")
        return 0;

    else:
        print("Produto encontrado.")
        print("Quantos deseja comprar?", end="")
        quantidade = validarintnumeros()

        if quantidade <= 0:
            print("Quantidade inválida.")
            return 0;

        elif quantidade > vEstoque[chave]['qtd_estoque']:
            print("Quantidade em estoque insuficiente.")
            return 0;

        else:
            vEstoque[chave]['qtd_estoque'] -= quantidade
            vEstoque[chave]['Vendas'] += quantidade

            vEmpresa['caixa'] += vEstoque[chave]['precoVenda'] * quantidade
            vEmpresa['vendastotais'] += vEstoque[chave]['precoVenda'] * quantidade

            nota_fiscal(vEstoque[chave], quantidade, "venda")

            print("Produto vendido com sucesso!")
            save("Estoque/estoque.json", vEstoque)
            sleep(1)

def nota_fiscal(a , b, c):

    texto = "Nota Fiscal\n"
    texto += "=" * 30 + "\n"
    texto += f"Produto: {a['produto']}\n"
    texto += f"Quantidade: {b}\n"
    texto += f"Preço de Venda: {a['precoVenda']}\n"
    texto += f"Total: {a['precoVenda'] * b}\n"
    texto += "=" * 30 + "\n"

    if c == "venda":
        os.makedirs("Empresa/Notas_Fiscais_vendas", exist_ok=True)
        caminho_arquivo = os.path.join("Notas_Fiscais_vendas", f"nota_fiscal_{a['produto']}.txt")
        try:
            with open(caminho_arquivo, "w") as arquivo:
                arquivo.write(texto)
            print("Nota Fiscal gerada com sucesso")
        except Exception as e:
            print(f"Erro ao gerar a nota fiscal: {e}")

    else:
        os.makedirs("Empresa/Notas_Fiscais_compras", exist_ok=True)
        caminho_arquivo = os.path.join("Empresa","Notas_Fiscais_compras", f"nota_fiscal_{a['produto']}.txt")
        try:
            with open(caminho_arquivo, "w") as arquivo:
                arquivo.write(texto)
            print("Nota Fiscal gerada com sucesso")
        except Exception as e:
            print(f"Erro ao gerar a nota fiscal: {e}")

def gerar_relatorio(vEstoque, vEmpresa):
    texto = "Relatório de Vendas\n"
    texto += "=" * 30 + "\n"

    for codigo, produto in vEstoque.items():
        if produto['Vendas'] > 0:
            texto += f"Código: {codigo}\n"
            texto += f"Nome: {produto['produto']}\n"
            texto += f"Preço de Venda: {produto['precoVenda']}\n"
            texto += f"Quantidade em Estoque: {produto['qtd_estoque']}\n"
            texto += "=" * 30 + "\n"
            texto += f"Total de Vendas: {produto['Vendas']}\n"
            texto += "=" * 30 + "\n"

    texto += f"Caixa: {vEmpresa['caixa']}\n"
    texto += f"Vendas Totais: {vEmpresa['vendastotais']}\n"

    os.makedirs("Empresa/Relatorios_Caixa", exist_ok=True)
    caminho_arquivo = os.path.join("Relatorios_Caixa", "relatorio.txt")
    try:
        with open(caminho_arquivo, "w") as arquivo:
            arquivo.write(texto)
        print("Relatório gerado com sucesso")

    except Exception as e:
        print(f"Erro ao gerar o relatório: {e}")




#endregion

#region  /Validações/

def validarintnumeros():
    while True:
        try:
            numero = int(input())
            return numero
        except ValueError:
            print("Por favor, digite um número inteiro válido.")

def validarfloatnumeros():
    while True:
        try:
            numero = float(input())
            return numero
        except ValueError:
            print("Por favor, digite um número válido.")

def validarcodigo(vEstoque):
    while True:
        codigo = randint(1000,9999)
        if codigo not in vEstoque:
            return codigo
        else:
            continue

def validadordata():
    while True:
        data = input("Digite a data (DD/MM/AAAA): ")
        try:
            return datetime.datetime.strptime(data, "%d/%m/%Y").date()

        except ValueError:
            print("Data inválida. Use o formato DD/MM/AAAA.")
            continue

#endregion

#region  /Menu/

def menu():
    print("=" * 30)
    print("Sistema de Estoque Inteligente")
    print("=" * 30)
    print("1. Cadastrar Produto")
    print("2. Listar Produtos")
    print("3. Vender Produto")
    print("4. Gerar Relatório")
    print("5. Imprimir Estoque")
    print("6. Alterar Dados do Produto")
    print("7. Remover Produto")
    print("8. Sair")
    print("=" * 30)

def opcoes():
    opcao = input("Escolha uma opção: ")
    while opcao not in ["1","2","3","4","5","6","7","8"]: opcao = input("Opção Invalida\nEscolha uma opção: ")
    return opcao

def opcoes_sn():
    opcao = input("Deseja continuar? (S/N): ")
    while opcao.upper() not in ["S" ,"N"]: opcao = input("Deseja continuar? (S/N): ")
    return opcao

#endregion

def main():
    #region    /Variaveis Iniciais/

    os.makedirs("Estoque", exist_ok=True)
    os.makedirs("Empresa", exist_ok=True)
    os.makedirs("Relatorios_Estoque", exist_ok=True)
    os.makedirs("Empresa/Notas_Fiscais_vendas", exist_ok=True)
    os.makedirs("Empresa/Notas_Fiscais_compras", exist_ok=True)
    os.makedirs("Empresa/Relatorios_Caixa", exist_ok=True)
    os.makedirs("Relatorios_Caixa", exist_ok=True)

    vEstoque = load("estoque.json")

    if not os.path.exists("empresa.json"):
        empresa(vEstoque)

    vEmpresa = load("empresa.json")
    vEmpresa.setdefault("caixa", 0)
    vEmpresa.setdefault("vendastotais", 0)
    vEmpresa.setdefault("variedadeprodutos", 0)


    #endregion

    while True:
        menu()
        opcao = opcoes()

        match opcao:

            case "1":
                print("=" * 30)
                print("  Cadastro de Produto")
                print("=" * 30)
                cadastrar_produto(vEstoque)
                print("=" * 30)

            case "2":
                print("=" * 30)
                print("\tProdutos")
                print("=" * 30)
                listar_produtos_venda(vEstoque)
                print("=" * 30)

            case "3":
                print("=" * 30)
                print("   Venda de Produtos")
                print("=" * 30)
                codigo = validarintnumeros()
                vender_produto(vEstoque, vEmpresa, codigo)

            case "4":
                print("=" * 30)
                print("   Relatório de Vendas")
                print("=" * 30)
                gerar_relatorio(vEstoque, vEmpresa)
                print("=" * 30)

            case "5":
                print("=" * 30)
                print(" Estoque")
                print("=" * 30)
                imprimir_estoque(vEstoque)
                print("=" * 30)

            case "6":
                print("=" * 30)
                print(" Alterar Dados do Produto")
                print("=" * 30)
                codigo = validarintnumeros()
                alterar_dados_produtos(vEstoque,codigo)
                print("=" * 30)

            case "7":
                print("=" * 30)
                print("   Remover Produto")
                print("=" * 30)
                codigo = validarintnumeros()
                remover_produto(vEstoque,codigo)
                print("=" * 30)

            case "8":
                print("Saindo do programa...")
                sleep(1)
                break
                
            case _:
                print("Opção inválida")
                sleep(1)

main()

#endregion
