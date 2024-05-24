import {IExpensesService} from "../domain/expenses/IExpensesService";
import {TelegramId} from "../domain/TelegramId";
import {Message} from "../domain/Message";
import {Expenses} from "../domain/expenses/Expenses";
import axios, {AxiosResponse} from "axios";

interface ExpensesResponse {
    category: string;
}

interface AddExpensesRequest {
    telegram_id: string;
    message: string;
}

export class HttpBotExpensesService implements IExpensesService {
    private readonly url: string

    constructor(baseUrl: string) {
        this.url = `${baseUrl}/api/expenses`
    }

    async add(telegramId: TelegramId, message: Message): Promise<Expenses> {
        const body = this.createRequest(telegramId, message)
        const response: AxiosResponse<ExpensesResponse> = await this.post(body)
        return this.toDomain(response)
    }

    private createRequest(telegramId: TelegramId, message: Message): AddExpensesRequest {
        return {
            telegram_id: telegramId.value,
            message: message.value
        };
    }

    private async post(body: AddExpensesRequest) {
        return await axios.post(this.url, body);
    }


    private toDomain(response: AxiosResponse<ExpensesResponse>): Expenses {
        if (response.status == 200) {
            const body = response.data
            return {
                category: body.category
            };
        }
        else if (response.status === 400) {
            throw new Error('Message is not an expense');
        } else if (response.status === 500) {
            throw new Error('Bot service fail');
        } else {
            throw new Error(`Unexpected error from bot-service: ${response.status}`);
        }

    }
}