class DataFormatter:
   ```python
    @staticmethod
    def format_data(data):
        # This method should be implemented based on the structure of the data
        formatted_data = ""
        for item in data:
            formatted_data += f"Name: {item['name']}\nPrice: {item['price']}\nLink: {item['link']}\n\n"
        return formatted_data
