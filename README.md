# Pedidos Lanchonete

> Sistema que realiza um <b>CRUD</b> dos clientes, endereços e produtos, para ser usado para realizar pedido de uma lanchonete.

<p>🚀 Projeto de pedidos para lanchonete, para fins educacionais, desenvolvido pelos alunos <a href="https://github.com/pac57282"><b>Marcelo do Nascimento</b></a> e <a href="https://github.com/titioneamorim"><b>Titione Falacio Amorim</b></a>, para a disciplina de <b>Desenvolvimento Web</b>, do professor <a href="https://github.com/Alexvjunior"><b>Alexsander Vieira Junior</b></a>, do curso de ADS da faculdade <a href="https://portal.sc.senac.br/portal/home/"><b>Senac Palhoça</b></a>.</p>

<p> Projeto desenvolvido no framework <a href="https://www.djangoproject.com/"><b>Django</b></a>.</p>

Por ser um projeto <b>Django</b>, esse projeto pode ser executado em <b>Linux, Mac e Windows</b>.

## Instalação

Para rodar o projeto corretamente, é necessário ter instalado o <a href="https://www.python.org/"><b>Python 3</b></a> e os seguintes compenentes:

<p><b>Django:</b></p>

```sh
pip install django
```

<p><b>Django Rest Framework:</b></p>

```sh
pip install djangorestframework
```

Caso esteja utilizando o <b>Python 3.10</b>, é necessário intalar o Django Extensions
<p><b>Django Extensions:</b></p>

```sh
pip install django-extensions
```
## Arquivos de Configuração

Ao instalar o Django, automaticamente é instalado o servidor de Banco de dados SQLlite, que é o que foi utilizado no projeto, caso necessite utilizar outro BD, é necessário alterar o `# DataBase` conforme necessário, do arquivo `settings.py`, que está dentro da pasta `config`.

A pasta `config` é onde estão os arquivos de configuração do Django.

## Executar Projeto

Para executar o projeto, é necessário abrir o terminal, e ir até a pasta do projeto `PEDIDOSLANCHONETE` e executar a linha de comando:

```sh
 python manage.py runserver
 ```
 
 Se der algum problema e não executar o seu projeto, será necessário informar a versão do Python que deseja executar:
 
 ```sh
 python3 manage.py runserver
 ```
 
Se não for especificado nenhuma porta, o projeto iniciará na porta padrão `8000`, caso queira, pode mudar a porta na hora de executar o projeto, no exemplo irei rodar o projeto na porta 8080:

```sh
 python manage.py runserver 8080
 ```
 
Após iniciar o projeto, o mesmo pode ser acessado via browser no endereço <a href="http://127.0.0.1:8000/">`http://127.0.0.1:8000/`</a> ou pelo ip do servidor web, que tiver hospedado.
