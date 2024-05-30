from uugai_python_color_prediction.ColorPrediction import ColorPrediction
from uugai_python_dynamic_queue.MessageBrokers import RabbitMQ
from uugai_python_kerberos_vault.KerberosVault import KerberosVault

from assets.scripts.read_first_frame import read_first_frame
from dotenv import load_dotenv
import os


# Load environment variables
load_dotenv()

# Initialize a message broker using the python_queue_reader package
print("1) Initializing RabbitMQ...")
rabbitmq = RabbitMQ(queue_name=os.getenv('QUEUE_NAME'),
                    target_queue_name=os.getenv('TARGET_QUEUE_NAME'),
                    exchange=os.getenv('EXCHANGE'),
                    host=os.getenv('HOST'),
                    username=os.getenv('USERNAME'),
                    password=os.getenv('PASSWORD'))

# Initialize Kerberos Vault
print("2) Initializing Kerberos Vault...")
kerberos_vault = KerberosVault(storage_uri=os.getenv('STORAGE_URI'),
                               storage_access_key=os.getenv(
                                   'STORAGE_ACCESS_KEY'),
                               storage_secret_key=os.getenv(
                                   'STORAGE_SECRET_KEY'))


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
        message, media_type='video', media_savepath='assets/videos/video.mp4')

    ############################################
    # Implement your own logic here
    ############################################

    # In this example, we will perform color prediction on the first frame of
    # the video
    print("5) Perform action on the media... (in this case color prediction)")
    main_colors, _, _ = ColorPrediction.find_main_colors(image=read_first_frame('assets/videos/video.mp4'),
                                                         min_clusters=1,
                                                         max_clusters=5,
                                                         downsample_factor=0.95,
                                                         increase_elbow=0,
                                                         verbose=False,
                                                         plot=False)
    print("\tMain colors found in the first frame:", main_colors.tolist())
