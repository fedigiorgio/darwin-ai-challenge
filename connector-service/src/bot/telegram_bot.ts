import TelegramBot from 'node-telegram-bot-api';

function newTelegramBot(telegram_token: string): TelegramBot {
    return new TelegramBot(telegram_token, {polling: true});
}


function listen(bot: TelegramBot) {
    bot.on('message', (msg) => {
        const telegramUserId = msg.chat.id;
        const message = msg.text
        bot.sendMessage(telegramUserId, `Recibido: ${message}`);
    });
}

export function start(telegram_token: string) {
    const bot = newTelegramBot(telegram_token);
    listen(bot);
}

