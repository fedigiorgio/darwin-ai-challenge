import {ExpensesTelegramBotListener} from './telegram/ExpensesTelegramBotListener';
import dotenv from 'dotenv';
import {HttpBotExpensesService} from "./core/infrastructure/HttpBotExpensesService";
import {AddExpenses} from "./core/use_cases/AddExpenses";
import TelegramBot from "node-telegram-bot-api";

dotenv.config();

const expensesService = new HttpBotExpensesService();
const addExpenses = new AddExpenses(expensesService);
const telegramBot = new TelegramBot(process.env.TELEGRAM_TOKEN!, {polling: true});
const expensesTelegramBotListener = new ExpensesTelegramBotListener(telegramBot, addExpenses);

expensesTelegramBotListener.listen();

