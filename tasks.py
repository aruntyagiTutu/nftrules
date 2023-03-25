from actions import push_notification
import tasks_after_time

users_nft_purchase = {}
nfts = {}
configured_time = 10


# Define the process_task function
def process_data(data):
    # Your task code here
    when_and_then(data)
    
    print(f"Processing task: {data}")


def when_and_then(data):
    user_id = data['userid']
    then = do_nothing
    params = ()
    if data['verb'] == 'listed':
         if check_condition():
              then = send_verified_notification_after_configured_time
    elif data['verb'] == 'buy':
        print('bought')
        if is_first_NFT_purchase_for_the_user(data):
            print('true')
            users_nft_purchase[user_id] = 1
            then = push_notification
            params = (user_id, 'Congratulations! You made your first NFT purchase.')
        users_nft_purchase[user_id] += 1
    result = then(*params)
    return result


    
#actions
def do_nothing():
    print("no action")

def send_verified_notification_after_configured_time(user_id, nft_id, time):
     tasks_after_time.add_message_with_delay(user_id, nft_id, time)

#conditions
def is_first_NFT_purchase_for_the_user(data):
    user_id = data['userid']
    verb = data['verb']
    noun = data['noun']
    if verb == 'buy' and noun == 'nft':
            if user_id not in users_nft_purchase:
                return True
    return False

def check_condition():
     # check condition as per rule data
     return True
