Step 1: Code for Each VM 
VM 1: Current Time Service  

This microservice will return the current time when accessed. 

# vm1_time_service.py
from flask import Flask
from datetime import datetime

app = Flask(_name_)

@app.route('/time', methods=['GET'])
def get_time():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {"current_time": current_time}

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=5001)
