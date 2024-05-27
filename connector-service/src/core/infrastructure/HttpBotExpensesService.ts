import {IExpensesService} from "../domain/expenses/IExpensesService";
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
        const body: AxiosResponse<GetExpensesResponse> = await axios.get(url);
        return this.mapGetResponse(body)
    }

    async add(telegramId: TelegramId, message: Message): Promise<Expenses> {
        const url = this.expensesUrl(telegramId);
        const body = this.createRequest(message);
        const response: AxiosResponse<ExpensesResponse> = await axios.post(url, body);
        return this.mapAddResponse(response);
    }

    private mapGetResponse(response: AxiosResponse<GetExpensesResponse>): Expenses[]
    {
        if (response.status == 200) {
            const body = response.data
            return body.expenses.map(e => this.toExpenses(e));
        } else if (response.status === 500) {
            throw new Error('Bot service fail');
        } else {
            throw new Error(`Unexpected error from bot-service: ${response.status}`);
        }
    }

    private createRequest(message: Message): AddExpensesRequest {
        return {
            message: message.value
        };
    }

    private expensesUrl(telegramId: TelegramId): string {
        return `${this.baseUrl}/api/telegram-users/${telegramId.value}/expenses`;
    }


    private mapAddResponse(response: AxiosResponse<ExpensesResponse>): Expenses {
        if (response.status == 200) {
            const body = response.data
            return this.toExpenses(body);
        } else if (response.status === 400) {
            throw new Error('Message is not an expense');
        } else if (response.status === 500) {
            throw new Error('Bot service fail');
        } else {
            throw new Error(`Unexpected error from bot-service: ${response.status}`);
        }

    }

    private  toExpenses(body: ExpensesResponse) {
        return {
            amount: body.amount,
            addedAt: body.added_at,
            description: body.description,
            category: body.category
        };
    }
}