from chatbot import ChatBot

Bot = ChatBot("Marvin")

while True:
    frase = Bot.escutar()
    resp = Bot.pensar(frase)
    Bot.falar(resp)
    if resp == 'tchau':
        break
