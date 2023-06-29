import datetime as dt
from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
TOKEN: Final = '6276661689:AAE-7JijKvJuYjjdLMSlCYHZllOg-v-xSsk'
BOT_USERNAME: Final = '@season_farmtogether_bot'

def season(current_time):
    one_year = 17*60*4
    one_season = 17*60
    season = ["Spring","Summer","Autumn","Winter"]
    part = int((current_time%one_year)//one_season)
    time_in_season = int((current_time%one_year)%one_season)
    m, s = divmod(time_in_season, 60)
    return season[part]+f' at {m:02d}:{s:02d}'
   

def annonce():
    stamp_Duc = dt.datetime(2023,6,11,18,22,42)
    stamp_Anh = dt.datetime(2023,6,11,18,13,22)
    current_time_Duc = (dt.datetime.now() - stamp_Duc).total_seconds()
    current_time_Anh = (dt.datetime.now() - stamp_Anh).total_seconds()
    return 'Season of Ngoc Anh is '+season(current_time_Anh)+'\nSeason of Duc is '+season(current_time_Duc)


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! Thank for chatting with me! I am a season-check bot')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Please type something so I can respond')

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('It is for custom')

#Respones

def handle_response(text:str) -> str:
    processed: str = text.lower()

    if 'check' in processed:
        return annonce() 
       
    return "I don't understand your commands"

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    response: str = handle_response(text)
    
    print('Bot:', response)
    await update.message.reply_text(response)
    

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')




if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler('start',start_command))
    app.add_handler(CommandHandler('help',help_command))
    app.add_handler(CommandHandler('custom',custom_command))


    app.add_handler(MessageHandler(filters.TEXT,handle_message))

    app.add_error_handler(error)


    

    print('Polling...')
    app.run_polling(poll_interval=3 )