import TelegramBot from 'node-telegram-bot-api';
import {TelegramId} from "../core/domain/TelegramId";
import {Message} from "../core/domain/Message";
import {Dispatcher} from "../core/use_cases/Dispatcher";
import {NotAnExpensesError, UnauthorizedUserError} from "../core/domain/expenses/IExpensesService";


export class ExpensesTelegramBotListener {
    constructor(private readonly telegramBot: TelegramBot, private readonly dispatcher: Dispatcher) {
    }

    listen() {
        this.telegramBot.on('message', (msg) => {
            try {
                const telegramId = new TelegramId(msg.chat.id.toString());
                const message = new Message(msg.text!!);

                this.dispatcher.execute(telegramId, message)
                    .then(r => this.telegramBot.sendMessage(msg.chat.id, r.message))
                    .catch(e => this.handleError(e, message, telegramId));
            }
            catch(error) {
                console.error("Unexpected error", error);
            }
        });
    }

    private handleError(error: Error, message: Message, telegramId: TelegramId): void {
        if (error instanceof UnauthorizedUserError) {
            console.error(`User with ${telegramId.value} is not authorized`);
        } else if (error instanceof NotAnExpensesError) {
            console.warn(`Message ${message.value} is not recognized as an expense, user: ${telegramId.value}`);
        } else {
            console.error(`Unexpected error with message: ${message.value} and user: ${telegramId.value}`, error);
        }
    }

}