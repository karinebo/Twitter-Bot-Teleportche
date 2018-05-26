import sys
import tweepy #API de comunicação com o Twitter
import fasttext ##API para aprendizado de classificação de textos
from secrets import *

#Autenticação no Twitter, os valores devem estar no arquivo secrets.py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
auth.set_access_token(access_token, access_secret)

#Criação da API do Twitter
api = tweepy.API(auth) 

#Após o modelo treinado, apenas carrega-se o arquivo "model.bin"
print("Carregando modelo")
classifier = fasttext.load_model('model.bin')
print("Modelo carregado: Pode Tweetar!")

#Classe para armazenar cada predição
class Prediction:
     def __init__(self, sentiment, probability, replymsg):
         self.sentiment = sentiment
         self.probability = probability
         self.replymsg = replymsg


def predictSentiment(textsArray):
    print(textsArray)

    #Predição do sentimento relacionado ao texto com probabilidade associada
    labels = classifier.predict_proba(textsArray)
    predictedValues = labels[0][0]
    sentiment = ""
    print(predictedValues[0])
    if predictedValues[0] == "__label__2":
        sentiment = "POSITIVO"
    else:
        if predictedValues[0] == "__label__1":
            sentiment = "NEGATIVO"
        else: sentiment = "NEUTRO"

    probability = round(predictedValues[1] * 100, 2)  
    replyMsg = sentiment+" com probabilidade de " + str(probability) + "%"
    if sentiment == "POSITIVO":
       replyMsg = replyMsg + "\nVida longa e próspera!"
    else:
        replyMsg = replyMsg + "\nDa próxima vez, vá de caminhão!"
    
    result = Prediction(sentiment, probability, replyMsg)
    print(replyMsg)
    return result 
    
#Classe herdando o StreamListener do Tweepy
class BotStreamer(tweepy.StreamListener):
    #Método chamado no momento em que um novo tweet atende às condições do filtro definido: stream.filter(track=['@teleporttche'])
    def on_status(self, status):
        #status é o objeto "tweet" que contém várias informações, aqui estão sendo extraídas
        #as informações necessárias para o contexto
        username = status.user.screen_name 
        status_id = status.id
        textTweet = status.text
        textTweet = textTweet.replace("@teleporttche ", "")
        review = [textTweet]
        #Montagem da mensagem Reply
        reply = predictSentiment(review)
        if reply.sentiment == "POSITIVO":
            image_name = "./images/spock1.gif"
        else:
            image_name = "./images/spock3.gif"

        #Posta o Reply à mensagem original
        api.update_with_media(image_name, status='@{0}'.format(username) + " "+reply.replymsg, in_reply_to_status_id=status_id)
    #Fim do método on_status
#Fim da classe BotStreamer

try:
    print("Pressione Ctrl + C para sair")
    #Criação do stream que ficará "ouvindo" os tweets
    myStreamListener = BotStreamer()
    stream = tweepy.Stream(auth, myStreamListener)
    
    # Filtra os tweets de acordo com o nome da aplicação criada anteriormente
    stream.filter(track=['@teleporttche'])
except KeyboardInterrupt:
    print("Saindo")
    sys.exit()
