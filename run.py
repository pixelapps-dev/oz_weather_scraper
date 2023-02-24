# %%

from github import Github

import os
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

token = os.environ['tokeny']
emailo = os.environ['emailo']


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

# g = Github(token)



# os.system("git init")
# os.system("git remote rm origin")
os.system(f"gh auth login --with-token < {token}")


# os.system(f"git remote add origin git@github.com:joshnicholas/oz_weather_scraper.git")

# os.system(f'git config --global user.email "{emailo}"')
# os.system('git config --global user.name joshnicholas')
# os.system(f'git config --global password {token}')
# os.system("git rm -r --cached .")
os.system("git add .")
git_commit_with_time = f'git commit -m "New data:{current_time}"'
os.system(git_commit_with_time)
os.system("git push --set-upstream origin main")



# %%
