import os
from postget.Posts import Posts
from dotenv import load_dotenv

load_dotenv()

date_start = '2022-08-01'
date_end = '2022-12-01'

twitter = Posts(username=os.environ['TWITTER_USERNAME'],
                password=os.environ['TWITTER_PASSWORD'],
                email_address=os.environ['TWITTER_EMAIL'],
                query='$TSLA',
                since_time=date_start,
                until_time=date_end,
                wait_scroll_base=1.5,
                wait_scroll_epsilon=1,
                mode=1)

try:
    twitter.login()
    twitter.search()
    twitter.print_results()
finally:
    # twitter.quit_browser()
    pass