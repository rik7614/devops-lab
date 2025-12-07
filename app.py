from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Rikesh Man Dangol v6 – auto-triggered deployment via Jenkins CI/CD!"
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
# dummy comment for polling
# dummy test 2 comment for polling
# dummy test 3 comment for polling
