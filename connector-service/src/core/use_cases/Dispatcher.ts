import {TelegramId} from "../domain/TelegramId";
import {Message} from "../domain/Message";
import {GetExpenses} from "./GetExpenses";
import {AddExpenses} from "./AddExpenses";
import {ResponseChat} from "./ResponseChat";

export class Dispatcher {
    constructor(private readonly getExpenses: GetExpenses, private readonly addExpenses: AddExpenses) {
    }

    async execute(telegramId: TelegramId, message: Message): Promise<ResponseChat> {
        console.log(`Received message: ${message.value} from telegramId: ${telegramId.value}`);

        if (message.isListExpenses())
            return await this.getExpenses.execute(telegramId);
        else if (message.isTelegramId())
            return {
                message: telegramId.value
            }
        else
            return this.addExpenses.execute(telegramId, message);
    }
}