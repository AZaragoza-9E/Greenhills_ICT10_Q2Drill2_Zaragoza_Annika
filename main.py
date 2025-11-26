# Working with Dictionaries
from pyscript import display


weather_fortoday = {
    "location" : "Manila",
    "temperature_c" : 32,
    "humidity" : 70,
    "condition" : "Sunny",
}

weather_fortoday['condition'] = 'Cloudy'
weather_fortoday['heat_index'] = 38  

display(weather_fortoday, target='weather')

display(f'We are currently in {weather_fortoday['location']}.', target='weather')
display(f'The temperature is currently {weather_fortoday['temperature_c']}°C.', target='weather')
display(f'The humidity is {weather_fortoday['humidity']}%.', target='weather')
display(f'The weather was mostly cloudy but is now {weather_fortoday['condition']}.', target='weather')

display(f'The heat index is {weather_fortoday['heat_index']}.', target='weather')
