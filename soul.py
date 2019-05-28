import time
import telebot
import re
import bs4
import random
import requests
from selenium import webdriver
from telebot import types

gap = ["dip","dip","dip","dip","dip"]
dap = ['https://www.mysmartprice.com/','https://www.mysmartprice.com/','https://www.mysmartprice.com/','https://www.mysmartprice.com/','https://www.mysmartprice.com/']
bot_token = '785004393:AAF1SzFgoMVlZ6A0uVZcXHJBwqiQVgJGTJk'

bot = telebot.TeleBot(token=bot_token)

updates = bot.get_updates()
print([u.message.text for u in updates])

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Greeting Sir! Welcome I am DazBot")
    bot.reply_to(message, "If you dont know how to use type /howtouse.")


@bot.message_handler(commands=['howtouse','help'])
def send_welcome(message):
    bot.reply_to(message, "Its very easy I have only few commands.")
    bot.reply_to(message, "/searchphones to search phones for there lowest prices")
    bot.reply_to(message, "/devinfo this tells you about the dev")
    bot.reply_to(message, "/botinfo this tells you about the bot and its working")
    bot.reply_to(message, "/technologies the technologies used")
    bot.reply_to(message, "/functionalities to see what all I can do")
    bot.reply_to(message, "/quotes if you are felling down I can cheer you up buddy")

@bot.message_handler(commands=['functionalities'])
def send_welcome(message):
    bot.reply_to(message, "My superbot ability is Searching lowest prices for any mobile phone you want")
    bot.reply_to(message, "But I can tell you a joke if you insist( Type /tellmeajoke)")

@bot.message_handler(commands=['tellmeajoke'])
def send_welcome(message):
    bot.reply_to(message, "Thor ask ultron whats your age. Ultron told he doesnt know. Told u age of ultron doesnt make sense....")

@bot.message_handler(commands=['devinfo'])
def send_welcome(message):
    bot.reply_to(message, "My Creators are.....")
    bot.reply_to(message, "Ashish Shah @alex55936 and Dipan Nanda @DarkDevil1999")

@bot.message_handler(commands=['botinfo'])
def send_welcome(message):
    bot.reply_to(message, "I feed on dynamic and static web pages and use web scraping to digest it")

@bot.message_handler(commands=['technologies'])
def send_welcome(message):
    bot.reply_to(message, "I was built using dynamic and static webscrapping using selenium and beautifulsoup on pythontelgrambot")

@bot.message_handler(commands=['searchphones'])
def send_welcome(message):
    msg = bot.reply_to(message, "The phone you want to search is.....")
    bot.register_next_step_handler(msg, process_title_step)

def urlify(s):
    s = re.sub(r"\s+", '%20', s)

    return s

def process_title_step(message):
    try:
        global gap
        global dap
        namer = str(message.text)
        sam = str(namer)
        nam = urlify(sam)
        s = "#s="
        msp = "https://www.mysmartprice.com/msp/search/search.php?search_type=full&typed_term=&s="
        dip = msp + nam + s + nam

        driver = webdriver.Chrome(executable_path=r'/usr/bin/chromedriver')
        driver.get(dip)
        res = driver.execute_script("return document.documentElement.outerHTML")
        soup = bs4.BeautifulSoup(res, 'html.parser')
        driver.quit()

        containers = soup.findAll('div', {'class': 'prdct-item'})
        productnames = []
        links = []
        for items in containers:
            productname = items.find('a', {"class": "prdct-item__name"}).text
            productnames.append(productname[1:-1])
            links.append(items.a["href"])

        for i in range(0,5):
            dap[i] = links[i]
            gap[i] = productnames[i]
        j = 1
        bot.reply_to(message, "I found these phones....")
        for i in productnames:
            if j < 5:
                d = str(j)
                f = d + " ----->  " + i
                bot.reply_to(message, f)
                j+=1
        daz = bot.reply_to(message,"Which one are you looking for?(Only type the Index)")
        bot.register_next_step_handler(daz, process_next_step)
    except Exception as e:
        bot.reply_to(message, 'oooops')

def process_next_step(message):
    try:
        global gap
        global dap
        gamer = int(message.text)
        bot.reply_to(message,gap[gamer-1])
        url = dap[gamer-1]

        page = requests.get(url)
        soup = bs4.BeautifulSoup(page.text, 'html.parser')

        containers = soup.findAll("div", {"class": "prc-tbl__row-wrpr"})
        cpu = soup.findAll("li", {"class": "kyspc__item kyspc__item--cpu"})
        ram = soup.findAll("li", {"class": "kyspc__item kyspc__item--ram"})
        storage = soup.findAll("li", {"class": "kyspc__item kyspc__item--strge"})
        battery = soup.findAll("li", {"class": "kyspc__item kyspc__item--bttry"})
        camera = soup.findAll("li", {"class": "kyspc__item kyspc__item--cmra"})
        screensize = soup.findAll("li", {"class": "kyspc__item kyspc__item--aspct"})
        sim = soup.findAll("li", {"class": "kyspc__item kyspc__item--sim"})
        os = soup.findAll("li", {"class": "kyspc__item kyspc__item--os"})

        productdata = []
        for item in cpu:
            productdata.append(item.getText())
        for item in ram:
            productdata.append(item.getText())
        for item in storage:
            productdata.append(item.getText())
        for item in battery:
            productdata.append(item.getText())
        for item in camera:
            productdata.append(item.getText())
        for item in screensize:
            productdata.append(item.getText())
        for item in sim:
            productdata.append(item.getText())
        for item in os:
            productdata.append(item.getText())

        stores = []
        prices = []
        for items in containers:
            stores.append(items["data-storename"])
            prices.append(items.getText())

        j = 0
        for i in stores:
            j += 1
        s = " "
        for i in range(0, 8):
            if i == 0:
                s = productdata[i]
            else:
                s = s + ", " + productdata[i]

        d = ["", "", "", ""]
        if j > 4:
            j = 4
        for i in range(0, j):
            d[i] = stores[i] + prices[i]

        bot.reply_to(message,s)
        for i in range(0, j):
            bot.reply_to(message,d[i])

        gotr = "For Further information contact "
        dotr = gotr + dap[gamer-1]

        bot.reply_to(message,dotr)
    except Exception as e:
        bot.reply_to(message, 'oooops')

@bot.message_handler(commands=['quotes'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add('Yes', 'Hell No')
    msg = bot.reply_to(message, "Are you felling down?", reply_markup=markup)
    bot.register_next_step_handler(msg, process_feedom_step)

def process_feedom_step(message):
    try:
        dom = message.text
        if (dom == u'Yes'):
            bot.reply_to(message, "Buddy let me cheer you up ;)")
            driver = webdriver.Chrome(executable_path=r'/usr/bin/chromedriver')
            driver.get('https://www.brainyquote.com/top_100_quotes')
            res = driver.execute_script("return document.documentElement.outerHTML")
            soup = bs4.BeautifulSoup(res, 'lxml')
            driver.quit()

            containers = soup.findAll('a')
            qt = []
            for items in containers:
                qt.append(items.text)

            qt = qt[80:146]

            quotes = []
            authors = []
            i = 0
            while i < len(qt) - 1:
                if i % 2 == 0:
                    quotes.append(qt[i])
                    authors.append(qt[i + 1])
                i += 1

            quotesauth = []
            ranc = random.randint(1, len(quotes) - 1)

            sam = ""
            i = 0
            while i < len(quotes) - 1:
                sam = quotes[i] + " - " + authors[i]
                quotesauth.append(sam)
                i += 1
            bot.reply_to(message, quotesauth[ranc])
        elif (dom == u'Hell No'):
            bot.reply_to(message, "As you say!")
        else:
            raise Exception()
    except Exception as e:
        bot.reply_to(message, 'oooops')

@bot.message_handler(commands=['feedback'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add('Yes', 'Hell No')
    msg = bot.reply_to(message, "Do You like Me?", reply_markup=markup)
    bot.register_next_step_handler(msg, process_feed_step)

def process_feed_step(message):
    try:
        dom = message.text
        if (dom == u'Yes'):
            bot.reply_to(message,"Thankyou for your love.")
        elif (dom == u'Hell No'):
            bot.reply_to(message,"Sorry If you are not impressed")
            bot.reply_to(message,"For further assistance contact /devinfo")
        else:
            raise Exception()
    except Exception as e:
        bot.reply_to(message, 'oooops')


while True:
    try:
        bot.enable_save_next_step_handlers(delay=2)
        bot.load_next_step_handlers()
        bot.polling()
    except Exception:
        time.sleep(15)

bot.enable_save_next_step_handlers(delay=2)

bot.load_next_step_handlers()

bot.polling()