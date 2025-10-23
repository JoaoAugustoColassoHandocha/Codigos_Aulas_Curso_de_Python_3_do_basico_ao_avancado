'''
Ambientes virtuais em Python (venv)

* Um ambiente virtual carrega toda a sua instalação do Python para uma pasta no caminho escolhido.

* Ao ativar um ambiente virtual, a instalação do ambiente virtual será usada.

* venv é o módulo que vamos usar para criar ambientes virtuais.

* Você pode dar o nome que preferir para um ambiente virtual, mas os mais comuns são: venv env .venv .env

Obs: o ponto (.venv ou .env, deixa a pasta oculta)

- Executar o PowerShell como administrador
- set-executionpolicy unrestricted
- python -V (Verifica a versão do Python que será criado o venv)
- python -m venv NomeDoAmbienteVirtual (Executa a venv como um script) 

Após a criação, a pasta do venv terá:

- Include: Serve para armazenar arquivos de cabeçalho de pacotes Python que dependem de extensões escritas em C. 

- Lib: Tudo que será instalado de terceiros dentro do ambiente virtual, irá para a pasta

- Scripts: Tem todos os executáveis que for ser utilizado no ambiente virtual

'''