
def convert_currency(amount, from_currency, to_currency):
    rates = {"USD": 1, "EUR": 0.85, "GBP": 0.73, "CAD": 1.25}
    converted = amount * (rates[to_currency] / rates[from_currency])
    return f"{amount} {from_currency} is approximately {converted:.2f} {to_currency}"