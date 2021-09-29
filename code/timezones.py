from datetime import datetime
import pytz

bogota_timezone = pytz.timezone("America/Bogota") #Zona horaria Bogotá "America/Bogota"
bogota_date = datetime.now(bogota_timezone)
print("Bogotá: ", bogota_date.strftime("%d/%m/%Y, %H:%M:%S"))

mexico_timezone = pytz.timezone("America/Mexico_City")
mexico_date = datetime.now(mexico_timezone)
print("Ciudad de México: ", mexico_date.strftime("%d/%m/%Y, %H:%M:%S"))

caracas_timezone = pytz.timezone("America/Caracas")
caracas_date = datetime.now(caracas_timezone)
print("Caracas: ", caracas_date.strftime("%d/%m/%Y, %H:%M:%S"))

