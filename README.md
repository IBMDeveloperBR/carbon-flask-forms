# carbon-flask-forms

Este repositório contém um servidor flask interfaceado via gunicorn, já configurado para implantação na Cloud Foundry da IBM Cloud. A aplicação Web é um template para a criação de formulários, com algumas funções prontas para tratamento de _inputs_ (nome, cpf, e-mail) e retorno de mensagens de erro. O _front-end_ é baseado no IBM Carbon Design System, com uma animação svg customizada para quando o usuário espera o formulário ser tratado pelo _back-end_.

## Medidas de segurança implementadas

- Proteção contra CSRF
- Proteção contra XSS
- Protocolo HTTPS forçado
- Medidas básicas contra SQL-Injection (tratamento de I/O no _back-end_)

## Medidas que precisam ser implementadas

- Remover css não utilizado do arquivo `ibm_carbon.css` para tornar a aplicação mais "_lightweight_";
- Refatorar o código Javascript para não utilizar o `JQuery`.

## Executando a aplicação localmente

- Comente fora do arquivo `app.py` a linha onde a comunicação SSL é configurada.
- Execute a aplicação com o comando `python -m flask run`

## Implantando a aplicação na IBM Cloud

- Faça login na IBM Cloud via CLI
- Escolha interativamente a Org e Space da Cloud Foundry desejada via o comando `ibmcloud target --cf`; e
- Inicie o _deploy_ da aplicação via o comando `ibmcloud cf push`;
