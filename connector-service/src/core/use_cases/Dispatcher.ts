import {TelegramId} from "../domain/TelegramId";
import {Message} from "../domain/Message";
import {GetExpenses} from "./GetExpenses";
import {AddExpenses} from "./AddExpenses";
import {ResponseChat} from "./ResponseChat";

export class Dispatcher {
    constructor(private readonly getExpenses: GetExpenses, private readonly addExpenses: AddExpenses) {
    }

    async execute(telegramId: TelegramId, message: Message): Promise<ResponseChat> {
        if (message.value == '/list-expenses')
            return await this.getExpenses.execute(telegramId);
        else
            return this.addExpenses.execute(telegramId, message);
    }

}