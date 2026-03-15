import os
from pathlib import Path
import json


data_folder = Path("data")
file_to_open = data_folder / "task.json"

def todo(command):
    if "add" or "added" in command: 
        print("testing")
        try:
            with open(file_to_open, mode='r', encoding='utf-8') as file:
                file_data = json.load(file)
                print(
                max(file_data["id"]) 
                )
                print(file_data)
                add()
        except Exception as ex:
            print("Error is throwing:", ex)
    elif "remove" in command:
        try:
            with open(file_to_open, mode='r', encoding='utf-8') as file:
                file_data = json.load(file)
                print(
                max(file_data["id"]) 
                )
                print(file_data)
                add()
        except Exception as ex:
            print("Error is throwing:", ex)

def add():
    with open(file_to_open,mode='a',encoding='utf-8') as file:
        value = input("Enter the task : ")
        json.dump(value,file,indent=4)