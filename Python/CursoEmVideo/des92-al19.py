'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o sálario. Caulcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar'''

from datetime import datetime
dados = dict()
dados['nome'] = input('Nome: ')
dados['nascimento'] = int(input('Data de nascimento [yyyy]: '))
dados['idade'] = datetime.now().year - dados['nascimento']
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contrato'] = int(input('Data de contratação [yyyy]: '))
    dados['salario'] = float(input('Salario: R$'))
dados['aposentadoria'] = (dados['idade'] + 35) - datetime.now().year
print(dados)