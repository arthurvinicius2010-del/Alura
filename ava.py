# Capacidade do bondinho
capacidade = 30

# Número fixo de professores
professores = 8

# Entradas do usuário
numero_de_alunos = int(input("Digite a quantidade de alunos: "))
numero_de_monitores = int(input("Digite a quantidade de monitores: "))

# Mensagens
resposta_positiva = "pode ir"
resposta_negativa = "não pode ir"

# Cálculo do total de pessoas
total = numero_de_alunos + numero_de_monitores + professores

# Estrutura condicional
if total <= capacidade:
    print(resposta_positiva)
else:
    print(resposta_negativa)