import {start} from "./bot/telegram_bot.js";
import dotenv from 'dotenv';

dotenv.config();
const env = process.env
start(env);