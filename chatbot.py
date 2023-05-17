class ChatBot():
    def __init__(self,nome):
        self.nome = nome
        self.historico = [""]
        self.conhecidos = ['Felipe','Emanuel']

    def peganome(self,nome):
        if 'o meu nome eh' in nome:
            nome = nome[14:]
        nome = nome.title()
        return nome    
    
    def escutar(self):
        frase = input(">: ")
        frase.lower()
        frase.strip()
        frase.replace('é','eh')
        return frase

    def pensar(self,frase):
        if frase == "oi":
            print("Olá, eu sou um Robo e me chamo "+self.nome+".")
            return "Qual seu nome?"
        
        if self.historico[-1] == "Qual seu nome?":
           nome = self.peganome(frase)
           frase = self.respondenome(nome)
           return frase
        
        return "Não entendi."
        
    def falar(self,resp):
        print(resp)
        self.historico.append(resp)
   
    def respondenome(self,nome):
        if nome in self.conhecidos:
            frase = "Eaew"
        else:
            frase = "Muito prazer!"
            self.conhecidos.append(nome)
        return frase    
            
        


