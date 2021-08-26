import time
import sys
from flask import Flask, render_template, redirect
from bot.bot import Bot

app = Flask(__name__)

bot = Bot()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/reaction_test/", methods=['POST'])
def reaction_test():
    bot.ReactionTest()
    return redirect("/")

@app.route("/aim_test/", methods=['POST'])
def aim_test():
    bot.AimTest()
    return redirect("/")

@app.route("/memory_test/", methods=['POST'])
def memory_test():
    bot.MemoryTest()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)