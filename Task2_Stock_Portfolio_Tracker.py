# ============================================================
#   CodeAlpha Python Internship
#   Task 2: Stock Portfolio Tracker
#   Concepts: dictionary, input/output, basic arithmetic,
#             file handling (optional)
# ============================================================

import csv
import os

# Hardcoded stock prices (dictionary)
STOCK_PRICES = {
    "AAPL":  180.00,   # Apple
    "TSLA":  250.00,   # Tesla
    "GOOGL": 140.00,   # Google
    "AMZN":  185.00,   # Amazon
    "MSFT":  415.00,   # Microsoft
    "META":  500.00,   # Meta
    "NFLX":  620.00,   # Netflix
    "NVDA":  875.00,   # NVIDIA
}


def show_available_stocks() -> None:
    """Display all available stocks and their prices."""
    print("\n" + "=" * 40)
    print(f"  {'Symbol':<8} {'Company':<12} {'Price (USD)':>10}")
    print("=" * 40)
    names = {
        "AAPL": "Apple", "TSLA": "Tesla", "GOOGL": "Google",
        "AMZN": "Amazon", "MSFT": "Microsoft", "META": "Meta",
        "NFLX": "Netflix", "NVDA": "NVIDIA",
    }
    for symbol, price in STOCK_PRICES.items():
        print(f"  {symbol:<8} {names[symbol]:<12} ${price:>9.2f}")
    print("=" * 40)


def get_portfolio() -> dict:
    """Prompt user to input stock names and quantities. Returns portfolio dict."""
    portfolio = {}
    print("\nEnter your stock holdings.")
    print("Type 'done' when finished.\n")

    while True:
        symbol = input("Stock symbol (e.g. AAPL): ").upper().strip()

        if symbol == "DONE":
            break

        if symbol not in STOCK_PRICES:
            print(f"  ⚠️  '{symbol}' not found. Available: {', '.join(STOCK_PRICES.keys())}\n")
            continue

        try:
            qty = int(input(f"  Quantity of {symbol}: ").strip())
            if qty <= 0:
                print("  ⚠️  Quantity must be a positive number.\n")
                continue
        except ValueError:
            print("  ⚠️  Please enter a valid whole number.\n")
            continue

        if symbol in portfolio:
            portfolio[symbol] += qty
        else:
            portfolio[symbol] = qty

        print(f"  ✅ Added {qty} share(s) of {symbol}.\n")

    return portfolio


def calculate_portfolio(portfolio: dict) -> list:
    """Calculate value of each holding. Returns list of result rows."""
    results = []
    for symbol, qty in portfolio.items():
        price = STOCK_PRICES[symbol]
        total = price * qty
        results.append({
            "symbol": symbol,
            "quantity": qty,
            "price": price,
            "total": total,
        })
    return results


def display_portfolio(results: list) -> float:
    """Print a formatted portfolio summary table. Returns grand total."""
    print("\n" + "=" * 60)
    print("              📊 YOUR STOCK PORTFOLIO SUMMARY")
    print("=" * 60)
    print(f"  {'Symbol':<8} {'Qty':>6} {'Price (USD)':>12} {'Value (USD)':>14}")
    print("-" * 60)

    grand_total = 0.0
    for row in results:
        print(f"  {row['symbol']:<8} {row['quantity']:>6} "
              f"${row['price']:>11.2f} ${row['total']:>13.2f}")
        grand_total += row["total"]

    print("-" * 60)
    print(f"  {'TOTAL INVESTMENT':.<40} ${grand_total:>13.2f}")
    print("=" * 60)
    return grand_total


def save_results(results: list, grand_total: float) -> None:
    """Ask user whether to save results to .txt or .csv file."""
    choice = input("\nSave results? (txt / csv / no): ").lower().strip()

    if choice == "txt":
        filename = "portfolio_result.txt"
        with open(filename, "w") as f:
            f.write("STOCK PORTFOLIO SUMMARY\n")
            f.write("=" * 50 + "\n")
            f.write(f"{'Symbol':<8} {'Qty':>6} {'Price':>12} {'Value':>14}\n")
            f.write("-" * 50 + "\n")
            for row in results:
                f.write(f"{row['symbol']:<8} {row['quantity']:>6} "
                        f"${row['price']:>11.2f} ${row['total']:>13.2f}\n")
            f.write("-" * 50 + "\n")
            f.write(f"TOTAL INVESTMENT: ${grand_total:.2f}\n")
        print(f"  ✅ Saved to '{filename}'")

    elif choice == "csv":
        filename = "portfolio_result.csv"
        with open(filename, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["symbol", "quantity", "price", "total"])
            writer.writeheader()
            writer.writerows(results)
            writer.writerow({"symbol": "TOTAL", "quantity": "", "price": "", "total": grand_total})
        print(f"  ✅ Saved to '{filename}'")

    else:
        print("  Results not saved.")


def main():
    print("=" * 60)
    print("       💹 CodeAlpha Stock Portfolio Tracker")
    print("=" * 60)

    show_available_stocks()
    portfolio = get_portfolio()

    if not portfolio:
        print("\n⚠️  No stocks entered. Exiting.")
        return

    results = calculate_portfolio(portfolio)
    grand_total = display_portfolio(results)
    save_results(results, grand_total)

    print("\nThank you for using Stock Portfolio Tracker! 👋\n")


if __name__ == "__main__":
    main()
