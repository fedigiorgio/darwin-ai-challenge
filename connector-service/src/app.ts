import { start } from './bot/telegram_bot';
import dotenv from 'dotenv';

dotenv.config();
start(process.env.TELEGRAM_TOKEN!);