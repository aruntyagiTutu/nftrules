import time
from actions import bulk_push_notification
#assumption: we need to do these on given time for all users, if have to trigger these for dynamic timing for every item, we will use queue with ttl
def trigger_daily():
    #rule 1
    alert_unsold_nfts_7days()

    #rule 2
    do_something()

def alert_unsold_nfts_7days():
    #code here
    users_to_alert = get_unsold_nfts([]) 
    bulk_push_notification(users_to_alert, "your nft is not sold from last 10 days, take action")
    return

def do_something():
    return


def get_unsold_nfts(nft_listing):
    unsold_nfts = []
    current_time = int(time.time())

    # in real proj this data will be extracted from db via query
    for user_id, nft_id, is_sold, listed_time in nft_listing:
        if not is_sold:
            time_diff = current_time - listed_time
            if time_diff >= 7 * 24 * 60 * 60:  # 7 days in seconds
                unsold_nfts.append(user_id)
    return unsold_nfts
