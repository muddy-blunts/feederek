import pickle
import sys
from time import sleep

import feedparser
import telegram

feed_list =["https://vchasnoua.com/rss",
            ]

last_feeds = pickle.load(open("/home/muddy/feederek/db.p", 'rb'))
fee_links = []

bot = telegram.Bot(token='1723458733:AAFfwCThgBDtVvoPS43-L_Lz-UwfjVHop8c')

print(last_feeds)
print("-----Last feeds---")

def feederek():
    for i in feed_list:
        fee = feedparser.parse(i)
        fee_title = fee.feed.title
        for x in range(5):
            fee_links.append(fee['entries'][x]['id'])
            if fee['entries'][x]['id'] in last_feeds:
                print("Nothing new - " + fee_title)
            else:
                sleep(5) # for server flood detection
                entry_title = fee['entries'][x]['title']
                entry_id = fee['entries'][x]['id']
                print("Updated - " + fee_title)


                message = str("\n" + entry_title +"\n" + entry_id)
                bot.sendMessage(chat_id="@pokrovskme", text=message)

    pickle.dump(fee_links, open("/home/muddy/feederek/db.p", 'wb'))
    sys.exit()

if __name__ == "__main__":
    feederek()
