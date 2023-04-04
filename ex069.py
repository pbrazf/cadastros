# cadastros
cmulher20 = chomem = cidade = 0
while True:
    print('-' * 20)
    print('CADASTRE UMA PESSOA')
    print('-' * 20)
    idade = int(input('idade: '))
    sexo = ''
    while sexo not in 'MF':
        sexo = str(input('sexo: [F/M] ')).strip().upper()[0]
    if idade > 18:
        cidade += 1
    if sexo == 'M':
        chomem += 1
    if sexo == 'F':
        if idade < 20:
            cmulher20 += 1
    print('-' * 25)
    continuar = ''
    while continuar not in 'SN':
        continuar = str(input('deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('\n')
print('FIM DO PROGRAMA')
print('------------------------->')
print(f'''total de pessoas com mais de 18 anos: {cidade}
total de homens cadastrados: {chomem}
total de mulheres com menos de 20 anos: {cmulher20}''')

