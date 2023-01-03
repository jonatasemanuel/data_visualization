from datetime import datetime
from matplotlib import pyplot as plt
import csv


# Obtém as temperaturas máximas do arquivo
filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], '%Y-%m-%d')
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            highs.append(row[1])
            dates.append(current_date)
            lows.append(low)

# Faz a plotagem dos dados
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.1)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
# Formata o gráfico
plt.title('Daily high and low temperatures, 2014\nDeath Valley, CA', fontsize=24)
plt.xlabel('', fontsize=12)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize=12)
plt.tick_params(axis='both', which='major', labelsize=12)
plt.show()

