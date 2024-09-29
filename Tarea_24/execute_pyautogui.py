"""Ejercicio: Convertir un Script de Python con PyAutoGUI a un Ejecutable con py2exe.
-Ajuntar explicación de lo que realiza el archivo setup.py""""

import datetime
import subprocess
import pyautogui

try:
    #fecha y hora
    date_time = datetime.datetime.now()
    dt_format = date_time.strftime("%Y-%m-%d_%H-%M")
    
    #toma de screenshot
    pyautogui.screenshot('{}.png'.format(dt_format))
    
    #reporte de procesos
    result = subprocess.run(
        ["tasklist"],
        capture_output=True,
        text=True,
        shell=True
    )   
       
    if result.returncode == 0:
        #creación del .txt
        with open('report_process_{}.txt'.format(dt_format), 'a') as file:
            file.write(result.stdout)
    else:
        print(f"Error al solicitar los procesos.")

except Exception as error:
    print(f'Ha ocurrido un error: {error}')
