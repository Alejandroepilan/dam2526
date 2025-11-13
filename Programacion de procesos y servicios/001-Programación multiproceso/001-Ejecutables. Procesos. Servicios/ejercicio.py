numero = 1.0000000098
multiplicador = 1.0000000000654

print("Empiezo")

for i in range(0, 1000000000):
  if i % 10000 == 0:
    numero *= multiplicador
    print(f"Iteración {i} -> numero = {numero}")

print("Acabo")
print("Valor final:", numero)
