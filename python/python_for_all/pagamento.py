try:
    horas      = int(input("Horas: "))
    taxa      = float(input("Taxa: "))
    pagamento = float(input("Pagamento: "))

    if(horas > 40):
        horas_superiores = horas - 40
    else:
        horas_superiores = 0

    taxa_horas_superiores = taxa * 1.5


    pagamento_taxa_normal = horas * (taxa/100*pagamento)
    pagamento_taxa_superior = horas * (pagamento * taxa_horas_superiores/100)

    valor_pago = pagamento_taxa_normal + pagamento_taxa_superior

    print(f"Valor do Pagemnto: {valor_pago}")
except:
    print("Erro! Por favor, digite uma entrada númerica")