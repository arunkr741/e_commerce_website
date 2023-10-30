from django.shortcuts import render
import requests
def contriesHome(request):
    api_url = 'https://restcountries.com/v3.1/all'
    response = requests.get(api_url)

    data = {}
    region = set()
    if response.status_code == 200:
        data = response.json()
        if len(data):
            for item in data:
                region.add(item["region"])

    return render(request, 'countriesData.html',{"contries_data":data,"regions": region})

def country_details(request, country_name):
    api_url = 'https://restcountries.com/v3.1/name/' + country_name
    response = requests.get(api_url)
    data = []
    native_names = []
    currencies = []
    if response.status_code == 200:
        data = response.json()
        if data[0]:
            for native_name in data[0]['name']['nativeName'].values():
                native_names.append(native_name['common'])
            for currency in data[0]['currencies'].values():
                currencies.append(currency['name'])
                currencies.append(currency['symbol'])
    return render(request, 'country_details.html', {'country': data[0], 'native_names':native_names, 'currencies':currencies})
