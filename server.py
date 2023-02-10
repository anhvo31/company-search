import zmq
import pandas as pd
import json
import time


PORT = "tcp://*:3000"

# Creates the socket object and binds it to a port
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind(PORT)

while True:
    print("Waiting for request...")
    
    # Receives the message sent and converts it to a string
    request = socket.recv()
    request = request.decode('utf-8')
    print(f"Received: {request}")

    time.sleep(1)

    user_request = request

    # Uses dataframe to access data in excel file
    excel_path = "clown_companies.csv"
    df = pd.read_csv(excel_path)

    company_list = [x for x in df['Company Name']]

    try:
        # Determines index of the company in the request
        index = company_list.index(user_request)
    except ValueError:
        print("Company does not exist")
        socket.send(b'Company does not exist')
        continue
    except KeyboardInterrupt:
        print("Closing socket...")
        break
    else:
        # Extracts data about the company
        name = df['Company Name'][index]
        price = df['Price (per hour)'][index]
        min_hours = df['Min Hours'][index]
        max_hours = df['Max Hours'][index]

        # Appends data to dictionary object
        result = {"Name": f"{name}", "Price": f"{price}", "Min Hours": f"{min_hours}", "Max Hours": f"{max_hours}"}

        # Sends dictionary as JSON reply back to client
        print(f"Sending: {result}")
        socket.send_json(result)