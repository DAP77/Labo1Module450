# Dictionnaire des taux fixes
exchange_rates = {
    ("USD", "EUR"): 0.92,
    ("EUR", "CHF"): 0.95,
    ("CHF", "USD"): 1.10,
    ("EUR", "USD"): 1.09,
    ("USD", "CHF"): 0.88,
    ("CHF", "EUR"): 1.07
}

def convert_currency(amount, base_currency, target_currency):
    """ Convertit un montant entre deux devises selon un taux de change fixe. """
    if amount < 0:
        return None  # Gestion des montants invalides

    rate = exchange_rates.get((base_currency, target_currency))
    if rate:
        return round(amount * rate, 2)  # Arrondi à 2 décimales
    return None  # Si la conversion n'est pas possible

def main():
    print("Bienvenue dans le convertisseur de devises!")
    
    try:
        amount = float(input("Entrez le montant à convertir: "))
        base_currency = input("Entrez la devise source (ex: USD, EUR, CHF): ").upper()
        target_currency = input("Entrez la devise cible (ex: USD, EUR, CHF): ").upper()
    
        converted_amount = convert_currency(amount, base_currency, target_currency)
    
        if converted_amount is not None:
            print(f"{amount} {base_currency} équivaut à {converted_amount:.2f} {target_currency}")
        else:
            print("Conversion impossible. Veuillez vérifier les devises entrées ou le montant.")
    except ValueError:
        print("Erreur : Veuillez entrer un nombre valide.")

if __name__ == "__main__":
    main()
