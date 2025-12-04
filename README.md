chatbot_demo.py         → Main chatbot script  
README.md          → Project documentation  
venv/              → Python virtual environment  
1 Create a virtual environment *git clone https://github.com/your-username/your-repo-name.git
cd chatbot_using_ollama

2 Install required Python modules
pip install ollama colorama pytz anyio httpx pydantic pydantic-core annotated-types typing-inspection sniffio

 3 Install Ollama (Linux / WSL)
curl -fsSL https://ollama.com/install.sh | sh


4 Verify installation:

ollama --version

 5 Start the Ollama server
ollama serve


Keep this terminal open.

6 Download the LLaMA model
ollama pull llama3.1

7️ Run the chatbot

Open a new terminal:

cd your-repo-name
source venv/bin/activate
python3 chatbot.py

 How It Works
Time-Based Greeting

The program uses datetime + pytz to detect your local time and greet accordingly.

 Local AI using Ollama

The chatbot sends user input to:

ollama.chat(model="llama3.1")


which gives local LLM responses.

Colored Terminal UI

Colorama adds colors like:

Yellow → Title

Green → Greeting

Blue → User input

Magenta → Chatbot exit message

Example Output
============================================================
     Python Mini Project: Smart Chatbot with Colors
============================================================

Enter your name: vishnu

Good evening, vishnu! I am your chatbot. How can I help you?

vishnu: hello bot
Chatbot is thinking...

Chatbot: Hello! How can I assist you today?
