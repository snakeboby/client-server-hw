const http = require('http');

const server = http.createServer((req, res) => {
    if (req.method === 'GET' && req.url === '/api/ping') {
        res.writeHead(200, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ message: 'Hello from Server!', status: 'Success' }));
    } else {
        res.writeHead(404);
        res.end();
    }
});

server.listen(3000, () => {
    console.log('[Server] Listening on port 3000...');
});