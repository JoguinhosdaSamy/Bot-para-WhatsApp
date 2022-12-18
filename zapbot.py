import pywhatkit
import keyboard
import time
from datetime import datetime

#INSIRA AQUI O CÓDIGO DO PAÍS MAIS O NÚMERO DO TELEFONE E NÃO SE ESQUEÇA DO 9 NA FRENTE
contatos = ['+552798819-9397', '+552899995-0128']

while len(contatos) >= 1:
    pywhatkit.sendwhatmsg(contatos[0], 'koleeeeeeeeeee, testando meu bot', datetime.now().hour, datetime.now().minute + 2)
    del contatos[0]
    time.sleep(15)
    keyboard.press_and_release('enter')
    time.sleep(20)
    keyboard.press_and_release('ctrl + w')