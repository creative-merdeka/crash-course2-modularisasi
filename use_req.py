import requests                                         #pip package

url = 'https://detik.com'                                                          #menggunakan syn variable url
try:                                                                               #utk mencari erorr script d atas
    response = requests.get(url)                                                   #python akan me return fungsi url
    if response.status_code == 200 :
        print(f'Succes! Response = {response.status_code}')                      #menampilkan data respon erorr code
        print(f'\nContent {response.text}')                                          #menapilkan data .txt(doctype html)
    else:
        print(f'ups ono sing sembrono req {response.status_code}')
except Exception as e:                                  #output dari try
    print(f'iki biang e masalah{e}')
print('\nprog rampung')