# stock_portfolio_tracker.py

import csv

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 125
}

def calculate_investment():
    print("📊 Welcome to the Stock Portfolio Tracker!")
    portfolio = {}

    while True:
        stock = input("Enter stock symbol (AAPL, TSLA, etc.): ").upper()
        if stock not in stock_prices:
            print("❌ Stock not found in price list.")
            continue

        try:
            quantity = int(input(f"Enter quantity of {stock} shares: "))
        except ValueError:
            print("❌ Please enter a valid number.")
            continue

        portfolio[stock] = portfolio.get(stock, 0) + quantity

        more = input("Add another stock? (y/n): ").lower()
        if more != 'y':
            break

    total_value = 0
    print("\n💼 Your Portfolio Summary:")
    for stock, qty in portfolio.items():
        value = stock_prices[stock] * qty
        total_value += value
        print(f"{stock} - {qty} shares @ ${stock_prices[stock]} = ${value}")

    print(f"\n🧮 Total Investment Value: ${total_value}")

    # Optional: Save to CSV
    save = input("Would you like to save this to a CSV file? (y/n): ").lower()
    if save == 'y':
        with open("portfolio_summary.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Stock", "Quantity", "Price", "Total Value"])
            for stock, qty in portfolio.items():
                writer.writerow([stock, qty, stock_prices[stock], stock_prices[stock]*qty])
            writer.writerow(["", "", "Total", total_value])
        print("✅ Portfolio saved to 'portfolio_summary.csv'")

if __name__ == "__main__":
    calculate_investment()
