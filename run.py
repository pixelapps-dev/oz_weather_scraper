# %%

import os
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

token = os.environ['tokeny']

current_time = datetime.now().strftime("%H:%M:%S")

# %%


def rand_delay(num):
  import random 
  import time 
  rando = random.random() * num
#   print(rando)
  time.sleep(rando)


# %%


import bom_scraper


rand_delay(5)


# os.system(f"gh auth login --with-token < {token}")
# os.system("git add .")
# git_commit_with_time = f'git commit -m "New data:{current_time}"'
# os.system(git_commit_with_time)
# os.system("git push --set-upstream origin main")


# # %%
