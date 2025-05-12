import requests
import logging

API_KEY = "your_openweathermap_api_key_here"  # Replace with your API key
LOG_FILE = "app.log"


logging.basicConfig(filename=LOG_FILE, level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")


def get_weather(city):
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()

        if response.status_code != 200:
            raise ValueError(data.get("message", "Could not retrieve weather data."))

        weather_info = {
            "Temperature": f"{data['main']['temp']} °C",
            "Humidity": f"{data['main']['humidity']}%",
            "Wind Speed": f"{data['wind']['speed']} m/s"
        }

        logging.info(f"Fetched weather for {city}")
        return weather_info

    except Exception as e:
        logging.error(f"Weather error: {e}")
        return {"Error": str(e)}


def calculator():
    print("\nCalculator - Supported operations: +, -, *, /")
    try:
        num1 = float(input("Enter first number: "))
        op = input("Enter operation (+, -, *, /): ").strip()
        num2 = float(input("Enter second number: "))

        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            result = num1 / num2
        else:
            raise ValueError("Unsupported operation.")

        print(f"Result: {result}")
        logging.info(f"Calculation: {num1} {op} {num2} = {result}")

    except Exception as e:
        print(f"Error: {e}")
        logging.error(f"Calculation error: {e}")


def main():
    while True:
        print("\n=== Weather & Calculator App ===")
        print("1. Get Weather")
        print("2. Calculator")
        print("3. Exit")

        choice = input("Choose an option: ").strip()

        if choice == '1':
            city = input("Enter city name: ").strip()
            weather = get_weather(city)
            for k, v in weather.items():
                print(f"{k}: {v}")
        elif choice == '2':
            calculator()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
