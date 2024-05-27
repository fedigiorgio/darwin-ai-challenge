export class Message {
    constructor(
        public readonly value: string,
    ) {
        if (!value) {
            throw new Error("Message cannot be empty.")
        }
    }
}