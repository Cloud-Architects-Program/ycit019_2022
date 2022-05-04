from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
    "https://media.giphy.com/media/mlvseq9yvZhba/giphy.gif",
    "https://media.giphy.com/media/13CoXDiaCcCoyk/giphy.gif",
    "https://media.giphy.com/media/LtVXu5s7KwlK8/giphy.gif",
    "https://media.giphy.com/media/PekRU0CYIpXS8/giphy.gif",
    "https://media.giphy.com/media/11quO2C07Sh2oM/giphy.gif",
    "https://media.giphy.com/media/12HZukMBlutpoQ/giphy.gif",
    "https://media.giphy.com/media/1HKaikaFqDt7i/giphy.gif",
    "https://media.giphy.com/media/v6aOjy0Qo1fIA/giphy.gif",
    "https://media.giphy.com/media/12bjQ7uASAaCKk/giphy.gif",
    "https://media.giphy.com/media/HFcl9uhuCqzGU/giphy.gif"
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
