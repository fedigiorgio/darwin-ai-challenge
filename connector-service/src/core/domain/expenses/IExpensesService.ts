import {TelegramId} from "../TelegramId";
import {Message} from "../Message";
import {Expenses} from "./Expenses";



export class NotAnExpensesError extends Error {
}

export class UnauthorizedUserError extends Error {
}


export interface IExpensesService {
    add(telegramId: TelegramId, message: Message): Promise<Expenses>;

    get(telegramId: TelegramId): Promise<Expenses[]>;
}