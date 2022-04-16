import requests
from time import sleep



class TelegramGroupToGroup():
    
    xtrade = "https://api.telegram.org/bot5106474176:AAGFChSzmjtOksah1FRznIZWedYDJ0pFf3U"
    xtradeChat_id = '-1001713261003'
    fastScalp = 'https://api.telegram.org/bot5199941980:AAHYniRpPGQ8cKu6eph3cbObl4BPiu0Frfk'

    def send_msg(self,message):
        msgtext = message["channel_post"]["text"]
        parameters = {"chat_id" : self.xtradeChat_id,"text" : msgtext,}
        requests.get(self.xtrade + "/sendMessage", data = parameters)
        


    def read_msg(self,offset):
        parameters = {"offset" : offset}
        resp = requests.get(self.fastScalp + "/getUpdates", data = parameters)
        data = resp.json()
        print(data)
        for result in data["result"]:
            self.send_msg(result)
        if data["result"]:
            return data["result"][-1]["update_id"] + 1


if __name__=='__main__':
    offset = 0
    bot = TelegramGroupToGroup()
    while True:  
        offset = bot.read_msg(offset)
        print('Stay for 3 Seconds')
        sleep(3)
        

