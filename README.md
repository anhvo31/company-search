# Company Search Microservice
This project is a microservice that returns information on clown companies in an excel file. The microservice utilizes the ZeroMQ library to set client-server sockets for communication.

## Getting Started
**Communication contract**

> The following instructions are writen in python and javascript for Node.js apps. If you are using a different language, refer to [ZeroMQ](https://zeromq.org/get-started/?language=nodejs&library=zeromqjs#) documentation on how to get client socket started.

* Setting up server side socket
    * Download all files in the repo.
    * Open folder in your IDE of choice (VSCode, etc.).
    * To start server, use the following command in the terminal:
        ```
        python server.py
        ```
* Setting up client side socket
    * Create a function.
        ```
        async function runCompanySearch() {}
        ```
    * Create socket object in the function and bind it to port `tcp://localhost:3000`
        ```
        const zmq = require("zeromq");
        const socket = new zmq.Request();
        socket.connect('tcp://localhost:3000');
        ```
    * To install the necessary packages, run the following command in the terminal:
        ```
        npm install zeromq@6.0.0-beta.16
        ```
* REQUEST Data
    * An app can request data from the microservice by using the socket and calling `send()`
        ```
        await socket.send(request_string);
        ```
    * The request should be a string containing the name of the clown company that you are requesting data for.
* RECEIVE Data
    * Microservice will return:
        * Name of the company 
        * Price per hour 
        * Minimum hours 
        * Maximum hours
    * Sent data format is a JSON encoded to bytes object. Convert the data back into a JSON by adding the following to your function:
        ```
        const [result] = await socket.receive();
        const result_string = result.toString();
        const result_JSON = JSON.parse(result_string)
        ```
    * Example:
        ```
        {
            "Name": "Starlights", 
            "Price": "55", 
            "Min Hours": "2", 
            "Max Hours": "8"
        }
        ```

## Resources
* Having trouble setting up the client side socket? Refer to the file `example-client.js` for examples and comments on how to fully set one up.
* [ZeroMQ Documentation](https://zeromq.org/get-started/?language=python&library=pyzmq#)
* [ZeroMQ library for Node.js](https://github.com/zeromq/zeromq.js)
* [ZeroMQ library for Python](https://pypi.org/project/pyzmq/)
