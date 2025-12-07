from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Rikesh v4 – updated via Jenkins CI/CD on Kubernetes!"
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
