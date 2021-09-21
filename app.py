from flask import Flask
import os
import socket




app = Flask(__name__)

@app.route("/")
def hello():
    myHostName = socket.gethostname()
    
    inserted_id = "test-id"
    
    html = "<h3>Hello {name}!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>" \
           "<b>Lab #2:</b> Kubernetes-Acceptance <br/>" \
           "<b>Test ID:</b> {inserted_id} "
           
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname(), inserted_id=inserted_id)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8088, debug=True)
