"""
Formatando datas do datetime
datetime.strftime('FORMATO', 'DATA')
https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
"""

from datetime import datetime

fmt = "%d/%m/%Y"
data = datetime.strptime("1984-8-7 8:29:57", "%Y-%m-%d %H:%M:%S")
print(data.strftime("%d/%m/%Y"))  # Formata a data para o formato especificado
print(data.strftime("%d/%m/%Y %H:%M"))  # Formata a data para o formato especificado
print(data.strftime("%d/%m/%Y %H:%M:%S"))  # Formata a data para o formato especificado
print(data.strftime("%Y"))  # Formata a data para o formato especificado
print((data.strftime("%Y"), data.year))  # Formata a data para o formato especificado
print((data.strftime("%m"), data.month))  # Formata a data para o formato especificado
print((data.strftime("%d"), data.day))  # Formata a data para o formato especificado
print((data.strftime("%H"), data.hour))  # Formata a data para o formato especificado
print((data.strftime("%M"), data.minute))  # Formata a data para o formato especificado
# Formata a data para o formato especificado
