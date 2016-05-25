f = open('jsonsnumaunicalinha.txt')

qtdChavesAbertas = 0

# Le 1 caracter (o primeiro) do arquivo
c = f.read(1)
while c:

	if c == '{':
		qtdChavesAbertas += 1
	elif c == '}':
		qtdChavesAbertas -= 1

	# [TODO] Escreve o caracter c na tela ou em um outro arquivo

	if qtdChavesAbertas == 0:
		print('Quebra a linha')
		# [TODO] Escreve a quebra de linha '\n' na tela ou em outro arquivo

	# Le mais 1 caractere (o proximo do arquivo)
	c = f.read(1)