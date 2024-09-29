"""Erandy Yamileth Escaname Balderas
Maurilio Uriel Garcia Culebro
Alondra Castillo Gonzalez"""

import subprocess
import openpyxl

# Ejecutar el script de PowerShell
def ejecutar_powershell(script_path):
    # Cambiar la llamada para usar una lista
    result = subprocess.run([r"C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe", "-ExecutionPolicy", "Bypass", "-File", script_path], 
                            capture_output=True, text=True)
    return result.stdout

# Guardar datos en Excel
def guardar_en_excel(data, archivo_excel):
    # Crear un nuevo libro de Excel
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Servicios"

    # Leer la salida CSV y añadirla a la hoja
    for row in data.splitlines():
        ws.append(row.split(','))

    # Guardar el archivo
    wb.save(archivo_excel)

# Ruta del script de PowerShell, en este caso los archivos estaran en la misma carpeta desde donde se ejecuta el .py
script_powershell = ".\monitor_servicios.ps1"
# Ruta del archivo Excel de salida
archivo_excel = ".\Reporte_servicios.xlsx"

# Ejecutar el script de PowerShell y capturar la salida
salida = ejecutar_powershell(script_powershell)

# Guardar la salida en un archivo Excel
guardar_en_excel(salida, archivo_excel)

print(f"La información de los servicios ha sido guardada en {archivo_excel}")