from random import randint
n = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print('-'*70)
for c in n:
    print(f'{c}',end=' ')
print(f'\nO maior número digitado foi {max(n)}.')
print(f'O menor número digitado foi {min(n)}.')
print('-'*70)