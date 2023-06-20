from chatbot.model import ChatGPT
from chatbot.scraper import SahibindenScraper
from chatbot.formatter import DataFormatter

def main():
    chatbot = ChatGPT()
    scraper = SahibindenScraper()
    formatter = DataFormatter()

    while True:
        user_input = input("User: ")
        query = chatbot.generate_response(user_input)
        data = scraper.search(query)
        formatted_data = formatter.format_data(data)
        final_response = chatbot.generate_response(formatted_data)
        print(f"Chatbot: {final_response}")

if __name__ == "__main__":
    main()
