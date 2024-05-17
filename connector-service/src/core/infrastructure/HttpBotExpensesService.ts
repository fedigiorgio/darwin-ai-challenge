import {IExpensesService} from "../domain/expenses/IExpensesService";
import {TelegramId} from "../domain/TelegramId";
import {Message} from "../domain/Message";
import {Expenses} from "../domain/expenses/Expenses";

export class HttpBotExpensesService implements IExpensesService {
    add(telegramId: TelegramId, message: Message): Promise<Expenses> {
        return Promise.resolve({category: "Healthcare", value: 20})
    }

}