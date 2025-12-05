# Relogio_Lamport

## Relógio de Lamport

### Implementação simples do algoritmo de relógio lógico proposto por Leslie Lamport para ordenação parcial de eventos distribuídos.

## Sobre o Projeto

#### Este repositório contém uma implementação do Relógio de Lamport, um mecanismo lógico utilizado em sistemas distribuídos para determinar a ordem de eventos sem depender de relógios físicos.
#### Ele permite:

#### Atribuir timestamps lógicos a eventos.

#### Manter consistência causal entre processos.

#### Sincronizar mensagens entre processos simulados.

#### O objetivo é demonstrar o funcionamento do algoritmo de forma simples, didática e fácil de reutilizar.

## Como Funciona o Relógio de Lamport

#### Cada processo possui um contador lógico.
#### As regras básicas são:

#### Evento interno:
#### Incrementa o contador local.

#### Envio de mensagem:
#### Incrementa o contador local e envia-o junto com a mensagem.
