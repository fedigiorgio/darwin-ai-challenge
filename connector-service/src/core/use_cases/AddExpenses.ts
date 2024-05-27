import {IExpensesService} from "../domain/expenses/IExpensesService";
import {TelegramId} from "../domain/TelegramId";
import {Message} from "../domain/Message";
import {Expenses} from "../domain/expenses/Expenses";
import {ResponseChat} from "./ResponseChat";
import {format} from "./Utils";

export class AddExpenses {
    constructor(private readonly expensesService: IExpensesService) {
    }

    async execute(telegramId: TelegramId, message: Message): Promise<ResponseChat> {
        return this.toResponseChat(await this.expensesService.add(telegramId, message));
    }

    toResponseChat(expenses: Expenses): ResponseChat {
        return  {
            message: `${format(expenses.category)} expenses added ✅`
        }
    }
}