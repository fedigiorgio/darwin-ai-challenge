import {IExpensesService} from "../domain/expenses/IExpensesService";
import {TelegramId} from "../domain/TelegramId";
import {Message} from "../domain/Message";
import {Expenses} from "../domain/expenses/Expenses";

export class AddExpenses {
    constructor(private readonly expensesService: IExpensesService) {
    }

    async execute(telegramId: TelegramId, message: Message): Promise<Expenses> {
        return await this.expensesService.add(telegramId, message);
    }
}