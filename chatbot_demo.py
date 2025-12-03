import datetime
import pytz  
import ollama
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Set your timezone (replace with your own if needed)
TIMEZONE = "Asia/Kolkata"

def time_based_greeting():
    local_time = datetime.datetime.now(pytz.timezone(TIMEZONE))
    hour = local_time.hour
    if 5 <= hour < 12:
        return "Good morning"
    elif 12 <= hour < 17:
        return "Good afternoon"
    elif 17 <= hour < 21:
        return "Good evening"
    else:
        return "Good night"

def chat_with_ollama(user_input):
    response = ollama.chat(
        model="llama3.1",
        messages=[{"role": "user", "content": user_input}]
    )
    return response['message']['content']

def main():
    print(Fore.CYAN + "=" * 60)
    print(Fore.YELLOW + "     Python Mini Project: smart chat bot")
    print(Fore.CYAN + "=" * 60 + "\n")

    # Ask user for their name
    username = input(Fore.MAGENTA + "Enter your name: " + Fore.WHITE)

    # Generate custom greeting based on local time
    greeting = time_based_greeting()
    print(Fore.GREEN + f"\n{greeting}, {username}! "
          + Fore.WHITE + "I am your chatbot. How can I help you?\n")

    # Chat loop
    while True:
        user_input = input(Fore.BLUE + f"{username}: " + Fore.WHITE)
        if user_input.lower() in ["exit", "quit", "bye"]:
            print(Fore.MAGENTA + f"Chatbot: Goodbye {username}! Have a great day!")
            break
        print(Fore.CYAN + "Chatbot is thinking...\n")
        bot_reply = chat_with_ollama(user_input)
        print(Fore.GREEN + "chatbot: " + Fore.WHITE + bot_reply + "\n")

if __name__ == "__main__":
    main()
