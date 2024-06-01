from uugai_python_color_prediction.ColorPrediction import ColorPrediction
from uugai_python_dynamic_queue.MessageBrokers import RabbitMQ
from uugai_python_kerberos_vault.KerberosVault import KerberosVault
from utils.read_first_frame import read_first_frame
from utils.config import read_config
import os

# Read config, this will load the .env file in the root directory
# and serve it as a config object
config = read_config()

# Initialize a message broker using the python_queue_reader package
print("1) Initializing RabbitMQ...")
rabbitmq = RabbitMQ(queue_name=config['QUEUE_NAME'],
                    target_queue_name=config['TARGET_QUEUE_NAME'],
                    exchange=config['EXCHANGE'],
                    host=config['HOST'],
                    username=config['USERNAME'],
                    password=config['PASSWORD'])

# Initialize Kerberos Vault
print("2) Initializing Kerberos Vault...")
kerberos_vault = KerberosVault(storage_uri=config['STORAGE_URI'],
                               storage_access_key=config['STORAGE_ACCESS_KEY'],
                               storage_secret_key=config['STORAGE_SECRET_KEY'])

# For educational purposes, we will receive 5 messages from the queue.
# In a real-world scenario, the while loop would be used to continuously
# receive messages.

# while True:
for _ in range(5):
    # Receive message from the queue
    print("3) Receiving message from the queue...")
    message = rabbitmq.receive_message()

    # Retrieve media from the Kerberos Vault
    print("4) Retrieving media from the Kerberos Vault...")
    resp = kerberos_vault.retrieve_media(
        message, media_type='video', media_savepath='data/video.mp4')

    ############################################
    # Implement your own logic here
    ############################################

    # In this example, we will perform color prediction on the first frame of
    # the video
    print("5) Perform action on the media... (in this case color prediction)")
    main_colors, _, _ = ColorPrediction.find_main_colors(image=read_first_frame('data/video.mp4'),
                                                         min_clusters=1,
                                                         max_clusters=5,
                                                         downsample_factor=0.95,
                                                         increase_elbow=0,
                                                         verbose=False,
                                                         plot=False)
    print("\tMain colors found in the first frame:", main_colors.tolist())

    # Cleanup the video
    print("6) Cleaning up the video...")
    os.remove('data/video.mp4')