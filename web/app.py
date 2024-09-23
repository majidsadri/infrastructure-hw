from flask import Flask, render_template, Response
from kafka import KafkaConsumer

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def stream():
    consumer = KafkaConsumer('hello-world-topic', bootstrap_servers='kafka:9092')
    for message in consumer:
        yield f"data: {message.value.decode('utf-8')}\n\n"

@app.route('/stream')
def stream_view():
    return Response(stream(), mimetype="text/event-stream")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
