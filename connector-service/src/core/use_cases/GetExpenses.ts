import {IExpensesService} from "../domain/expenses/IExpensesService";
import {TelegramId} from "../domain/TelegramId";
import {Expenses} from "../domain/expenses/Expenses";
import {format} from "./Utils";
import {ResponseChat} from "./ResponseChat";

export class GetExpenses {
    constructor(private readonly expensesService: IExpensesService) {
    }

    async execute(telegramId: TelegramId): Promise<ResponseChat> {
        return this.toResponseChat(await this.expensesService.get(telegramId));
    }

    toResponseChat(expenses: Expenses[]): ResponseChat {
        const message = expenses.map(expense => {
            return `📅 Added at: ${expense.addedAt}\n💵 Amount: $${expense.amount}\n🧾 Category: ${format(expense.category)}\n✅ Description: ${expense.description}\n`;
        }).join('\n');

        return {message: message};
    }

}