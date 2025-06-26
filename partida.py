class Partida:
    def __init__(self, jogador1, jogador2):
        self.turno = 1
        self.jogador1 = jogador1
        self.jogador2 = jogador2
        self.jogador_atual = jogador1

    def iniciar(self):
        print(f"Iniciando a partida entre {self.jogador1.nome} e {self.jogador2.nome}. \n")
        print(f"{self.jogador_atual.nome} começa! \n")
        
        while True: 
            self.informacoes1()
            self.informacoes2()
            
            print(f"É a vez do {self.jogador_atual.nome}. \n")
            print(f"1 - Usar uma carta")
            print(f"2 - Passar a vez")
            print(f"3 - Atacar")
            
            escolha = input()
            escolha = int(escolha)
            print(f"O jogador escolheu a opção {escolha}. \n")
            
            if escolha == 1: 
                print(f"O jogador escolheu usar uma carta. \n")
                self.jogador_atual.ver_cartas()

                if not self.jogador_atual.cartas:
                    print("Você não tem cartas disponíveis. \n")
                    continue

                escolha_carta = int(input("Qual carta deseja usar? \n")) 

                if 0 <- escolha_carta < len(self.jogador_atual.cartas):
                    carta = self.jogador_atual.cartas[escolha_carta]
                    alvo = self.jogador2 if self.jogador_atual == self.jogador1 else self.jogador1

                    try:
                        carta.usar_carta(personagem = self.jogador_atual, alvo = alvo)
                        self.jogador_atual.cartas.pop(escolha_carta)
                    except Exception as e:
                        print(f"Erro ao usar carta: {e}")

                else:
                    print("Carta inválida. \n")

                    
            elif escolha == 2:
                print("Você escolheu passar a vez.\n")

            elif escolha == 3:
                print("Você escolheu atacar.\n")
                self.jogador_atual.atacar(self.jogador2 if self.jogador_atual == self.jogador1 else self.jogador1)

            else:
                print("Opção inválida.\n")
                continue

            self.trocar_turno()
            
                        
    def trocar_turno(self):
        self.turno += 1
        self.trocar_jogador()
        print(f"Turno {self.turno}: Agora é o {self.jogador_atual.nome}.")
        
        if self.jogador1.vida_atual <= 0 or self.jogador2.vida_atual <= 0:
            self.acabar()
            
    def informacoes1(self):
        print("=" * 30)
        print(f"🔷 {self.jogador1.nome}")
        print(f"❤️ Vida:    {self.jogador1.vida_atual}/{self.jogador1.vida_maxima} {self.barra(self.jogador1.vida_atual, self.jogador1.vida_maxima)}")
        print(f"🛡️ Defesa:  {self.jogador1.defesa}")
        print(f"⚔️ Ataque:  {self.jogador1.ataque}")
        print(f"⚡ Energia: {self.jogador1.energia}/{self.jogador1.energia_maxima} {self.barra(self.jogador1.energia, self.jogador1.energia_maxima)}")
        print("=" * 30 + "\n")

    def informacoes2(self):
        print("=" * 30)
        print(f"🔶 {self.jogador2.nome}")
        print(f"❤️ Vida:    {self.jogador2.vida_atual}/{self.jogador2.vida_maxima} {self.barra(self.jogador2.vida_atual, self.jogador2.vida_maxima)}")
        print(f"🛡️ Defesa:  {self.jogador2.defesa}")
        print(f"⚔️ Ataque:  {self.jogador2.ataque}")
        print(f"⚡ Energia: {self.jogador2.energia}/{self.jogador2.energia_maxima} {self.barra(self.jogador2.energia, self.jogador2.energia_maxima)}")
        print("=" * 30 + "\n")
            
    def barra(self, atual, maxima, tamanho=20):
        proporcao = atual / maxima if maxima > 0 else 0  # Evita divisão por zero
        preenchido = int(tamanho * proporcao)
        vazio = tamanho - preenchido
        return f"[{'█' * preenchido}{'.' * vazio}]"


    def trocar_jogador(self):
        if self.jogador_atual == self.jogador1:
            self.jogador_atual = self.jogador2
        else:
            self.jogador_atual = self.jogador1
            
    def acabar(self):
        vencedor = self.jogador1 if self.jogador1.vida_atual > 0 else self.jogador2
        print(f"Fim de jogo! {vencedor.nome} venceu.")