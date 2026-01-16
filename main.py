# main.py
# Projeto: Controle de Prazos de Migração com Datas
# Autor: Luana Andia da Costa

from datetime import datetime

def calcular_dias(data_inicio, data_fim):
    """Calcula a diferença de dias entre duas datas"""
    delta = data_fim - data_inicio
    return delta.days

def migracao_sem_adequacao():
    prazo_total = 180
    prazo_envio_max = 30
    etapas_internas = 30
    prazo_ccee = 30
    tempo_minimo_necessario = etapas_internas + prazo_ccee

    try:
        data_envio_str = input("Data de envio da documentação (dd/mm/aaaa): ")
        data_envio = datetime.strptime(data_envio_str, "%d/%m/%Y")
        data_inicio = datetime.today()
        dias_envio_docs = calcular_dias(data_inicio, data_envio)
    except ValueError:
        print("❌ Formato de data inválido!")
        return

    dias_restantes = prazo_total - dias_envio_docs

    if dias_envio_docs > prazo_envio_max:
        print("❌ Documentação enviada fora do prazo inicial.")
    elif dias_restantes > tempo_minimo_necessario + 30:
        print("✅ Migração sem adequação adiantada.")
    elif dias_restantes >= tempo_minimo_necessario:
        print("⚠️ Migração sem adequação no limite do prazo.")
    else:
        print("❌ Migração sem adequação fora do prazo.")

def migracao_com_adequacao():
    prazo_total = 180
    envio_docs = 30
    prazo_max_adequacao = 120
    etapas_internas = 30

    try:
        data_inicio_str = input("Data de início da adequação (dd/mm/aaaa): ")
        data_fim_str = input("Data de fim da adequação (dd/mm/aaaa): ")
        data_inicio = datetime.strptime(data_inicio_str, "%d/%m/%Y")
        data_fim = datetime.strptime(data_fim_str, "%d/%m/%Y")
        dias_adequacao = calcular_dias(data_inicio, data_fim)
    except ValueError:
        print("❌ Formato de data inválido!")
        return

    tempo_total_usado = envio_docs + dias_adequacao + etapas_internas

    if dias_adequacao < prazo_max_adequacao:
        sobra = prazo_total - tempo_total_usado
        print(f"✅ Adequação concluída com antecedência. Sobram {sobra} dias.")
    elif dias_adequacao == prazo_max_adequacao:
        print("⚠️ Adequação no limite. Migração possível, porém apertada.")
    else:
        print("❌ Adequação atrasada. Migração fora do prazo.")

def menu():
    while True:
        print("\n=== CONTROLE DE PRAZOS DE MIGRAÇÃO ===")
        print("1 - Migração sem adequação")
        print("2 - Migração com adequação")
        print("3 - Sair")

        opcao = input("Escolha uma opção (1, 2 ou 3): ")

        if opcao == "1":
            migracao_sem_adequacao()
        elif opcao == "2":
            migracao_com_adequacao()
        elif opcao == "3":
            print("Saindo do programa...")
            break
        else:
            print("❌ Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()

