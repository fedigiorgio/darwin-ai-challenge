import * as http from 'http';

const PORT: number = 3000;

const server: http.Server = http.createServer((req: http.IncomingMessage, res: http.ServerResponse) => {
    res.writeHead(200, {'Content-Type': 'text/plain'});
    res.end('This a dummy response');
});


export function listenDummyServer() {
    server.listen(PORT, () => {
        console.log(`Listen ${PORT}`);
    });
}

