#La tarea es preparar un código simple para evaluar o encontrar el tiempo final de un periodo de tiempo dado, expresándolo en horas y minutos. Las horas van de 0 a 23 y los minutes de 0 a 59. El resultado debe ser mostrado en la consola.#

#Por ejemplo, si el evento comienza a las 12:17 y dura 59 minutos, terminará a las 13:16.#

hora = int(input("Hora de inicio (horas): "))
min = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))
min = min + dura # encuentra el total de minutos
hora = hora + min // 60 # encuentra el número de horas ocultos en los minutos y actualiza las horas
min = min % 60 # corrige los minutos para que estén en un rango de (0..59)
hora = hora % 24 # corrige las horas para que estén en un rango de (0..23)
print(hora, ":", min, sep='')

20.12E8