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
