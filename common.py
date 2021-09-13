import os
import logging

# mode = "prod" for heroku "dev" for running locally

mode = "prod" 
TELEGRAM_ACCESS_TOKEN = "1828250945:AAG8mxez-5ufyPwlikLAzl1A8wyoUQT409I"
HEROKU_APP_NAME = "libgentelegrambot123"
LIBGEN_DOMAIN = "https://libgen.is/"

# Enable logging
logging.basicConfig(format='%(asctime)s | %(levelname)s | %(name)s | %(message)s',
                    level=logging.INFO)

logger = logging.getLogger()
