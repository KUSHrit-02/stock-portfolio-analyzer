
stock_number = int(input("Enter number of stocks in your portfolio: "))

if stock_number <= 0:
    print("Please enter at least one stock.")
    raise SystemExit

total_investment = 0
total_current_value = 0
profitable_stocks = 0
loss_making_stocks = 0
no_profit_no_loss_stocks = 0
best_performing_stock = ""
highest_return = float("-inf")

for i in range(1, stock_number + 1):

    print(f"\nEnter details for stock {i}")

    stock_name = input("Enter stock name: ").strip()
    number_of_shares = int(input("Enter number of shares: "))
    buy_price = float(input("Enter buy price per share: "))
    current_price = float(input("Enter current price per share: "))

    if not stock_name or number_of_shares <= 0 or buy_price <= 0 or current_price < 0:
        print("Invalid stock details. Please enter valid values.")
        raise SystemExit

    if current_price > buy_price:
        profitable_stocks += 1

    elif current_price < buy_price:
        loss_making_stocks += 1

    else:
        no_profit_no_loss_stocks += 1

    stock_return = ((current_price - buy_price) / buy_price) * 100

    if stock_return > highest_return:
        highest_return = stock_return
        best_performing_stock = stock_name

    total_investment += buy_price * number_of_shares
    total_current_value += current_price * number_of_shares

print("\n========== PORTFOLIO SUMMARY ==========")

print(f"Total investment: {total_investment:.2f}")
print(f"Current portfolio value: {total_current_value:.2f}")

profit_loss = total_current_value - total_investment

if profit_loss > 0:
    print(f"Profit: {profit_loss:.2f}")

elif profit_loss < 0:
    print(f"Loss: {abs(profit_loss):.2f}")

else:
    print("No profit, no loss")

if total_investment > 0:
    return_percentage = (profit_loss / total_investment) * 100
    print(f"Portfolio return: {return_percentage:.2f}%")

print("\n========== STOCK PERFORMANCE ==========")

print(f"Profitable stocks: {profitable_stocks}")
print(f"Loss-making stocks: {loss_making_stocks}")
print(f"No-profit-no-loss stocks: {no_profit_no_loss_stocks}")

print("\n========== BEST PERFORMING STOCK ==========")

print(f"Stock name: {best_performing_stock}")
print(f"Highest return: {highest_return:.2f}%")
