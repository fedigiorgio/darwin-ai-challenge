import TelegramBot from 'node-telegram-bot-api'

function newTelegramBot(env) {
    return new TelegramBot(env.TELEGRAM_TOKEN, {polling: true});
}

function listen(bot) {
    bot.on('message', (msg) => {
        const chatId = msg.chat.id;
        const message = msg.text;

        console.log(`${chatId} - ${message}`);

        bot.sendMessage(chatId, `Recibido: ${message}`);
    });
}

export function start(env){
    const bot = newTelegramBot(env);
    listen(bot);
}

