import zmq
import pandas as pd
import json
import time
import sys


PORT = "tcp://*:3000"

while True:
    try:
        # Creates the socket object and binds it to a port
        context = zmq.Context()
        socket = context.socket(zmq.REP)
        socket.bind(PORT)
        print(f"Server listening on port {PORT}...")
        
        # Receives the message sent and converts it to a string
        request = socket.recv()
        request = request.decode('utf-8')

        # Closes socket when server receives an empty string
        if not request:
            print("Closing socket...")
            time.sleep(1)
            socket.send(b'Server closed')
            sys.exit()

        print(f"Received: {request}")

        time.sleep(1)

        user_request = request

        # Uses dataframe to access data in excel file
        excel_path = "clown_companies.csv"
        df = pd.read_csv(excel_path)

        company_list = [x for x in df['Company Name']]

        # Determines index of the company in the request
        company_index = company_list.index(user_request)

        # Extracts data about the company
        name = df['Company Name'][company_index]
        price = df['Price (per hour)'][company_index]
        min_hours = df['Min Hours'][company_index]
        max_hours = df['Max Hours'][company_index]

        company_info = {"name": f"{name}", "price": f"{price}", "minHours": f"{min_hours}", "maxHours": f"{max_hours}"}

        # Sends dictionary as JSON reply to client
        print(f"Sending: {company_info}")
        socket.send_json(company_info)
    except ValueError:
        print("Company does not exist")
        socket.send(b'Company does not exist')
        continue