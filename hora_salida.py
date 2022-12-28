from datetime import datetime
import time

formato = "%H:%M:%S"

hoy = datetime.now()
s_hoy = datetime.strftime(hoy, formato)
print(f"Hora actual: {s_hoy}")

hora_salida = "19:00:00"
print(f"Hora de salida: {hora_salida}")

f_hoy = datetime.strptime(s_hoy, formato)
f_hora_salida = datetime.strptime(hora_salida, formato)


resto_horas = f_hora_salida - f_hoy
print(f"Horas restantes: {resto_horas}")

if f_hoy < f_hora_salida:
    print(f"Tienes que seguir trabajando. Que quedan {resto_horas} en la oficina")
else:
    print("Ya deberías estar fuera")
