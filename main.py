from flask import Flask, render_template, redirect, request, jsonify, send_file
from datetime import datetime

def log():
  tiempo = datetime.now()
  if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
    file = open("ip_logs.html", "a+")
    file.write(f"[{tiempo.day}/{tiempo.month}/{(tiempo.year)}] - ({tiempo.hour}:{tiempo.minute}:{tiempo.second}) - " + request.environ['REMOTE_ADDR'] + "\n")
    file.close()
  else:
    file = open("ip_logs.html", "a+")
    file.write(f"[{tiempo.day}/{tiempo.month}/{(tiempo.year)}] - ({tiempo.hour}:{tiempo.minute}:{tiempo.second}) - " + request.environ['HTTP_X_FORWARDED_FOR'] + "\n")
    file.close()


web = Flask(
  __name__,
  template_folder='templates',
  static_folder='static'
)


@web.errorhandler(404)
def not_found(e):
  log()
  return render_template("./templates/index.html")


@web.route('/', methods=["GET"])
def home():
  log()
  #return render_template('index.html')
  return render_template("index.html")


if __name__ == '__main__':
    web.run(
    host='0.0.0.0',
    debug=False,
    port=8080
    )