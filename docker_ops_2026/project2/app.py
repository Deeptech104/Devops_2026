from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello deepak your  great man who is runing  inside Docker! 🚢"

if __name__ == "__main__":
    # IMPORTANT: 0.0.0.0 allows access from outside the container
    app.run(host="0.0.0.0", port=5000)
