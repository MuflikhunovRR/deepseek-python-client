# DeepSeek Python Client

This is a Python client library designed to interact with the DeepSeek API, offering functionality such as chat completions and other AI-driven services. It provides an easy way to integrate DeepSeek services into Python applications.

## Features

- Chat completion with customizable parameters like model, messages, and temperature.
- Efficient error handling with detailed logs and exception management.

## Requirements

- Python 3.7 or higher
- `requests` library for API communication (install with `pip install requests`)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/deepseek-python-client.git
   cd deepseek-python-client

2. Install the required dependencies:
    
   ```bash
    pip install -r requirements.txt
   
Usage
Below is an example of how to use the DeepSeekClient to send a chat request and receive a response:

from src.deepseek.client import DeepSeekClient, ClientConfig

def main():
    config = ClientConfig(
        DEEPSEEK_API_KEY="your-api-key-here",
    )

    with DeepSeekClient(config=config) as client:
        response = client.chat.create(
            messages=[{"role": "user", "content": "Hello, how are you?"}],
            model="deepseek-chat"
        )
        print(response)


if __name__ == "__main__":
    main()

## Open to new opportunities in the US! 🇺🇸

I’m seeking ** SDET / Lead QA / QA Automation ** roles and I have **work authorization**.
Let's connect on LinkedIn: [LinkedIn](https://www.linkedin.com/in/romanmuf/)

### Key Skills & Interests:
- **QA Automation** | **SDET** | **AI** | **Machine Learning** | **Test Automation**  
- **Java** | **Selenium** | **Python** | **Postman** | **Jenkins** | **RestAssured** | **SQL** | **Pytest**  
- Passionate about leveraging **AI** and **ML** in test automation and quality assurance.

