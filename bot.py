import os
from telegram import Update, LabeledPrice
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, PreCheckoutQueryHandler

# СЮДА ВСТАВЛЯЕМ ТОКЕН (между кавычек)
TOKEN = "ВАШ_ТОКЕН_ТУТ"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Привет! Я твой AI-помощник.\n"
        "Чтобы активировать доступ, используй команду /buy"
    )

async def buy(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.message.chat_id
    title = "Доступ к AI"
    description = "Подписка на генерацию текстов и фото"
    payload = "ai-sub"
    currency = "XTR" # Звезды Telegram
    prices = [LabeledPrice("Premium", 100)] # 100 звезд

    await context.bot.send_invoice(
        chat_id, title, description, payload, "", currency, prices
    )

async def precheckout_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.pre_checkout_query
    await query.answer(ok=True)

if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("buy", buy))
    app.add_handler(PreCheckoutQueryHandler(precheckout_callback))
    print("Бот запущен...")
    app.run_polling()
