N = int(input('Digite o numero de itens que deseja ordenar: '))
qtd = input('Agora, digite os numeros desejados: ').split()[:N]

for i in range(len(qtd)):
  qtd[i] = int(qtd[i])
  
QTD = sorted(qtd)
print('Aqui está! ', *QTD)
