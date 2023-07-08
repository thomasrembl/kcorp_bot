#Kc bot
import os
import dotenv
import tweepy
import time
dotenv.load_dotenv()

api_key = os.environ.get('API_KEY')
api_secret = os.environ.get('API_SECRET')
bearer_token = os.environ.get('BEARER_TOKEN')
access_token = os.environ.get('ACCESS_TOKEN')
access_token_secret = os.environ.get('ACCESS_TOKEN_SECRET')



client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)

auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

def create_tweet():

    message_rl = "Fin des worlds pour nous après un magnifique top 8 #KCORP #KCORPWIN"
    message_lol = "L'équipe Lol est en vacances #KCORP #KCORPWIN"
    message_tm = "Top 5-8 à l' @ArcticGE pour Bren  #KCORP #KCORPWIN"
    message_tft = "Fin de solary party pour Double61 et Canbizz #KCORP #KCORPWIN"
    message_valo = "L'équipe valo est en vacances #KCORP #KCORPWIN"
    message_all = "L'équipe RL, l'équipe lol et valo sont en vacances. Pas de competition pour Bren. Fin de solary party pour Doule61 et Canbizz #KCORP #KCORPWIN"

    
    client_id = client.get_me().data.id

    start_id = 1
    initialisation_resp = client.get_users_mentions(client_id)
    if initialisation_resp.data != None:
        start_id = initialisation_resp.data[0].id

    while True:
        response = client.get_users_mentions(client_id, since_id=start_id)
        
        if response.data != None:
            for tweet in response.data:
                text= str(tweet.text).split(' ')
                last_world = text[-1]
                if str(last_world) == '#rl' or '#Rl' or '#RL':
                    try:
                        print(tweet.text)
                        client.create_tweet(in_reply_to_tweet_id=tweet.id, text=message_rl)
                        start_id = tweet.id
                    except:
                        pass
                elif str(last_world) == '#lol' or '#Lol':
                    try:
                        print(tweet.text)
                        client.create_tweet(in_reply_to_tweet_id=tweet.id, text=message_lol)
                        start_id = tweet.id
                    except:
                        pass
                elif str(last_world) == '#tm' or '#Tm' or '#TM':
                    try:
                        print(tweet.text)
                        client.create_tweet(in_reply_to_tweet_id=tweet.id, text=message_tm)
                        start_id = tweet.id
                    except:
                        pass
                elif str(last_world) == '#tft' or '#Tft':
                    try:
                        print(tweet.text)
                        client.create_tweet(in_reply_to_tweet_id=tweet.id, text=message_tft)
                        start_id = tweet.id
                    except:
                        pass
                elif str(last_world) == '#valo' or '#Valo':
                    try:
                        print(tweet.text)
                        client.create_tweet(in_reply_to_tweet_id=tweet.id, text=message_valo)
                        start_id = tweet.id
                    except:
                        pass
                elif str(last_world) == '#all' or '#All':
                    try:
                        print(tweet.text)
                        client.create_tweet(in_reply_to_tweet_id=tweet.id, text=message_all)
                        start_id = tweet.id
                    except:
                        pass
        time.sleep(5)

create_tweet()
