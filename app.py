import json
from riotwatcher import LolWatcher, ApiError
from flask import Flask,render_template


app = Flask(__name__)

# golbal variables
api_key = 'RGAPI-457ce921-196c-4880-b44c-4845e0a5c5b0'
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
    return tier+" "+rank+"|"+str(lp)+" wins:"+str(wins)+" losses:"+str(losses)


if __name__ == '__main__':
    app.run()
