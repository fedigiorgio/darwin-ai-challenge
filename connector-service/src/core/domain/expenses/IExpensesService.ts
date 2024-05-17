import {TelegramId} from "../TelegramId";
import {Message} from "../Message";
import {Expenses} from "./Expenses";

export interface IExpensesService {
    add(telegramId: TelegramId, message: Message): Promise<Expenses>;
}