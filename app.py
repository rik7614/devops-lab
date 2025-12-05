from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Rikesh from DevOps Lab running in Kubernetes via Jenkins!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
