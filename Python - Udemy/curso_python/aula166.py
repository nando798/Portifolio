# Usando calendar para calendários e datas
# https://docs.python.org/3/library/calendar.html
# calendar é usado para coisas genéricas de calendários e datas.
# Com calendar, você pode saber coisas como:
# - Qual o último dia do mês (ex.: monthrange)
# - Qual o nome e número do dia de determinada data (ex.: weekday)
# - Criar um calendário em si (ex.: monthcalendar)
# - Trabalhar com coisas específicas de calendários (ex.: calendar, month)
# Por padrão dia da semana começa em 0 até 6
# 0 = segunda-feira | 6 = domingo
import calendar
import locale

locale.setlocale(locale.LC_ALL, "")  # Define o locale para português do Brasil

print(calendar.calendar(2025))
print(calendar.monthrange(2025, 8))
print(list(enumerate(calendar.day_name)))
print(locale.getlocale(locale.LC_ALL))  # Verifica o locale atual

# primeiro_dia, ultimo_dia = calendar.monthrange(2025, 8)
# print(f"O primeiro dia do mês é {calendar.day_name[primeiro_dia]}")

# ultimo_dia_mes = calendar.weekday(2025, 8, ultimo_dia)
# print(f"O último dia do mês é {calendar.day_name[ultimo_dia_mes]}")


# for week in calendar.monthcalendar(2026, 8):
#     print(list(enumerate(week)))
