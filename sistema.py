# Projeto pré carnaval.
# Foco deste projeto é a criação de um Sistema de Atendimento por Prioridade.

fila = []
contador_ordem = 0
solicitacao = {}

def criar_solicitacao(cliente, problema, ordem_de_chegada):
    nivel_de_prioridade = {
        "software": 3,
        "hardware": 2,
        "duvida": 1
    }

    solicitacao = {
        "cliente": cliente,
        "problema": problema,
        "nivel_de_prioridade": nivel_de_prioridade[problema],
        "ordem_de_chegada": ordem_de_chegada
    }

    return solicitacao


def adicionar_solicitacao(fila, cliente, problema, nivel_de_prioridade, ordem_de_chegada):
    solicitacao = {
        "cliente": cliente,
        "problema": problema,
        "nivel_de_prioridade": nivel_de_prioridade,
        "ordem_de_chegada": ordem_de_chegada
        }
    
    fila.append(solicitacao)
    contador_ordem += 1


