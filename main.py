from datetime import datetime

# Prazos adicionais
ETAPAS_INTERNAS = 30
PRAZO_CCEE = 30

def calcular_dias(data_inicio, data_fim):
    """Retorna a diferença em dias entre duas datas."""
    return (data_fim - data_inicio).days

def mostrar_explicacao(dias_sobrando):
    """Mostra se dá tempo para as etapas internas e prazo CCEE."""
    total_necessario = ETAPAS_INTERNAS + PRAZO_CCEE

    if dias_sobrando >= total_necessario:
        print(f"✅ Faltam {dias_sobrando} dias até o prazo final da migração.")
        print(f"👍 Com {dias_sobrando} dias, dará tempo para:")
        print(f"- Etapas internas: {ETAPAS_INTERNAS} dias")
        print(f"- Prazo CCEE: {PRAZO_CCEE} dias")
        print("Tudo dentro do prazo!\n")
    elif dias_sobrando >= 0:
        print(f"⚠️ Faltam apenas {dias_sobrando} dias até o prazo final da migração!")
        print(f"Pode não ser suficiente para concluir:")
        if dias_sobrando < ETAPAS_INTERNAS:
            print(f"- Etapas internas (faltam {ETAPAS_INTERNAS - dias_sobrando} dias)")
            print(f"- Prazo CCEE: {PRAZO_CCEE} dias")
        else:
            print(f"- Etapas internas: {ETAPAS_INTERNAS} dias")
            print(f"- Prazo CCEE (faltam {PRAZO_CCEE - (dias_sobrando - ETAPAS_INTERNAS)} dias)")
        print()
    else:
        print("❌ Prazo estourado! A ação ocorreu após o prazo final da migração.\n")

def pedir_data(mensagem):
    """Pede a data do usuário até que seja válida."""
    while True:
        try:
            data_str = input(mensagem).strip()
            data = datetime.strptime(data_str, "%d/%m/%Y")
            return data
        except ValueError:
            print("Formato inválido! Use dd/mm/aaaa, por exemplo 01/03/2026.")

def main():
    # Passo 1: datas iniciais
    print("=== VERIFICAÇÃO DE PRAZOS ===")
    data_aceite_denuncia = pedir_data("Data do aceite da denúncia (dd/mm/aaaa): ")
    data_migracao = pedir_data("Data prevista de conclusão da migração (dd/mm/aaaa): ")

    if data_migracao <= data_aceite_denuncia:
        print("❌ A data prevista da migração deve ser após o aceite da denúncia.")
        return

    print(f"\nO aceite da denúncia ocorreu em {data_aceite_denuncia.strftime('%d/%m/%Y')}.")
    print(f"A migração está prevista para ocorrer em {data_migracao.strftime('%d/%m/%Y')}.\n")

    # Menu principal
    while True:
        print("=== VERIFICAÇÃO DE PRAZOS DE MIGRAÇÃO ===")
        print("1 - Migração sem adequação")
        print("2 - Migração com adequação")
        print("3 - Sair")
        
        opcao = input("Escolha uma opção (1, 2 ou 3): ").strip()
        
        if opcao == "1":
            # Migração sem adequação
            data_envio = pedir_data("Data de envio da documentação inicial (dd/mm/aaaa): ")
            dias_sobrando = calcular_dias(data_envio, data_migracao)
            if dias_sobrando < 0:
                print("❌ A documentação foi enviada após o prazo final da migração!\n")
            else:
                print("✅ Migração sem adequação adiantada.")
                mostrar_explicacao(dias_sobrando)

        elif opcao == "2":
            # Migração com adequação
            data_inicio_adequacao = pedir_data("Data de início da adequação (dd/mm/aaaa): ")
            data_fim_adequacao = pedir_data("Data de fim da adequação (dd/mm/aaaa): ")
            
            if data_fim_adequacao > data_migracao:
                print("❌ A adequação termina após o prazo final da migração!\n")
            else:
                dias_sobrando = calcular_dias(data_fim_adequacao, data_migracao)
                print("✅ Adequação concluída dentro do prazo." if dias_sobrando >=0 else "❌ Adequação atrasada!")
                mostrar_explicacao(dias_sobrando)

        elif opcao == "3":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida! Escolha 1, 2 ou 3.\n")

if __name__ == "__main__":
    main()