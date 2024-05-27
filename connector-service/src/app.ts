import {ExpensesTelegramBotListener} from './telegram/ExpensesTelegramBotListener';
import dotenv from 'dotenv';
import {HttpBotExpensesService} from "./core/infrastructure/HttpBotExpensesService";
import {AddExpenses} from "./core/use_cases/AddExpenses";
import TelegramBot from "node-telegram-bot-api";
import {GetExpenses} from "./core/use_cases/GetExpenses";
import {Dispatcher} from "./core/use_cases/Dispatcher";

dotenv.config();

const expensesService = new HttpBotExpensesService(process.env.BOT_SERVICE_URL!);
const getExpenses = new GetExpenses(expensesService);
const addExpenses = new AddExpenses(expensesService);
const dispatcher = new Dispatcher(getExpenses, addExpenses);
const telegramBot = new TelegramBot(process.env.TELEGRAM_TOKEN!, {polling: true});
const expensesTelegramBotListener = new ExpensesTelegramBotListener(telegramBot, dispatcher);

expensesTelegramBotListener.listen();

