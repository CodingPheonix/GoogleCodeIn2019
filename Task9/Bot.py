from telegram.ext import Updater, CommandHandler
import requests
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

def start(update, context):
    update.message.reply_text('Hi! I am FedoraTaskBot and I fetch the number of forks of different pages from the Fedora-Infra!')

def help(update, context):
    update.message.reply_text('Ask me to fetch the number of forks in the Fedora-Infra github repository by typing /fetch {page} or /forks {page}!')

def fetch(update, context):

    r = requests.get(url='https://api.github.com/orgs/fedora-infra/repos').json()
    found = False

    if (len(context.args) != 1):
        update.message.reply_text("Please only supply one and only one argument to fetch")
    else:    
        for i in range(len(r)):
            if (context.args[0] == r[i]["name"]):
                update.message.reply_text("Number of forks for " + context.args[0] + " in the Fedora-Infra repository: " + str(r[i]["forks"]) + "!")
                found = True
                break
        if (not found):
            update.message.reply_text("I couldn't find a page for " + context.args[0] + " in the Fedora-Infra repository, try another page")
        
def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    
    updater = Updater("1037409868:AAG9ff6BCIb7PrWRT40jo228BZ_MLNUiHyU", use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("fetch", fetch, pass_args=True))
    dp.add_handler(CommandHandler("forks", fetch, pass_args=True))
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
