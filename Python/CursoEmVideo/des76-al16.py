produtos = ('Lápis', 1.75, 'Borracaha', 2, 'Caderno', 15.9, 'Estojo', 25, 'Transferidor', 4.2, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.3, 'Livro', 34.9 )
print('-'*50)
print(f'{"L I S T A G E M   DE   P R E Ç O S":^50}')
print('-'*50)
for c in range (0,len(produtos)):
    if c % 2 == 0:
        print(f'{produtos[c]:.<40}',end='R$')
    else:
        print(f'{produtos[c]:>7.2f}')
print('-'*50)