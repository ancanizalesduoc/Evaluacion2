import urllib.parse
import requests

# URL base de la API de GraphHopper
service_url = "https://graphhopper.com/api/1/route?"
# Coloca aquí tu clave/token de GraphHopper
key = "6e49a0da-8c8b-431a-9bc7-91963cece536"  

def geocoding(location, key):
    while location == "":
        location = input("Por favor, ingrese una ubicación válida: ")
    
    geocode_url = "https://graphhopper.com/api/1/geocode?"
    url = geocode_url + urllib.parse.urlencode({"q": location, "limit": "1", "key": key})
    
    reply = requests.get(url)
    json_data = reply.json()
    json_status = reply.status_code
    
    if json_status == 200 and len(json_data["hits"]) != 0:
        lat = json_data["hits"][0]["point"]["lat"]
        lng = json_data["hits"][0]["point"]["lng"]
        name = json_data["hits"][0]["name"]
        value = json_data["hits"][0]["osm_value"]
        
        if "street" in json_data["hits"][0]:
            street = json_data["hits"][0]["street"]
        else:
            street = ""
            
        if "state" in json_data["hits"][0]:
            state = json_data["hits"][0]["state"]
        else:
            state = ""
            
        if "country" in json_data["hits"][0]:
            country = json_data["hits"][0]["country"]
        else:
            country = ""
            
        new_location = f"{name}, {street}, {state}, {country}".replace(", ,", ",")
        print(f"URL de la API de Geocodificación para {new_location} (Código de estado: {json_status})\n{url}")
        return json_status, lat, lng, new_location
    else:
        print(f"No se encontraron resultados para la ubicación: {location}")
        return json_status, None, None, location

while True:
    print("\n-------------------------------------------------")
    print("      Sistema de Geolocalización de Rutas        ")
    print("-------------------------------------------------")
    
    loc1 = input("Ingrese la ubicación de origen (o escriba 's' / 'salir' para finalizar): ")
    if loc1.lower() in ["s", "salir"]:
        print("¡Gracias por utilizar el servicio de geolocalización! Hasta luego.")
        break
        
    loc2 = input("Ingrese la ubicación de destino (o escriba 's' / 'salir' para finalizar): ")
    if loc2.lower() in ["s", "salir"]:
        print("¡Gracias por utilizar el servicio de geolocalización! Hasta luego.")
        break

    status1, lat1, lng1, new_loc1 = geocoding(loc1, key)
    status2, lat2, lng2, new_loc2 = geocoding(loc2, key)

    if status1 == 200 and status2 == 200 and lat1 is not None and lat2 is not None:
        op_url = f"{service_url}point={lat1},{lng1}&point={lat2},{lng2}&vehicle=car&locale=es&key={key}"
        reply = requests.get(op_url)
        json_status = reply.status_code
        json_data = reply.json()
        
        if json_status == 200:
            print(f"\nEstado de la solicitud de la API de Rutas: {json_status}")
            print(f"URL de la ruta: {op_url}\n")
            print("=================================================")
            print(f"Direcciones desde '{new_loc1}' hasta '{new_loc2}'")
            print("=================================================")
            
            # Obtener distancia (metros a kilómetros) y formatear a 2 decimales
            distance_km = json_data["paths"][0]["distance"] / 1000
            # Obtener tiempo (milisegundos a minutos y horas) y formatear a 2 decimales
            time_ms = json_data["paths"][0]["time"]
            time_min = time_ms / (1000 * 60)
            
            print(f"Distancia total: {distance_km:.2f} km")
            print(f"Tiempo estimado del viaje: {time_min:.2f} minutos")
            print("-------------------------------------------------")
            print("Instrucciones paso a paso (Narrativa del viaje en español):")
            print("-------------------------------------------------")
            
            instructions = json_data["paths"][0]["instructions"]
            for i, step in enumerate(instructions, 1):
                text = step["text"]
                dist_step = step["distance"] / 1000
                print(f"{i}. {text} ({dist_step:.2f} km)")
            print("-------------------------------------------------")
        else:
            print(f"Error al calcular la ruta. Código de estado: {json_status}")