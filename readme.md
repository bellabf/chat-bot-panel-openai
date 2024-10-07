# Chat Interface with OpenAI and Panel

This repository contains two Python scripts that create a chat interface using OpenAI's API and the Panel library. The interface allows for interaction with OpenAI's models and displays chat messages in a web-based UI.

# Prerequisites

Make sure you have Python 3.8 or higher installed on your machine.
The instructions will vary according to the tools that you use, but it should be something like this.

```bash
conda create -n "new_env"
conda activate "new_env
pip install -r requirements.txt
```

# OpenAI API Key

You'll need an OpenAI API key to use this project. Create a .env file in the root directory of the project, and add your API key as follows:

```bash
OPENAI_API_KEY=your_openai_api_key_here
```

Make sure to replace your_openai_api_key_here with your actual OpenAI API key. If you are pushing this code to a public repo, don't forget to add `.env` to your `.gitignore`.

# Running the Project

You can run the chat interface by executing the Python script:


```bash
python chat-template.py
```

This will start a local server, and the interface should be accessible in your browser (something like at http://localhost:5006).

## Project Files
- chat-template.py: Main script that runs the chat interface using OpenAI and Panel.
- chat-template-prompt.py: A helper file that handles prompts and other utilities for the interface.

## Contributing
Feel free to submit issues or pull requests to improve the project. Contributions are always welcome!

