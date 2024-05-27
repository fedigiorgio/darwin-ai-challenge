export class Message {
    constructor(
        public readonly value: string,
    ) {
        if (!value) {
            throw new Error("Message cannot be empty.")
        }
    }

    isListExpenses(): boolean{
        return this.value === '/list-expenses';
    }

    isTelegramId(): boolean {
        return this.value === '/telegram-id';
    }
}