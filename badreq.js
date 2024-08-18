const http = require('http');
const url = require('url');

// Create an HTTP server
const server = http.createServer((req, res) => {
    const queryObject = url.parse(req.url, true).query;

    // Get the 'name' parameter from the query string
    const name = queryObject.name;

    // Insecure: Reflect the 'name' parameter directly in the response without sanitizing it
    res.writeHead(200, { 'Content-Type': 'text/html' });
    res.end(`<h1>Hello, ${name}</h1>`);
});

// Start the server
server.listen(3000, () => {
    console.log('Server is running on http://localhost:3000');
});
