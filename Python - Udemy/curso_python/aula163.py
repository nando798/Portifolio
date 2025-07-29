# datetime.timedelta e dateutil.relativetimedelta (calculando datas)
# Docs:
# https://dateutil.readthedocs.io/en/stable/relativedelta.html
# https://docs.python.org/3/library/datetime.html#timedelta-objects
from datetime import datetime
from dateutil.relativedelta import relativedelta  # Importe ZoneInfo


fmt = "%d/%m/%Y %H:%M:%S"
data_inicio = datetime.strptime("07/08/1984 09:30:30", fmt)
data_fim = datetime.strptime("17/07/2025 10:30:30", fmt)
delta = data_fim - data_inicio
# delta = timedelta(days=10, hours=5, minutes=30, seconds=20)
data = relativedelta(data_fim, data_inicio)
print(data)  # exibe a diferenca entre as datas
print(data.years, data.days)  # exibe a diferenca entre as datas


# print(data_fim + delta)
# print(data_fim + relativedelta(days=2, hours=2, minutes=40, seconds=10))
# print(delta.days, delta.seconds, delta.microseconds)
# print(delta.total_seconds())

# print(data_fim - data_inicio)  # Diferença entre as datas
# print(data_fim > data_inicio)
# print(data_fim < data_inicio)
# print(data_fim == data_inicio)

