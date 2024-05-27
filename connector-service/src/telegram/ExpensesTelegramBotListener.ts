import TelegramBot from 'node-telegram-bot-api';
import {AddExpenses} from "../core/use_cases/AddExpenses"
import {TelegramId} from "../core/domain/TelegramId";
import {Message} from "../core/domain/Message";
import {Dispatcher} from "../core/use_cases/Dispatcher";


export class ExpensesTelegramBotListener {
    constructor(private readonly telegramBot: TelegramBot, private readonly dispatcher: Dispatcher) {
    }

    listen() {
        this.telegramBot.on('message', (msg) => {
            const telegramId = new TelegramId(msg.chat.id.toString());
            const message = new Message(msg.text!!);

            this.dispatcher.execute(telegramId, message)
                .then(r => this.telegramBot.sendMessage(msg.chat.id, r.message))
                .catch(_ => _);
        });
    }
}