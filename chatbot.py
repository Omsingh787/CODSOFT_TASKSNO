print("🤖 ChatBot: Hello! Main aapka AI assistant hoon.")
print("🤖 ChatBot: Aap mujhse baat kar sakte hain. Exit karne ke liye 'bye' likhein.")

while True:
    user_input = input("You: ").lower().strip()

    if user_input in ["hi", "hello", "hey"]:
        print("🤖 ChatBot: Hello! Kaise ho?")

    elif "how are you" in user_input:
        print("🤖 ChatBot: Main bilkul theek hoon! Aap kaise ho?")
 
    elif "your name" in user_input:
        print("🤖 ChatBot: Mera naam CodSoft ChatBot hai.")

    elif "help" in user_input:
        print("🤖 ChatBot: Main basic questions ka answer de sakta hoon.")

    

    elif user_input in ["bye", "exit", "quit"]:
        print("🤖 ChatBot: Goodbye! Have a great day! 👋")
        break

    else:
        print("🤖 ChatBot: Sorry, main is question ko samajh nahi paaya.") 