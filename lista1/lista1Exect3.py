segundos_totais = int(input("Quantos segundos o evento tem?: "))


horas = (segundos_totais // 3600)
minutos = int((segundos_totais % 3600) / 60)
segundos = (segundos_totais % 3600) % 60

print(f"O evento tem {horas} horas, {minutos} minutos e {segundos} segundos!")