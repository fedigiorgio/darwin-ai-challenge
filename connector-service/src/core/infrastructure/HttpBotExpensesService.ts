import {IExpensesService} from "../domain/expenses/IExpensesService";
import {TelegramId} from "../domain/TelegramId";
import {Message} from "../domain/Message";
import {Expenses} from "../domain/expenses/Expenses";
import axios, {AxiosResponse} from "axios";

interface ExpensesResponse {
    category: string;
}

interface AddExpensesRequest {
    telegramId: string;
    message: string;
}

export class HttpBotExpensesService implements IExpensesService {
    private readonly url: string

    constructor(baseUrl: string) {
        this.url = `${baseUrl}/expenses`
    }

    async add(telegramId: TelegramId, message: Message): Promise<Expenses> {
        const body = this.createRequest(telegramId, message)
        const response: AxiosResponse<ExpensesResponse> = await this.post(body)
        return this.toDomain(response)
    }

    private createRequest(telegramId: TelegramId, message: Message): AddExpensesRequest {
        return {
            telegramId: telegramId.value,
            message: message.value
        };
    }

    private async post(body: AddExpensesRequest) {
        return await axios.post(this.url, body);
    }


    private toDomain(response: AxiosResponse<ExpensesResponse>): Expenses {
        const body = response.data
        return {
            category: body.category
        };
    }
}