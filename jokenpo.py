#pedra-1 papel-2 tesoura-3

#funcao para retornar o que os jogadores digitaram
def jogada(jogada):
	if jogada == 1:
		return "PEDRA"
	elif jogada == 2:
		return "PAPEL"
	return "TESOURA"
	
#funcao para sortear a jogada da maquina
def aleatorio():
	from random import randint
	x = randint(1,3)
	return x


#funcao que retorna quem ganhou
def jogo(jog1,jog2):
    if jog1 == jog2:
        return True
    elif (jog1 == 1 and jog2 == 3) or (jog1 == 3 and jog2 == 2) or (jog1 == 2 and jog2 == 1):
        return True
    return False


#funcao principal
def main():
	#blibioteca do python para importar comandos do sistema
	import os
	
	cont = 1
	voce = 0
	maquina = 0
	vencedor = ""
	jogadas=0
	validaVecendor=False
	continuar = 1
	
	while cont <=6:
		
		#valida o fim do jogo
		if cont == 6:
			validaVecendor = True
			cont -= 1
		
		#limpa a tela	
		os.system("clear")
		#os.system("cls")
				
		print "# JOKENPO #"
		print "Voce: "+str(voce)+" | "+"PC: "+str(maquina)
		print "round: "+str(cont)+" | "+"5"
		print ""
		print "1-PEDRA"
		print "2-PAPEL"
		print "3-TESOURA"
						
		# mostra na tela o que os jogadores jogaram
		if jogadas!=0:
			print "Voce jogou "+jogada(jogador1)+" e o PC "+jogada(jogador2)
			print vencedor
		
		#verifca se o jogo acabou		
		if cont == 5 and validaVecendor == True:
			
					
			print""
			print"PLACAR FINAL"
			print"Voce: "+str(voce)+" | "+"PC: "+str(maquina)
			print""
			print"JOGAR NOVAMENTE?"
			print"1-SIM"
			print"2-NAO"
			
			#verifica se o usuario vai continuar ou nao
			continuar = input()
			if continuar == 1:
				main()
                
		#acao para parar jogo caso o usuario nao queria continuar
		if continuar == 2:
			cont = 10
			break
		
		#entrada dos jogadores
		jogador1 = input()
		jogador2 = aleatorio()

		#verifica quem venceu e contabiliza vitorias
		if  jogo(jogador1,jogador2) and jogo(jogador2,jogador1):
			vencedor= "Ninguem Ganhou"
			jogadas += 1
		elif jogo(jogador1,jogador2) == True and jogo(jogador2,jogador1) == False:
			vencedor= "Voce GANHOU!!!"
			voce += 1
			cont += 1
			jogadas += 1
		else:
			vencedor= "O PC GANHOU!!!"
			maquina += 1
			cont += 1
			jogadas += 1

#chamando funcao principal1
main()



