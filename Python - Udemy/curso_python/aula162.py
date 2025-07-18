# Criando datas com módulo datetime
# datetime(ano, mês, dia)
# datetime(ano, mês, dia, horas, minutos, segundos)
# datetime.strptime('DATA', 'FORMATO')
# datetime.now()
# https://pt.wikipedia.org/wiki/Era_Unix
# datetime.fromtimestamp(Unix Timestamp)
# https://docs.python.org/3/library/datetime.html
# Para timezones
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# Instalando o pytz
# pip install pytz types-pytz

# from datetime import datetime
# from zoneinfo import zoneinfo

# # data_str = "11/07/2025"
# # data_fmt = "%d/%m/%Y"

# # data = datetime.strptime(data_str, data_fmt)
# # print(data)


# data = zoneinfo("America/Sao_Paulo")
# data2 = datetime.now()

# print(data)
# print(data2)

from datetime import datetime
from zoneinfo import ZoneInfo
from dateutil.relativedelta import relativedelta  # Importe ZoneInfo

# Crie o objeto de fuso horário
tz_sp = ZoneInfo("Asia/Tokyo")
aware_dt = datetime.now()  # Adicione o parâmetro tz
print(aware_dt.timestamp())
print(datetime.fromtimestamp(1752786663))
print(datetime.relativedelta(seconds=60, minutes=14))
# Você pode criar o datetime já com o fuso horário correto


# print(f"Horário com zoneinfo: {aware_dt}")
# print(f"Fuso horário: {aware_dt.tzinfo}")
