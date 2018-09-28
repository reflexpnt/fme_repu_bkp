import requests
#from forex_python.converter import CurrencyRates



TWILIO_SID = "AC6f5b2634a0d8271b75c06305ee087763"
TWILIO_AUTHTOKEN = "d320fa12da4b7b096a27e87c38c463cd"
TWILIO_MESSAGE_ENDPOINT = "https://api.twilio.com/2010-04-01/Accounts/AC6f5b2634a0d8271b75c06305ee087763/Messages.json".format(TWILIO_SID=TWILIO_SID)
TWILIO_NUMBER = "whatsapp:+14155238886"

#c = CurrencyRates()

def get_USD_2_PESOS():
    #valor = c.get_rate('USD', 'EUR')
    return 39.4

def send_whatsapp_message(to, message):
    message_data = {
        "To": to,
        "From": TWILIO_NUMBER,
        "Body": message,
    }
    response = requests.post(TWILIO_MESSAGE_ENDPOINT, data=message_data, auth=(TWILIO_SID, TWILIO_AUTHTOKEN))

    response_json = response.json()
    return response_json



to_number = "whatsapp:+5491131841931" #fer_number
#to_number = "whatsapp:+5491153168907" #facu_number
#to_number = "whatsapp:+5491140741607" #Mariano_number
#to_number = "whatsapp:+5491131982942" #Joaquin_number


MENSAJE = "Fresenius REPUESTOS - Mensaje de Prueba" + '\r\n' + "Dolar = " + str(get_USD_2_PESOS())

msg_enviado = send_whatsapp_message(to_number, MENSAJE)
print(msg_enviado['sid']) # SM5xxxafa561e34b1e84c9d22351ae08a0
print('\r\n') # SM5xxxafa561e34b1e84c9d22351ae08a0
print(msg_enviado['status']) # queued
print("errorCode: " + str(msg_enviado['error_code']) + " - ErrorMsg: "  + str(msg_enviado['error_message'])) # queued
print("msg: "  + str(msg_enviado['body'])) # queued
print('\r\n') # retorno carro
#print(msg_enviado) # SM5xxxafa561e34b1e84c9d22351ae08a0
