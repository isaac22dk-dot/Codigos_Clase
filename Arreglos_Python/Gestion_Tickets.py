tickets = [105, 102, 108, 101]
print(f"Estado inicial de la cola: {tickets}")

tickets.insert(0, 999)
print(tickets)
print(f"Tras recibir emergencia: {tickets}")

tickets.pop(3)
print(f"Tras cancelacion de 108: {tickets}")

tickets.sort()
tickets.sort(reverse=True)
print(f"Cola ordenada por prioridad: {tickets}")

print("--- Atencion ---")
print(f"Atendiendo al ticket ID {tickets.pop(0)}")
print(f"Cola pendiente actualizada: {tickets}")
