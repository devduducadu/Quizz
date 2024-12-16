import time
from bd import lista_de_perguntas


for pergunta, opcoes, resposta_correta in lista_de_perguntas:

    print(pergunta)
    for i, opcao in enumerate(opcoes):
        print(f'{chr(65 + i)}. {opcao}')
    

    time.sleep(1)  

   
    resposta_usuario = input('Qual opção você acha que está correta? [digite uma letra.]: ').upper()

  
    if resposta_usuario == resposta_correta:
        print('Você acertou!!')
    else:
        print(f'Você errou... a resposta correta é {resposta_correta}. {opcoes[ord(resposta_correta) - 65]}\n')

print('Fim do quiz!')
