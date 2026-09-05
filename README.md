# Controle de Vendas - CLI

Sistema de controle de vendas desenvolvido em Python para registrar e acompanhar fechamentos diários e mensais.

O projeto foi criado inicialmente como uma aplicação de terminal e posteriormente evoluiu para uma versão com interface gráfica e aplicativo Android.

## Funcionalidades

- Cadastro de meses
- Registro de fechamento diário
- Registro de pagamentos por:
  - Dinheiro
  - Pix
  - Cartão de crédito
  - Cartão de débito
- Cálculo automático do total diário
- Resumo mensal
- Resumo diário
- Edição de fechamentos
- Exclusão de fechamentos
- Persistência dos dados em JSON

## Tecnologias utilizadas

- Python 3
- JSON
- Git
- GitHub

## Estrutura do projeto

```text
Controle-de-Vendas-CLI/
├── main.py
├── funcoes.py
├── cadastro_mes.py
└── vendas.json


Como executar

Clone o repositório:
git clone git@github.com:candeany/Controle-de-Vendas-CLI.git

Entre na pasta:
cd Controle-de-Vendas-CLI

Execute:
python3 main.py


Sobre o projeto:

Este projeto foi desenvolvido para resolver uma necessidade real de controle de vendas de um pequeno comércio.

A primeira versão foi criada totalmente em terminal utilizando Python e JSON. Posteriormente, o projeto foi expandido com interface gráfica em Kivy e transformado em um aplicativo Android.

O objetivo do projeto é praticar lógica de programação, modularização, persistência de dados e desenvolvimento de soluções para problemas reais.
