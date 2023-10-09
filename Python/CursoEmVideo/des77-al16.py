palavras = ('carro', 'moto', 'caminhão', 'aprender', 'programar',  'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
for a in palavras:
    print(f'\nNa palavra "{a}" tem as seguintes vogais: ', end='')
    for b in a:
        if b.lower() in 'aeiou':
            print(f'{b}', end='   ')     