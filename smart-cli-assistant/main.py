from modules.weather import weather
from modules.todo import todo
command = input()

if command == "weather":
    weather()
elif "todo" in command:
    todo(command)
