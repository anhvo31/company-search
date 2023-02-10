/* 
Client is for testing purposes.
Server for company search uses ZeroMQ.
As such, this test client is written in Node.JS using ZeroMQ.
Install the ZeroMQ package: npm install zeromq@6.0.0-beta.16
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

    // Variable to hold message sent to the server
    // Example used here is to receive data on a clown company called "Starlights"
    let userInput = "Starlights";

    console.log("Sending", userInput);
    await socket.send(userInput);

    const [result] = await socket.receive();
    const result_string = result.toString();

    try {
        console.log("Received: ", result_string);
        const result_JSON = JSON.parse(result_string)

        /* 
        Example on how to extract info from JSON:
            let price = result_JSON["Price"];
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