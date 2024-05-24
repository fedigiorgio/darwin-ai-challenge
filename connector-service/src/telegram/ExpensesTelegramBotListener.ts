import TelegramBot from 'node-telegram-bot-api';
import {AddExpenses} from "../core/use_cases/AddExpenses"
import {TelegramId} from "../core/domain/TelegramId";
import {Message} from "../core/domain/Message";


export class ExpensesTelegramBotListener {
    constructor(private readonly telegramBot: TelegramBot, private readonly addExpenses: AddExpenses) {
    }

    listen() {
        this.telegramBot.on('message', (msg) => {
            const telegramId = new TelegramId(msg.chat.id.toString())
            const message = new Message(msg.text!!)

            this.addExpenses.execute(telegramId, message)
                .then(e => this.telegramBot.sendMessage(msg.chat.id, `${e.category} expenses added ✅`))
                .catch(_ => _)
        });
    }
}