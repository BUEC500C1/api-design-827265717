import requests

def weather_report(location):
    try:
        appid = 'f9d6395b1ce7e2196e30897f4205606e'
        url = 'https://api.openweathermap.org/data/2.5/weather?q=' + location + '&APPID=' + appid
        data = requests.get(url).json()
        country = data['sys']['country']
        main = data['weather'][0]['main']
        description = data['weather'][0]['description']
        temperature = data['main']['temp']
        feels_like = data['main']['feels_like']
        pressure = data['main']['pressure']
        print('Here is the information: ')
        print('country: ', country)
        print('main weather: ', main)
        print('description: ', description)
        print('temperature: ', temperature)
        print('feels_like: ', feels_like)
        print('pressure: ', pressure)
    except:
        print('input error')

def main():
    print('Please enter the city you will take a flight:')
    user_input = input('city name: ')
    print('===============================================')
    weather_report(user_input)

if __name__ == '__main__':
        main()