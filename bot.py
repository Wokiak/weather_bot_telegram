from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import json
import requests
TOKEN = 'ur own token'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
@dp.message_handler(commands=['start'])
async def on_message(message : types.Message):
	await bot.send_message(message.from_user.id,"Hello, enter your city name...")
@dp.message_handler(content_types=['text'])
async def on_message(message : types.Message):
	city = message.text
	api_key = '6515bb3582e8427298c0c38d2ada0508'
	defolt_url = "https://api.openweathermap.org/data/2.5/weather?"
	# city = str(input("Enter ur full city name: "))
	url = defolt_url + "q=" + city + "&units=metric" + "&appid=" + api_key
	response = requests.get(url)
	if response.status_code == 200:
	   data = response.json()   
	   main = data['main']
	   temperature = main['temp']  
	   humidity = main['humidity']  
	   pressure = main['pressure']  
	   report = data['weather']
	   print(f"{city:-^30}")
	   print(f"Temperature: {temperature}")
	   print(f"Humidity: {humidity}")
	   print(f"Pressure: {pressure}")
	   print(f"Weather Report: {report[0]['description']}")
	else: 
	   print("Error in the HTTP request")
	final_data = "Your city is : " + city + "\n" + f"Temperature: {temperature}" + "\n" + f"Humidity: {humidity}" + "\n"  + f"Pressure: {pressure}" + "\n" + f"Weather Report: {report[0]['description']}"	
	await bot.send_message(message.from_user.id, final_data )
if __name__ == '__main__':   
	executor.start_polling(dp)

