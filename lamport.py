numeroProcessos = int(input(('Digite o número de processos: ')))
numeroTempos = int(input(('Digite o numero de tempos dos processos: ')))

###### Matriz Dinâmica ######
process = []

for i in range(numeroProcessos):
    process.append([])
    for j in range(numeroTempos):
        process[i].append(j)

index = 0

###### Cria o primeiro processo padrão ######

for i in range(1):
    for j in range(numeroTempos):
        if i == 0 and j == 0:
            process[0][0] = 0
        if i != 0 or j != 0:
            process[i][j] = index
        index += 5

###### Cria os outros processos conforme a quantidade solicitada ######

diference = 0
diferenceStatus = 0

for i in range(numeroProcessos):
    if (i == 0):
        continue
    diference += 3
    diferenceStatus = 0
    for j in range(numeroTempos):
        if j == 0:
            process[i][j] = 0
        elif j == 1:
            process[i][j] = process[i-1][j] + 3
            diferenceStatus = process[i][j]
        else:
            process[i][j] = process[i][j-1] + diferenceStatus

###### Mostra os processos criados ######

for i in range(numeroProcessos):
    print('')
    print('Processo',i)
    for j in range(numeroTempos):
        print('[', process[i][j], ']', end="")
print('')
print('------------------------------------------------------------')

###### Recebe o indice de qual processo e tempo será utilizado ######

processoOrigem = int(input(('Digite o processo de origem: ')))
tempoOrigem = int(input(('Digite o tempo de origem: ')))
processoDestino = int(input(('Digite o processo de destino: ')))
tempoDestino = int(input(('Digite o tempo de destino: ')))

diference = process[processoDestino][1]

###### Valida se necessita sincronia nos processos e, caso necessário, sincroniza os processos ######

if (process[processoOrigem][tempoOrigem] > process[processoDestino][tempoDestino]):
    process[processoDestino][tempoDestino] = process[processoOrigem][tempoOrigem] + 1
    for i in range(tempoDestino + 1, numeroTempos):
        process[processoDestino][i] = process[processoDestino][i-1] + diference
    print('Sincronia Realizada com Sucesso: ', process[processoOrigem][tempoOrigem], '->', process[processoDestino][tempoDestino])
else:
    print('Sem Necessidade de Sincronia: ', process[processoOrigem][tempoOrigem], '->', process[processoDestino][tempoDestino])

print('Diferença: ', diference)

###### Mostra os processos após toda validação e, se feita, após toda sincronização ######

for i in range(numeroProcessos):
    print('')
    print('Processo',i)
    for j in range(numeroTempos):
        print('[', process[i][j], ']', end="")
print('')
print('------------------------------------------------------------')