class Processo:
    def __init__(self, nome):
        self.nome = nome
        self.relogio = 0

    def evento_interno(self):
        self.relogio += 1  # Regra 1
        print(f"{self.nome}: Evento interno, relógio = {self.relogio}")

    def enviar_mensagem(self, destinatario):
        self.relogio += 1  # Regra 1 antes de enviar
        timestamp = self.relogio
        print(f"{self.nome}: Envia mensagem para {destinatario.nome} com timestamp {timestamp}")
        destinatario.receber_mensagem(self, timestamp)

    def receber_mensagem(self, remetente, timestamp):
        self.relogio = max(self.relogio, timestamp)  # Ajusta relógio
        self.relogio += 1  # Regra 1 após ajuste
        print(f"{self.nome}: Recebe mensagem de {remetente.nome}, relógio = {self.relogio}")


# Criando os processos
P1 = Processo("P1")
P2 = Processo("P2")
P3 = Processo("P3")

# Simulando a sequência de eventos
print("\n--- Simulação de Relógios Lógicos de Lamport ---\n")

# 1. P1: Evento interno
P1.evento_interno()

# 2. P2: Envia mensagem para P3
P2.enviar_mensagem(P3)

# 3. P3: Recebe mensagem de P2
# (já feito dentro do método enviar_mensagem)

# 4. P1: Envia mensagem para P2
P1.enviar_mensagem(P2)

# 5. P3: Evento interno
P3.evento_interno()

# 6. P2: Recebe mensagem de P1
# (já feito dentro do método enviar_mensagem)

# 7. P2: Envia mensagem para P1
P2.enviar_mensagem(P1)

# 8. P1: Recebe mensagem de P2
# (já feito dentro do método enviar_mensagem)

print("\n--- Fim da Simulação ---\n")
