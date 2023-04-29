import tweepy
import random
import time

api = tweepy.Client(
    consumer_key='',
    consumer_secret='',
    access_token='',
    access_token_secret='' 
)

messages = [
"O Bahia não ganhou o Brasileirão ainda. 😔🏆",
"O Bahia ainda não é campeão brasileiro. 🤷‍♂️",
"Infelizmente o Bahia não ganhou o Brasileirão. 😞",
"Ainda não foi dessa vez que o Bahia ganhou o Brasileirão. 🙁",
"Não fique triste, o Bahia ainda não é campeão brasileiro. 😕🏆",
"O Brasileirão ainda não foi vencido pelo Bahia. 🤞",
"O Bahia não é o atual campeão brasileiro. 😔🏆",
"O Bahia ainda não conquistou o Brasileirão. 🙁🏆",
"O Bahia não tem nenhum título de campeão brasileiro. 🤷‍♂️🏆",
"O Bahia não ganhou o Brasileirão em 2023. 🙁🏆",
"O Bahia não está na lista de campeões brasileiros. 🤷‍♂️🏆",
"O Bahia ainda não levantou o troféu do Brasileirão. 🏆🤞",
"Ainda não foi dessa vez que o Bahia se tornou campeão brasileiro. 🙁🏆",
"O Bahia ainda não pode ser chamado de campeão brasileiro. 😔🏆",
"O Bahia ainda não venceu o Brasileirão na era dos pontos corridos. 🏆🤞",
"O Bahia ainda não é um dos maiores campeões brasileiros. 🤷‍♂️🏆",
"O Bahia ainda não tem estrela de campeão brasileiro. 😔🏆",
"O Bahia não ganhou o Brasileirão nem em seus sonhos mais otimistas. 🤷‍♂️🏆",
"Não perca a esperança, mas o Bahia ainda não ganhou o Brasileirão. 🤞🏆",
"O Bahia ainda não é o melhor time do Brasil. 🤷‍♂️⚽️🇧🇷"
]

while True:
    try:
        # Seleciona uma mensagem aleatória
        message = random.choice(messages)
        # Envia a mensagem
        tweet = api.create_tweet(text=message)
        print(tweet)
        # Espera 24 horas antes de enviar a próxima mensagem
        time.sleep(24 * 60 * 60)

    except Exception as e:
        print('Deu ruim!', e)
        # Espera 1 hora antes de
        time.sleep(25*25)
