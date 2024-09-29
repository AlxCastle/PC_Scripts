# Uso de la API de Have I been pwned con manejo de errores y creación de reportes
import requests
import json
import logging
import getpass
headers = {}
headers['content-type']= 'application/json'
headers['api-version']= '3'
headers['User-Agent']='python'

try: 
    key = getpass.getpass('Introduce la api-key: ') #key = ('ec1e2ebed1754f1b8c00f2b90aa15906') 
    headers['hibp-api-key']=key
    #Preguntar correo a revisar.
    email = input("Ingrese el correo a investigar: ")#'falso@hotmail.com'
    #solicitud.
    url = 'https://haveibeenpwned.com/api/v3/breachedaccount/'+email+'?truncateResponse=false'

    r = requests.get(url, headers=headers)
    
    #Devuelve un código de estado http.
    r.raise_for_status()  
    data = r.json()

    encontrados = len(data)
    if encontrados > 0:
        print("Los sitios en los que se ha filtrado el correo",email,"son:")
            
    else:
        print("El correo",email,"no ha sido filtrado")

    #Se guarda la informacion en un archivo txt.
    with open('reporteDeFiltraciones.txt', 'a') as file:  
        file.write(f"Los sitios en los que se ha filtrado el correo {email} son:")

        for filtracion in data:
            name = (f"Nombre: {filtracion['Name']}")
            domain = (f"Dominio: {filtracion['Domain']}")
            description = (f"Descripcion: {filtracion['Description']}")
            date = (f"Fecha en la que se registró la búsqueda en Have I Been Pwned: {filtracion['AddedDate']}")

            file.write(name)
            file.write(domain)
            file.write(date)
            file.write(description)

            #Imprimimos la informacion de la filtracion
            print(name)
            print(domain)
            print(date)
            print(description)

#Trata las respuestas con un status_code igual a 405, 500, etc. Es decir, si hay un error http.
except requests.exceptions.HTTPError:
    msg = r.text
    #print(msg) #finally
    logging.basicConfig(filename='hibpERROR.log',
                        format="%(asctime)s %(message)s",
                        datefmt="%m/%d/%Y %H:%M:%S",
                        level=logging.ERROR)
    logging.error(msg)

#Para cualquier error que tambien pudo ocurrir en la ejecucion. 
except Exception as err:
    msg = (f"Ocurrió un error inesperado: {err}")

else:
    msg = email+" Filtraciones encontradas: "+str(encontrados)
    #print(msg) #finally

    logging.basicConfig(filename='hibpINFO.log',
                        format="%(asctime)s %(message)s",
                        datefmt="%m/%d/%Y %I:%M:%S %p",
                        level=logging.INFO)
    logging.info(msg)

finally:
    print(msg)





