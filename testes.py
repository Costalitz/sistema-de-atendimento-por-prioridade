from sistema import(
    criar_solicitacao,
    inserir_solicitacao,
    atender_solicitacao
)

def main():
    fila = []
    contador_ordem = 0

    dados = [
        ('Carlos', 'software'),
        ('Ana', 'hardware'),
        ('Beatriz', 'consultoria'),
        ('Daniel', 'software'),
        ('Eduardo', 'hardware'),
        ('Alexandra', 'consultoria'),
        ('João', 'consultoria')
    ]

    for cliente, problema in dados:
        solicitacao = criar_solicitacao(cliente, problema, contador_ordem)
        contador_ordem += 1
        inserir_solicitacao(fila, solicitacao)

    print("Fila inicial:")
    for s in fila:
        print(s)
    
    print('\nAtendimentos:')
    while fila:
        atendida = atender_solicitacao(fila)
        print(f"Atendendo: {atendida} - {atendida['problema']}")