import logging
from load_config import *
from slack_sdk import WebhookClient

# loads local configuration
config = load_config('config.yml')

log = logging

# Set default log settings
log_level = 'INFO'
log_file = 'bot.log'

# Get logging variables
log_level = config['LOGGING']['LOG_LEVEL']
log_file = config['LOGGING']['LOG_FILE']
if config['LOGGING']['ENABLE_STREAM']:
    handlers = [logging.FileHandler(log_file), logging.StreamHandler()]
else:
    handlers = [logging.FileHandler(log_file)]
log.basicConfig(format='%(asctime)s %(levelname)s: %(message)s',
                handlers=handlers)
logger = logging.getLogger(__name__)
level = logging.getLevelName(log_level)
logger.setLevel(level)

def sendMessageToChannel(msg):
    if config['LOGGING']['SLACK']['ENABLE']:
        url = config['LOGGING']['SLACK']['WEBHOOK_URL']
        webhook = WebhookClient(url)
        webhook.send(text=msg)