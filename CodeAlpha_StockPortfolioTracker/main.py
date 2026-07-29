import csv

stock_prices = {
    "AAPL": 15000,
    "TSLA": 20000,
    "MSFT": 35000,
    "GOOGL": 18000,
    "AMZN": 25000
}

portfolio = []


def display_stocks():
    print("\n========================================")
    print("         AVAILABLE STOCKS")
    print("========================================")

    for stock, price in stock_prices.items():
        print(f"{stock} - ₹{price:,.2f}")


def add_stock():
    display_stocks()

    stock_symbol = input("\nEnter stock symbol: ")
    stock_symbol = stock_symbol.strip().upper()

    print("You entered:", stock_symbol)

    if stock_symbol not in stock_prices:
        print("\n❌ Invalid stock symbol.")
        print("Please choose a stock from the available list.")
        return

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("\n❌ Quantity must be greater than 0.")
            return

    except ValueError:
        print("\n❌ Please enter a valid whole number.")
        return

    price = stock_prices[stock_symbol]

    investment = price * quantity

    stock_data = {
        "stock": stock_symbol,
        "quantity": quantity,
        "price": price,
        "investment": investment
    }

    portfolio.append(stock_data)

    print("\n✅ Stock added successfully!")
    print(f"Stock: {stock_symbol}")
    print(f"Quantity: {quantity}")
    print(f"Price per share: ₹{price:,.2f}")
    print(f"Investment value: ₹{investment:,.2f}")


def display_portfolio():
    if not portfolio:
        print("\n⚠️ Your portfolio is empty.")
        return
    
    print("\n========================================")
    print("           YOUR PORTFOLIO")
    print("========================================")

    total_investment = 0

    print(
        f"{'Stock':<10}"
        f"{'Quantity':<10}"
        f"{'Price':<15}"
        f"{'Investment':<15}"
    )

    print("-" * 50)

    for item in portfolio:
        print(
            f"{item['stock']:<10}"
            f"{item['quantity']:<10}"
            f"₹{item['price']:<14,.2f}"
            f"₹{item['investment']:<14,.2f}"
        )

        total_investment += item["investment"]

    print("-" * 50)
    print(f"Total Investment: ₹{total_investment:,.2f}")


def calculate_total():
    if not portfolio:
        print("\n⚠️ Your portfolio is empty.")
        return

    total_investment = 0

    for item in portfolio:
        total_investment += item["investment"]

    print("\n========================================")
    print("       TOTAL INVESTMENT")
    print("========================================")
    print(f"Your total investment is: ₹{total_investment:,.2f}")



def save_portfolio():
    if not portfolio:
        print("\n⚠️ Your portfolio is empty.")
        return

    try:
        with open("portfolio.csv", "w", newline="") as file:

            fieldnames = [
                "Stock",
                "Quantity",
                "Price",
                "Investment"
            ]

            writer = csv.DictWriter(
                file,
                fieldnames=fieldnames
            )

            writer.writeheader()

            for item in portfolio:
                writer.writerow({
                    "Stock": item["stock"],
                    "Quantity": item["quantity"],
                    "Price": item["price"],
                    "Investment": item["investment"]
                })

        print("\n✅ Portfolio saved successfully!")
        print("File created: portfolio.csv")
        
    except Exception as error:
        print("\n❌ Error while saving portfolio.")
        print(error)



def main():

    print("========================================")
    print("       STOCK PORTFOLIO TRACKER")
    print("========================================")

    print("\nWelcome to your Stock Portfolio Tracker!")

    while True:

        print("\n========================================")
        print("              MAIN MENU")
        print("========================================")
        print("1. View Available Stocks")
        print("2. Add Stock to Portfolio")
        print("3. View My Portfolio")
        print("4. Calculate Total Investment")
        print("5. Save Portfolio to CSV")
        print("6. Exit")

        choice = input("\nEnter your choice (1-6): ").strip()

        if choice == "1":
            display_stocks()

        elif choice == "2":
            add_stock()

        elif choice == "3":
            display_portfolio()

        elif choice == "4":
            calculate_total()

        elif choice == "5":
            save_portfolio()

        elif choice == "6":
            print("\nThank you for using Stock Portfolio Tracker!")
            print("Goodbye! 👋")
            break

        else:
            print("\n❌ Invalid choice.")
            print("Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()