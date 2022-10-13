# Import Library
import requests
from datetime import datetime


cari_kota = input('Masukan Kota: ')
req_city = requests.get(
    url=f'https://api.myquran.com/v1/sholat/kota/cari/{cari_kota}')


datas = req_city.json()
city_data = datas['data']
print(city_data)
for index in range(len(city_data)):
    print(f'{index+1}. {city_data[index]["lokasi"]}')

city_kode = ''
pick_city = int(input('Pilih kota: '))
city_kode += city_data[pick_city-1]['id']


now = datetime.now()
current_date = now.strftime('%Y/%m/%d')

req_jadwal = requests.get(
    url=f'https://api.myquran.com/v1/sholat/jadwal/{city_kode}/{current_date}')

jadwal_datas = req_jadwal.json()
print(jadwal_datas['data']['jadwal'])
