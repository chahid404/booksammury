import chatgpt_engine
import csv_engine
from telegram_lib import TelegramBot
import summary
import csv
# import schedule
import time
TOKEN = '6435664758:AAFeD-yJ6c8HStj14YHDvm2jC3BlieNgeuw'
CHAT_ID = '6209734296'



def send_message(message):
    bot = TelegramBot(TOKEN, CHAT_ID)
    bot.send_message(message)

def books():
    with open(r'data/top books.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(row['Title'])
    

def main():
    book = csv_engine.books()
    print(f"Book Title : {book['Title']} , author : {book['Author']}")
    propt = summary.generate_summary_prompt_v2(book['Title'],book['Author'],"Arabic")
    res = chatgpt_engine.chat_with_chatgpt4(propt)
    send_message(res)

# def job():
#     main()

# schedule.every().day.at("22:04").do(job)
print("book summary service is running ...")
main()

# while True:
#     schedule.run_pending()
#     time.sleep(60)