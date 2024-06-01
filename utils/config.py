import os
from dotenv import load_dotenv

# This fill will load the .env file in the root directory
# and serve it as a config object

def read_config():
    load_dotenv()
    CONFIG = {
        'QUEUE_NAME': os.getenv('QUEUE_NAME'),
        'TARGET_QUEUE_NAME': os.getenv('TARGET_QUEUE_NAME'),
        'EXCHANGE': os.getenv('EXCHANGE'),
        'HOST': os.getenv('HOST'),
        'USERNAME': os.getenv('USERNAME'),
        'PASSWORD': os.getenv('PASSWORD'),
        'STORAGE_URI': os.getenv('STORAGE_URI'),
        'STORAGE_ACCESS_KEY': os.getenv('STORAGE_ACCESS_KEY'),
        'STORAGE_SECRET_KEY': os.getenv('STORAGE_SECRET_KEY')
    }
    return CONFIG