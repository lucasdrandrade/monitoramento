
import tkinter.scrolledtext as tkst
from tkinter import *
import json
from tkinter.filedialog import asksaveasfile
from tkinter.ttk import Combobox
from tkinter import messagebox

window = Tk()
window.geometry('380x320')
window.title('Conf File Setup')
path = 'C:/Users/ldg/Desktop/UFSC/EEL7802/monitoramento/projeto_monitoramento/dataBase/conf.json'

v1 = BooleanVar()


sensibility_intensity = ['Instrumental', 'Weak', 'Slight', 'Moderate', 'Rather Strong', 'Strong', 'Very Strong', 'Violent', 'Super Strong', 'Extreme']

def jSONfile(path, data):
        json.dump(data, path)

def submit_values():
	    
	#creating the dict that will be converted in the json file 
    data = {}
    
    #The defalt value is False | Fill the Showvideo field with any entry to get a True return

    show_video = v1.get()
    data['Show_video'] = show_video
	
    #Fill the Min_upload_seconds field with the time value in seconds
    min_upload_seconds = float(Min_upload_seconds.get())
    data['Min_upload_seconds'] = min_upload_seconds

    #Fill the Min_motion_frames field with a integer 
    min_motion_frames = int(Min_motion_frames.get()) 
    data['Min_motion_frames'] = min_motion_frames 

    #Fill the camera_warmup_time field with a float
    camera_warmup_time = float(Camera_warmup_time.get())
    data['Camera_warmup_time'] = camera_warmup_time

    #Fill the resolution field with 2 values
    resolution = list(Resolution.get())
    data['Resolution'] = resolution

    #Fill the fps field with a integer 
    fps = int(FPS.get()) 
    data['FPS'] = fps 

    #fill the sensibility field with a value from the intensity table as a string
    sensibility = Sensibility.get()  
    data['sensibility'] = sensibility

    #Converting to json
    File = [('JSON_File', '*.json')]
    File_Name='conf'
    File_position = asksaveasfile(filetypes = File, defaultextension = json, initialfile='conf', initialdir = path)
    jSONfile(File_position, data)

    return messagebox.showinfo('Status', 'Saved the info in as .json file')

button_submit = Button(window, text ="Submit", command=submit_values).grid(row=8, column=1)

#-----------------------------------------------------------------------------------------
show_video = Label(window, text="Show_video: (Select the option for True)")
show_video_True = Radiobutton(window, text="True | False", variable=v1, value=1).grid(row=0, column=1)

show_video.grid(row=0, column=0) 
#------------------------------------------------------------------------------------------------
min_upload_seconds = Label(window, text = "Min_upload_seconds:")
Min_upload_seconds = Entry(window)

min_upload_seconds.grid(row=1, column=0, padx=10, pady= 10) 
Min_upload_seconds.grid(row=1, column=1, padx=10, pady= 10)
#------------------------------------------------------------------------------------------
min_motion_frames = Label(window, text = "Min_motion_frames:")
Min_motion_frames = Entry(window)

min_motion_frames.grid(row=2, column=0, padx=10, pady= 10) 
Min_motion_frames.grid(row=2, column=1, padx=10, pady= 10)
#-----------------------------------------------------------------------------------------------
camera_warmup_time = Label(window, text = "Camera_warmup_time:")
Camera_warmup_time = Entry(window) 

camera_warmup_time.grid(row=3, column=0, padx=10, pady= 10)
Camera_warmup_time.grid(row=3, column=1, padx=10, pady= 10)
#----------------------------------------------------------------------------------------------
resolution = Label(window, text = "Resolution:")
Resolution = Entry(window) 

resolution.grid(row=6, column=0, padx=10, pady= 10)
Resolution.grid(row=6, column=1, padx=10, pady= 10)
#-------------------------------------------------------------------------------------------------
fps = Label(window, text = "FPS:")
FPS = Entry(window)

fps.grid(row=4, column=0, padx=10, pady= 10)
FPS.grid(row=4, column=1, padx=10, pady= 10)
#-------------------------------------------------------------------------------------------------
sensibility = Label(window, text = "Sensibility:")
Sensibility=Combobox(window, values=sensibility_intensity)

sensibility.grid(row=5, column=0, padx=10, pady= 10)
Sensibility.grid(row=5, column=1 , padx=10, pady= 10)
#-------------------------------------------------------------------------------------------------

window.mainloop()