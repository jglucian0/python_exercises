# Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai
# retornar um dicionário com as seguintes informações:
#– Quantidade de notas              
#– A maior nota                   
#– A menor nota                                                                                                                                              
#– A média da turma                                       
#– A situação (opcional)

def notas(*notas, sit=False):
  resultado = dict()
  resultado['total'] = len(notas)
  resultado['maior'] = max(notas)
  resultado['menor'] = min(notas)
  resultado['media'] = sum(notas) / len(notas)
  
  if sit == True:
    if resultado['media'] >= 7:
      resultado['situação'] = 'BOA'
    elif resultado['media'] >= 5:
      resultado['situação'] = 'MEDIANA'
    else:
      resultado['situação'] = 'RUIM'
  
  return resultado

resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)