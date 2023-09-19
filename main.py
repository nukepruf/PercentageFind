#Simple program made to calculate gains from Crypto trading.
import sys


def asset_change():
    coin_buy_price = float(input("What price did you buy the asset? "))  # Initial Buy in price.
    usd_spent = float(input("How much $USD did you invest? "))
    coin_current_price = float(input("What is the current price of the asset? "))  # Current price of the asset.
    coin_difference = coin_current_price - coin_buy_price
    coin_percent_change = coin_difference / coin_buy_price
    coin_final_value = coin_percent_change * 100
    coin_final_rounded = round(coin_final_value)
    current_value = coin_final_value + 100
    final = (float(current_value) * usd_spent / 100)

    print("That is a change of", coin_final_rounded, "%")

    # USD_Increase = USD_Spent + Coin_FinalValue
    print("Your initial investment of $", usd_spent, "is now worth $", final)
    x = round(final - usd_spent)
    print("That is an increase of $", x)
    print("This does not factor in your trade fees")

    if input("Would you like to try again y or n.") == "y":
        asset_change()
    elif input == "n":
        sys.exit("GoodBye")


if __name__ == '__main__':
    asset_change()
