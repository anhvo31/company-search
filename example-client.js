/* 
Citation for setting up socket
Date: 02/13/2023
Adapted from ZeroMQ.org
Source URL: https://zeromq.org/get-started/?language=nodejs#

Client is for testing purposes.
This test client is written using Node.js and ZeroMQ.
To install the ZeroMQ package, run the following: npm install zeromq@6.0.0-beta.16
*/

async function runCompanySearch() {
    /*
    Sends a request containing the string in the variable userInput to the server at port 3000.
    Converts response to a JSON.
    */
    const zmq = require("zeromq");
    const PORT = 'tcp://localhost:3000';

    // Creates socket and connect to port
    const socket = new zmq.Request();
    socket.connect(PORT);

    // Variable to hold message sent to the server. Example used here is to receive data on a clown company called "Starlights"
    let userInput = "Starlights";

    console.log("Sending", userInput);
    await socket.send(userInput);

    const [result] = await socket.receive();
    const result_string = result.toString();

    try {
        const result_JSON = JSON.parse(result_string)
        console.log("Received: ", result_JSON);

        /* 
        Example on how to extract info from JSON:
            let price = result_JSON["price"];
            console.log(price);
        */

    } catch (SyntaxError) {
        console.log(result_string);
    }
}

// How to call the function
runCompanySearch()

/* 
Example on how to export the function for use in other files:
    exports.runCompanySearch = runCompanySearch;
*/