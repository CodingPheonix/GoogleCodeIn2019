from telegram.ext import Updater, CommandHandler
import requests
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


def start(update, context):
    update.message.reply_text('Hi! I FedoraTaskBot and I fetch forks from the Fedora-Infra!')

def help(update, context):
    update.message.reply_text('Ask me to fetch the number of forks in the Fedora-Infra github repository by typing /fetch!')

def fetch(update, context):
    
    r = requests.get(url='https://api.github.com/orgs/fedora-infra/repos').json()
    
    numberForks=0
    
    for obj in r:
        numberForks += obj['forks']
    
    update.message.reply_text('Number of forks in Fedora-Infra repository: {}!'.format(numberForks))

def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    
    updater = Updater("1037409868:AAG9ff6BCIb7PrWRT40jo228BZ_MLNUiHyU", use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("fetch", fetch))
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
