# Projeto pré carnaval.
# Foco deste projeto é a criação de um Sistema de Atendimento por Prioridade.

fila = []
contador_ordem = 0

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


def inserir_solicitacao(fila, solicitacao):
    if not fila:
        fila.append(solicitacao)
        return

    for i in range(len(fila)):
        fila_atual = fila[i]
        
        if solicitacao["nivel_de_prioridade"] > fila_atual["nivel_de_prioridade"]:
            fila.insert(i, solicitacao)
            return
        
        elif (solicitacao["nivel_de_prioridade"] == fila_atual["nivel_de_prioridade"] and
              solicitacao["ordem_de_chegada"] < fila_atual["ordem_de_chegada"]):
            
            fila.insert(i, solicitacao)
            return
        
    fila.append(solicitacao)
def atender_solicitacao(fila):
    if not fila:
        print("Não há solicitações a fila.")
        return None
    
    return fila.pop(0)

soli1 = criar_solicitacao('Carlos', 'software', contador_ordem)
contador_ordem += 1
inserir_solicitacao(fila, soli1)

soli2 = criar_solicitacao('Ana', 'hardware', contador_ordem)
contador_ordem += 1
inserir_solicitacao(fila, soli2)

soli3 = criar_solicitacao('Beatriz', 'duvida', contador_ordem)
contador_ordem += 1
inserir_solicitacao(fila, soli3)

