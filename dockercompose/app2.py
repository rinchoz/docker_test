from flask import Flask
from redis import Redis

#/******************************

app = Flask(__name__)
db = Redis(host="redis")

@app.route("/")
def hello():
  visitsCounter = db.incr('visitsCounter')
  html = "<H1> Mне надоели твои розовые сиськи и твой микрофон. Даааа. Пезда! Встала и пошла отсюда ! </H1>" \
  "<b>Встала и пошла, повторяю </b>{visits} раз" \
  "<br/>"

  return html.format(visits=visitsCounter)

if (__name__=="__main__") :
  app.run(host="0.0.0.0", port=80)
