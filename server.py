import zmq
import pandas as pd
import json
import time


PORT = "tcp://*:3000"

# creates the socket object and binds it to a port
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind(PORT)

while True:
    print("Waiting for request...")
    
    # receives the message sent and converts it to a string
    request = socket.recv()
    request = request.decode('utf-8')
    print(f"Received: {request}")

    time.sleep(1)

    user_request = request

    # uses dataframe to access data in excel file
    excel_path = "clown_companies.csv"
    df = pd.read_csv(excel_path)

    # determines index of the company in the request
    companyList = [x for x in df['Company Name']]
    index = companyList.index(user_request)

    # extracts data about the company
    name = df['Company Name'][index]
    price = df['Price (per hour)'][index]
    min = df['Min Hours'][index]
    max = df['Max Hours'][index]

    # appends data to dictionary object
    result = {}
    result["Name"] = f"{name}"
    result["Price"] = f"{price}"
    result["Min Hours"] = f"{min}"
    result["Max Hours"] = f"{max}"

    # sends dictionary as JSON reply back to client
    print(f"Sending: {result}")
    socket.send_json(result)