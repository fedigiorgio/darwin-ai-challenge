import {IExpensesService, NotAnExpensesError, UnauthorizedUserError} from "../domain/expenses/IExpensesService";
import {TelegramId} from "../domain/TelegramId";
import {Message} from "../domain/Message";
import {Expenses} from "../domain/expenses/Expenses";
import axios, {AxiosResponse} from "axios";

interface ExpensesResponse {
    description: string
    amount: number
    category: string
    added_at: string
}

interface GetExpensesResponse {
    expenses: ExpensesResponse[]
}

interface AddExpensesRequest {
    message: string;
}

export class HttpBotExpensesService implements IExpensesService {
    private readonly baseUrl: string;

    constructor(baseUrl: string) {
        this.baseUrl = baseUrl;
    }

    async get(telegramId: TelegramId): Promise<Expenses[]> {
        const url = this.expensesUrl(telegramId);
        const response: AxiosResponse<GetExpensesResponse> = await axios.get(url);
        return this.mapResponse(response, items => items.expenses.map(e => this.toExpenses(e)))
    }

    async add(telegramId: TelegramId, message: Message): Promise<Expenses> {
        const url = this.expensesUrl(telegramId);
        const body = this.createRequest(message);
        const response: AxiosResponse<ExpensesResponse> = await axios.post(url, body);
        return this.mapResponse(response, this.toExpenses)
    }

    private createRequest(message: Message): AddExpensesRequest {
        return {
            message: message.value
        };
    }

    private expensesUrl(telegramId: TelegramId): string {
        return `${this.baseUrl}/api/telegram-users/${telegramId.value}/expenses`;
    }


    private mapResponse<T>(response: AxiosResponse<T>, toDomain: (body: T) => any): any {
        if (response.status === 200) {
            const body = response.data;
            return toDomain(body);
        } else if (response.status === 400) {
            throw new NotAnExpensesError;
        } else if (response.status === 401) {
            throw new UnauthorizedUserError();
        } else {
            throw new Error(`Unexpected error from bot-service: ${response.status}`);
        }
    }


    private toExpenses(body: ExpensesResponse) {
        return {
            amount: body.amount,
            addedAt: body.added_at,
            description: body.description,
            category: body.category
        };
    }
}