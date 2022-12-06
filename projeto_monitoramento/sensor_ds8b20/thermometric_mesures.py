import os
import glob
import time
import json 
 
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
 
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave' 

keys = ["Temperature_in_Celcius","Temperature_in_Farenheit"] 

def read_temp_raw():
    
    '''
    Função que faz a leitura dos sinais de dados raw do ds8b20.
    '''

    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp():

    '''
    Função que faz a leitura e conversão dos valores de temperaturas.
    '''

    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c, temp_f

def escrita_json(data, path='/home/pi/projetos/monitoramento/projeto_monitoramento/sensor_ds8b20/themometric_mesures.json'):
    '''
    Função que faz a escrita do arquivo de temperaturas.
    '''
    with open(path, 'w', encoding='utf-8') as outfile:
        outfile.write(data)

while True:

    thermometric_mesures = read_temp() 
    temperature_celcius = thermometric_mesures[0] 
    temperature_farenheit = thermometric_mesures[1] 

    values = [temperature_celcius, temperature_farenheit]
    
    thermo_dict = dict(zip(keys, values))
    
    # Serializing json
    json_object = json.dumps(thermo_dict, indent=4)
    
    escrita_json(json_object)

    #print(f"Essa é a temperatura medida pelo ds8b20 em ºC {temperature_celcius}")
    #print(f"Essa é a temperatura medida pelo ds8b20 em ºF {temperature_farenheit}")   
    print(thermo_dict)
    #print(type(thermo_dict))
    time.sleep(1)
