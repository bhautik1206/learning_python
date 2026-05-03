from modules.todo import todo
from modules.weather import weather
from modules.news import newsFunction
from modules.password import passwordGeneration
command = input()

if command == "weather":
    weather()
elif "todo" in command:
    todo(command)
elif "news" in command : 
    newsFunction()
elif "password" in command:
    passwordGeneration(command)