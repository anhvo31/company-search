/* 
Client is for testing purposes
Install the package: npm install zeromq@6.0.0-beta.16
Note: zeroMQ version 5 doesn't have prebuilt binaries
*/

const zmq = require("zeromq");

async function runClient() {
    /*
    Sends a request containing the string in the variable userInput to the server at port 3000.
    Converts response to a JSON.
    */
    const PORT = 'tcp://localhost:3000';

    // Creates socket and connect to port
    const socket = new zmq.Request();
    socket.connect(PORT);

    // Variable to hold message sent to the server
    // Example used here is to receive data on a clown company called "Starlights"
    let userInput = "Starlights"

    console.log("Sending ", userInput)
    await socket.send(userInput);

    const [result] = await socket.receive();

    // Converts result(byte literal) to JSON
    const result_string = result.toString();
    const result_JSON = JSON.parse(result_string)

    console.log("Received: ", result_JSON);

    // Example on how to extract info from JSON
    console.log(result_JSON["Price"])

}

runClient()