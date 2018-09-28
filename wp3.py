import requests
import json
import datetime, threading, time



next_call = time.time()

CURRENCY_LAYER_KEY = "12ce71e92325aaf31ddea964b322f754"

PESOS_OLD_VALOR = 0

NEW_VALOR = 0


ALARMA_MIN = 39
ALARMA_MAX = 41.1

GAP = 0.5

TWILIO_SID = "AC6f5b2634a0d8271b75c06305ee087763"
TWILIO_AUTHTOKEN = "d320fa12da4b7b096a27e87c38c463cd"
TWILIO_MESSAGE_ENDPOINT = "https://api.twilio.com/2010-04-01/Accounts/AC6f5b2634a0d8271b75c06305ee087763/Messages.json".format(TWILIO_SID=TWILIO_SID)
TWILIO_NUMBER = "whatsapp:+14155238886"

to_number = "whatsapp:+5491131841931" #fer_number
#to_number = "whatsapp:+5491153168907" #facu_number
#to_number = "whatsapp:+5491140741607" #Mariano_number
#to_number = "whatsapp:+5491131982942" #Joaquin_number

MENSAJE = ("Fresenius REPUESTOS - Msg de Prueba" + '\r\n')

def get_USD_2_PESOS(debugEcho):
    payload = {'access_key':'12ce71e92325aaf31ddea964b322f754','currencies':'ARS','source':'USD','format': '1'}
    r = requests.get('http://apilayer.net/api/live', params=payload)
    if (debugEcho == True):
        print('\r\n') # retorno carro
        print(r.url)
        print('\r\n') # retorno carro
    json_data = json.loads(r.text)
    valor = json_data['quotes']['USDARS']
    return valor

def send_whatsapp_message(to, message):
    message_data = {
        "To": to,
        "From": TWILIO_NUMBER,
        "Body": message,
    }
    response = requests.post(TWILIO_MESSAGE_ENDPOINT, data=message_data, auth=(TWILIO_SID, TWILIO_AUTHTOKEN))

    response_json = response.json()
    return response_json

def send_whatapp_ver2(para_quien, mensaje):
    mensaje+= "Dolar = " + str( NEW_VALOR )
    msg_enviado = send_whatsapp_message(para_quien, mensaje )
    #print(msg_enviado['sid']) # SM5xxxafa561e34b1e84c9d22351ae08a0
    #print('\r\n') # SM5xxxafa561e34b1e84c9d22351ae08a0
    print(msg_enviado['status']) # queued
    print("errorCode: " + str(msg_enviado['error_code']) + " - ErrorMsg: "  + str(msg_enviado['error_message'])) # queued
    print("msg: "  + str(msg_enviado['body']) + " " + str( NEW_VALOR ) ) # queued
    print('\r\n') # retorno carro
    return True


def foo():
    global next_call

    global NEW_VALOR
    global PESOS_OLD_VALOR

    NEW_VALOR = get_USD_2_PESOS(False)

    if  ( NEW_VALOR >= ALARMA_MAX) :
        send_whatapp_ver2(to_number, "mayor que alarma")

    if  ( NEW_VALOR < ALARMA_MIN) :
        send_whatapp_ver2(to_number, "menor que alarma")

    if  ( abs( NEW_VALOR - PESOS_OLD_VALOR) > GAP ) :
        send_whatapp_ver2(to_number, "mayor q GAP")

    print (datetime.datetime.now())
    print ( " [" + str(PESOS_OLD_VALOR) + "] -" + " [" + str(NEW_VALOR) + "]")
    #print ( " [" + "] -" + " [" + str(NEW_VALOR) + "]")
    next_call = next_call+15

    PESOS_OLD_VALOR = NEW_VALOR

    threading.Timer( next_call - time.time(), foo ).start()





# Init Variables __________________________________________________________________________
PESOS_OLD_VALOR = get_USD_2_PESOS(True)
PESOS_OLD_VALOR = 0


# main___________________________________________________________________________
foo()


