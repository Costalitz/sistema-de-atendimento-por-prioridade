# Foco deste projeto é a criação de um Sistema de Atendimento por Prioridade.

fila = []
contador_ordem = 0

def criar_solicitacao(cliente, problema, ordem_de_chegada):
    nivel_de_prioridade = {
        "software": 3,
        "hardware": 2,
        "consultoria": 1
    }

    solicitacao = {
        "cliente": cliente,
        "problema": problema,
        "nivel_de_prioridade": nivel_de_prioridade[problema],
        "ordem_de_chegada": ordem_de_chegada
    }

    return solicitacao

# função com condicional composta, que insere pelo nível de prioridade e desempata solicitações de mesmo nível pela ordem de chegada
def inserir_solicitacao(fila, solicitacao):
    if not fila:
        fila.append(solicitacao)
        return

    for i in range(len(fila)):
        fila_atual = fila[i]
        
        if solicitacao["nivel_de_prioridade"] > fila_atual["nivel_de_prioridade"]:
            fila.insert(i, solicitacao)
            return
        
        if (solicitacao["nivel_de_prioridade"] == fila_atual["nivel_de_prioridade"] and
              solicitacao["ordem_de_chegada"] < fila_atual["ordem_de_chegada"]):
            
            fila.insert(i, solicitacao)
            return
        
    fila.append(solicitacao)

# função que remove o primeiro elemento da fila
def atender_solicitacao(fila):
    if not fila:
        print("Não há solicitações na fila.")
        return None
    
    return fila.pop(0)