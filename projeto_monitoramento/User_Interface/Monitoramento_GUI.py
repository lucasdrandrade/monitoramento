import json

import datetime 

import tkinter.scrolledtext as tkst
from tkinter import *
from tkinter.filedialog import asksaveasfile
from tkinter.ttk import Combobox
from tkinter import messagebox

# -------------------------------------------------------------------------------------------------------------------------------- 

#load the configs of the json file in the conf variable
sensor_data = open('C:/Users/ldg/Desktop/UFSC/EEL7802/monitoramento/projeto_monitoramento/dataBase/sensor_data.json')

#loading the time variable
now = datetime.datetime.now()

data = json.load(sensor_data)
temperatura_sensor = data['Temperature']
umidade_sensor = data['Humidity']

string_dateTime_temperature = (f"{temperatura_sensor} | {now}") 
string_dateTime_humidity = (f"{umidade_sensor} | {now}") 

# -------------------------------------------------------------------------------------------------------------------------------- 

window = Tk()
window.geometry('580x160')
window.title('Projeto Monitoramento')

label = Label(window, text='Projeto Monitoramento')
label.grid(row=0, column=1, padx=10, pady=10) 

temperature = Label(window, text = "Temperatura Ambiente | Date Time:")
Ttemperature = Label(window, text= string_dateTime_temperature)

temperature.grid(row=1, column=0, padx=10, pady= 10) 
Ttemperature.grid(row=1, column=1, padx=10, pady= 10)

humidity = Label(window, text = "Úmidade Ambiente | Date Time:")
Hhumidity = Label(window, text= string_dateTime_humidity)

humidity.grid(row=2, column=0, padx=10, pady= 10) 
Hhumidity.grid(row=2, column=1, padx=10, pady= 10)

window.mainloop()