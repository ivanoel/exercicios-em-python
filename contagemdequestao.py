pontos = 0
questao = 1
while questao <= 3:
    resposta = input("Resposta da questão %d: " %questao)
    if questao == 1 and (resposta == 'b' or resposta == 'B'):
        pontos = pontos + 1
    if questao == 2 and (resposta == 'a' or resposta == 'A'):
        pontos = pontos + 1
    if questao == 3 and (resposta == 'd' or resposta == 'D'):
        pontos = pontos + 1
    questao += 1
    if questao == 0:
        break
print("O aluno fez %d pontos(s)"%pontos)
        
