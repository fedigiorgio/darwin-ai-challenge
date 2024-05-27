import net from "net";

const dummyServer: net.Server = net.createServer((socket: net.Socket) => {
    socket.on('data', (data: Buffer) => {});

    socket.on('end', () => {});
});

export function listenDummyServer() {
    const port = 3000
    dummyServer.listen(port, () => {
        console.log(`Listen port: ${port}`);
    });
}
