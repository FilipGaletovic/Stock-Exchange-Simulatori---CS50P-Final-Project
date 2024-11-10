import re
import sys
import load_save
import get_stock_info



JSON_USERS = "accounts.json"

def get_latest_close_price(symbol, username, index = 0):
    try:
        current_stock = get_stock_info.get_stock(symbol)
    except ValueError as e:
        print(e)
        main_menu(username, False)
    time_series = current_stock["Time Series (60min)"]
    latest_time = sorted(time_series.keys(), reverse=True)[index]
    return float(time_series[latest_time]["4. close"])

def main_menu(username, first_login=True):
    if first_login:
        print(f"\n\nWelcome {username}")
    print("\n\tType 1 to Display Balance")
    print("\tType 2 to Search for Stocks")
    print("\tType 3 to Save and Exit\n\n")

    try:
        user_choice = int(input("Enter your choice: "))
        if user_choice not in [1, 2, 3]:
            print("Invalid choice, please enter 1, 2, or 3.")
            main_menu(username, False)
            return
    except ValueError:
        print("Invalid input. Please enter a number.")
        main_menu(username, False)
        return

    # Load user data
    user_data = load_save.load_users(JSON_USERS)
    user_index = fetch_user(username, user_data)

    if user_choice == 1:
        # Display Balance
        invested_balance = user_data[user_index]["invested"]
        for symbol, stock_data in invested_balance.items():
            latest_close_price = get_latest_close_price(symbol, username)
            if latest_close_price:
                shares = stock_data["amount"] / latest_close_price
                stock_data["amount"] = shares * latest_close_price

        # Display invested balance details
        invested_balance_str = ", ".join(
            f"{symbol}: [${stock_data['amount']:.2f} ({shares:.3f}) bought at {stock_data['purchase_price_per_share']:.2f}]"
            for symbol, stock_data in invested_balance.items()
        )
        print(f"\n\nBalance: ${user_data[user_index]['balance']:.2f}")
        print(f"Invested: \n\t{invested_balance_str}")
        main_menu(username, False)

    elif user_choice == 2:
        def buy_function(search, owned_now):
            print(f"\nAvailable Balance: ${user_data[user_index]['balance']}\n")
            try:
                amount_to_buy = int(input("Enter Amount: "))
                if amount_to_buy > user_data[user_index]["balance"]:
                    print("Amount exceeds balance")
                    search_function()
            except ValueError as e:
                print(e + "-- Please enter valid amount")
                search_function()
            try:
                confirm = input(f"Type y/n to confirm buying ${amount_to_buy} of [{search}]:  ")
                invested_data = user_data[user_index]["invested"]
                latest_close_price = get_latest_close_price(search, username)
                if confirm.lower() in ["y", "yes", "yeah"]:
                    user_data[user_index]["balance"] -= amount_to_buy
                    if not owned_now:
                        invested_data[search] = {
                            "amount": amount_to_buy,
                            "purchase_price_per_share": latest_close_price
                        }

                    else:
                        invested_data[search] = {
                            "amount": owned_now + amount_to_buy,
                            "purchase_price_per_share": latest_close_price
                        }

                    load_save.save_users(user_data, JSON_USERS)
                    print(f"You just bought {amount_to_buy/latest_close_price:02f} shares of [{search}]")
                    main_menu(username, False)

                elif confirm.lower() in ["n", "no", "nope"]:
                    main_menu(username, False)
                else:
                    print("Not a confirmation, try again")
                    search_function()
            except ValueError as e:
                print(e, "-- Please enter valid amount")
                search_function()


        def sell_function(search, owned_now):
            invested_stocks = user_data[user_index]["invested"]
            print(f"Currently Invested: {owned_now} shares")
            try:
                amount_to_sell = int(input("Enter Amount: "))
                if amount_to_sell > owned_now:
                    print("Amount exceeds invested balance")
                    search_function()
                elif amount_to_sell < 0:
                    print("-- Please enter valid amount")
                    search_function()
            except ValueError as e:
                print(e + "-- Please enter valid amount")
                search_function()
            try:
                confirm = input(f"Type y/n to confirm selling ${amount_to_sell} of [{search}]:  ")
                if confirm.lower() in ["y", "yes", "yeah"]:

                    user_data[user_index]["balance"] += amount_to_sell
                    if amount_to_sell == owned_now:
                        del invested_stocks[search]
                    else:
                        invested_stocks[search]["amount"] -= amount_to_sell
                    load_save.save_users(user_data, JSON_USERS)
                    print(f"You just sold ${amount_to_sell} of [{search}]")
                    main_menu(username, False)

                elif confirm.lower() in ["n", "no", "nope"]:
                    main_menu(username, False)
                else:
                    print("Not a confirmation, try again")
                    search_function()
            except ValueError as e:
                print(e, "-- Please enter valid amount")
                search_function()

        def search_function():
            search = input("Search top 50 stocks: ")
            try:
                current_data = get_stock_info.get_stock(search)
            except ValueError as e:
                print(e)
                main_menu(username, False)
            meta_data = current_data['Meta Data']
            print("\n")
            for key, value in meta_data.items():
                print(f"{key}: {value}")
            latest_close_price = get_latest_close_price(search, username)
            print(f"\nLatest Closing Price: {latest_close_price}\n")
            invested_balance = user_data[user_index]["invested"]
            if search in invested_balance:
                price_change = ((latest_close_price - invested_balance[search]["purchase_price_per_share"]) / latest_close_price) * 100
                owned_now = invested_balance[search]["amount"]/(invested_balance[search]["purchase_price_per_share"] + (invested_balance[search]["purchase_price_per_share"] * price_change))
                print(f"You currently own {owned_now:.4f} shares of {search}")
                next_input = input("Would you like to BUY/SELL: ")
            else:
                next_input = input("Would you like to BUY: ")

            if next_input.lower() in ["buy", "b", "y", "yes", "yeah"]:
                buy_function(search, 0)

            elif next_input.lower() in ["sell", "s", "se"]:
                sell_function(search, owned_now*latest_close_price)
            else:
                print("\n--Please provide a valid stock symbol or name--\n")
                search_function()

        search_function()

    else:
        load_save.save_users(user_data, JSON_USERS)
        sys.exit("Goodbye!\n")



def fetch_user(name, user_data):
    index = 0
    for user in user_data:
        if user["username"] == name:
            break
        else:
            index += 1
    return index


if __name__ == "__main_menu__":
    main_menu()
