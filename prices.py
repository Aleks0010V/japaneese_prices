import requests, time
from bs4 import BeautifulSoup

baseURL = 'https://www.numbeo.com/cost-of-living/in/'
cities = ['Chiba-Japan', 'Fukuoka', 'Hiroshima-Japan', 'Kawasaki-Japan', 'Kobe', 'Kyoto', 'Matsudo-Japan', 'Nagasaki-Japan', 'Nagoya', 'Okinawa', 'Osaka', 'Saitama-Japan', 'Sapporo', 'Sendai', 'Tokyo', 'Tsukuba-Japan', 'Yokohama', 'Yokosuka-Japan']
p = {'displayCurrency' : 'USD'}

for city in cities:
    time.sleep(0.25)
    url = f"{baseURL}{city}"
    r = requests.get(url, params=p)
    soup = BeautifulSoup(r.text, 'html.parser')
    table = soup.find('table',class_="data_wide_table")
    city_name = f"{soup.head.title.text.split()[-1]}.csv"
    handle = open(city_name, 'w')
    handle.write('Title,Price\n')
    print(city_name)
    for i in range(20, 58, 2):
        row = table.contents[i]
        row = f"{' '.join(row.contents[0].text.split(','))},{''.join(row.contents[2].text.split(','))}\n"
        handle.write(row)
    handle.close()
