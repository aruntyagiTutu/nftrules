from actions import push_notification
from queue import PriorityQueue
import time

# Create an in-memory priority queue
q = PriorityQueue()

# Define a function to add a message to the queue with a delay
def add_message_with_delay(user_id, nft_id, delay_in_minutes):
    # Get the current time in seconds
    current_time = time.time()

    # Calculate the delay in seconds
    delay_in_seconds = delay_in_minutes * 60

    # Calculate the timestamp when the message should be processed
    process_time = current_time + delay_in_seconds

    # Add the message to the queue with the calculated timestamp as the priority
    q.put((process_time, (user_id, nft_id)))

# Define a worker function to process messages from the queue
def process_messages():
    while True:
        # Get the next message from the queue
        _, message = q.get()

        # Unpack the message
        user_id, nft_id = message

        status = '' # get state of nft from db
        # Check if the NFT has been sold or not
        message = 'listed successfully' if status == 'v' else 'not listed because {reason}'
        push_notification(user_id, message)

        # Wait for 1 second before processing the next message
        time.sleep(1)

# Start the worker process in a separate thread
import threading
worker_thread = threading.Thread(target=process_messages)
worker_thread.start()
