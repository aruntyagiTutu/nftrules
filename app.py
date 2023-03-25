from flask import Flask, request
from tasks import process_data
from buy_service import place_order

app = Flask(__name__)
#celery = Celery(__name__, broker='redis://localhost:6379/0')

@app.route('/post', methods=['POST'])
def receive_post_request():
    data = request.json
    #process_data.delay(data)  # execute the task asynchronously
    return 'POST request received successfully'


# Define the route for adding tasks
@app.route('/buy', methods=['POST'])
def buy_nft():
    # Get the request payload
    payload = request.json
    
    if place_order(payload):
    # Add the task to the queue
        task_queue.put(payload)
                 
    # Return a JSON response with the task ID
    return 'Request Processed'

@app.route('/list', methods=['POST'])
def list_nft():
    # Get the request payload
    payload = request.json
    
    # Add the task to the queue
    task_queue.put(payload)
                 
    # Return a JSON response with the task ID
    return 'Request Processed'

import threading
import queue

# Create a queue object
task_queue = queue.Queue()

# Define the worker function
def worker():
    while True:
        # Get a task from the queue
        data = task_queue.get()
        
        # Process the task
        process_data(data)
        
        # Mark the task as done
        task_queue.task_done()

# Start the worker thread
worker_thread = threading.Thread(target=worker)
worker_thread.start()


if __name__ == '__main__':
    app.run()
