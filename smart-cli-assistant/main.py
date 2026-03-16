from modules.todo import todo
from modules.weather import weather
command = input()

if command == "weather":
    weather()
elif "todo" in command:
    todo(command)
