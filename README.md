# Sistema de Gerenciamento de Estoque 📦

***Este é um sistema simples de gerenciamento de estoque e ponto de venda (PDV) desenvolvido em Python. O programa roda inteiramente no terminal e permite ao usuário realizar as operações essenciais de controle de um pequeno negócio, como cadastrar produtos, realizar vendas, controlar o caixa e gerar relatórios.***

**Todos os dados são salvos localmente em arquivos .json e .txt, garantindo que as informações persistam mesmo após o programa ser fechado.**

## ✨ Funcionalidades Principais

    Gestão de Produtos: Cadastro, alteração e remoção de produtos no inventário.
    
    Controle de Estoque: Atualização automática da quantidade de produtos após compras e vendas.
    
    Módulo de Vendas: Função para vender produtos, atualizando o estoque e o saldo do caixa.
    
    Módulo de Compras: Função para registrar a compra de novos itens de fornecedores, atualizando o estoque e debitando do caixa.
    
    Geração de Relatórios: Criação de relatórios de vendas e de situação do estoque em arquivos de texto (.txt).
    
    Emissão de Notas: Geração automática de "notas fiscais" simplificadas para cada transação de compra ou venda.
    
    Persistência de Dados: Uso de arquivos JSON para salvar o estado do estoque e da empresa, permitindo continuar de onde parou.
    
    Interface de Linha de Comando (CLI): Interação com o usuário através de um menu simples e intuitivo no terminal.

## 🚀 Como Executar

*Requisitos: Certifique-se de ter o Python 3 instalado em sua máquina. Nenhuma biblioteca externa é necessária.*

*Download: Clone ou baixe os arquivos do projeto para o seu computador.*

*Execução: Abra um terminal ou prompt de comando, navegue até a pasta onde o arquivo do projeto está salvo e execute o seguinte comando:*

**python main.py**


## 📂 Estrutura de Arquivos e Pastas
*Ao ser executado, o script cria automaticamente uma estrutura de pastas e arquivos para organizar os dados gerados:*
    
    estoque.json: Arquivo principal que armazena o inventário completo, com todos os detalhes de cada produto.
    
    empresa.json: Armazena os dados financeiros da empresa, como o saldo atual do caixa e o total de vendas.
    
    📁 Relatorios_Estoque/
    
    Contém os relatórios detalhados de todo o inventário, gerados pela opção "Imprimir Estoque".
    
    📁 Empresa/
    
    📁 Notas_Fiscais_vendas/: Guarda as notas fiscais em .txt de cada venda realizada.
    
    📁 Notas_Fiscais_compras/: Guarda as notas fiscais em .txt de cada compra de reposição de estoque.
    
    📁 Relatorios_Caixa/: Contém os relatórios financeiros, com detalhes sobre as vendas e o caixa.

## 🛠️ Detalhes das Funções do Menu
*O sistema é operado através de um menu principal com as seguintes opções:*

    Opção	Descrição
    1	Cadastrar Produto
    2	Listar Produtos
    3	Vender Produto
    4	Gerar Relatório
    5	Imprimir Estoque
    6	Alterar Dados do Produto
    7	Remover Produto
    8	Sair
