import json
import os

from riotwatcher import LolWatcher, ApiError
from flask import Flask,render_template


app = Flask(__name__)

# golbal variables

api_key = os.getenv('api')
watcher = LolWatcher(api_key)
my_region = 'na1'
me = watcher.summoner.by_name(my_region, 'NewtMo')
my_ranked_stats = watcher.league.by_summoner(my_region, me['id'])


@app.route('/')
def hello_world():
    tier = my_ranked_stats[0]['tier']
    rank = my_ranked_stats[0]['rank']
    lp = my_ranked_stats[0]['leaguePoints']
    wins = my_ranked_stats[0]['wins']
    losses = my_ranked_stats[0]['losses']
    print(my_ranked_stats)
    return "His rank is "+ tier+" "+rank+" League Points Are "+str(lp)+" wins:"+str(wins)+" losses:"+str(losses)


if __name__ == '__main__':
    app.run()
