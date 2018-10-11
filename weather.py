import requests, json
if __name__=='__main__':
    api_key = "18aefc39ee9dfc223aeb1eb917003656"
    city_name=input("Enter city name : ")
    url = "http://api.openweathermap.org/data/2.5/weather?appid=" + api_key + "&q="+city_name

    response = requests.get(url).json()

    if response["cod"] == 200:
        print("weather condition : "+response['weather'][0]['main'])
        print("temperature(in Celcius) : "+str(response['main']['temp']-273.15))
        print("humidity : "+str(response['main']['humidity'])+"%")
    elif response["message"] == "city not found":
        print("city not found")
    else:
        print("error occured")
