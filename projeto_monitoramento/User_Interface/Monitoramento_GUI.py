import json

import datetime 

import tkinter.scrolledtext as tkst
from tkinter import *
from tkinter.filedialog import asksaveasfile
from tkinter.ttk import Combobox
from tkinter import messagebox

# -------------------------------------------------------------------------------------------------------------------------------- 

#load the configs of the json file in the conf variable
sensor_data = open('C:/Users/ldg/Desktop/UFSC/EEL7802/monitoramento/projeto_monitoramento/dataBase/Themometric_mesures.json')

#loading the time variable
now = datetime.datetime.now()

data = json.load(sensor_data)
temperatura_sensor_celcius = data['Temperature_in_Celcius']
temperatura_sensor_farenheit = data['Temperature_in_Farenheit']

string_dateTime_temperature_Celcius = (f"{temperatura_sensor_celcius} | {now}") 
string_dateTime_temperature_Farenheit = (f"{temperatura_sensor_farenheit} | {now}") 

# -------------------------------------------------------------------------------------------------------------------------------- 
while True: 
    window = Tk()
    window.geometry('580x160')
    window.title('Projeto Monitoramento')
    
    label = Label(window, text='Projeto Monitoramento')
    label.grid(row=0, column=1, padx=10, pady=10) 
    
    temperature = Label(window, text = "Temperatura Ambiente ºC | Date Time:")
    Ttemperature = Label(window, text= string_dateTime_temperature_Celcius)
    
    temperature.grid(row=1, column=0, padx=10, pady= 10) 
    Ttemperature.grid(row=1, column=1, padx=10, pady= 10)
    
    humidity = Label(window, text = "Temperatura Ambiente ºF | Date Time:")
    Hhumidity = Label(window, text= string_dateTime_temperature_Farenheit)
    
    humidity.grid(row=2, column=0, padx=10, pady= 10) 
    Hhumidity.grid(row=2, column=1, padx=10, pady= 10)
    
    window.mainloop()