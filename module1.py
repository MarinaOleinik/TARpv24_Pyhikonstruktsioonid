import random
import os
from colorama import init, Fore, Style

# Colorama initsialiseerimine, et see töötaks Windowsis
init(autoreset=True)

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

def print_colored_text(word, target):
    result = ""
    for i, letter in enumerate(word):
        if letter == target[i]:
            result += Fore.GREEN + letter + Style.RESET_ALL  # Roheline, kui täht on õiges kohas
        elif letter in target:
            result += Fore.YELLOW + letter + Style.RESET_ALL  # Kollane, kui täht on vales kohas
        else:
            result += Fore.LIGHTBLACK_EX + letter + Style.RESET_ALL  # Hall, kui täht ei ole sõnas
    print(result)

def wordle_game():
    words = ["maja", "koer", "kass", "põld", "lill"]  # Näidis sõnade loend
    target_word = random.choice(words)
    attempts = 6
    word_length = len(target_word)
    
    print("\nTere tulemast sõnamängu Wordle! Proovi ära arvata sõna.")
    print(f"Sõna on {word_length} tähe pikkune.")
    print("Sul on 6 katset!")
    
    print("\n" + Fore.GREEN + "Roheline" + Style.RESET_ALL + " = õige täht ja õige koht")
    print(Fore.YELLOW + "Kollane" + Style.RESET_ALL + " = õige täht, aga vale koht")
    print(Fore.LIGHTBLACK_EX + "Hall" + Style.RESET_ALL + " = täht ei ole sõnas")
    
    while attempts > 0:
        guess = input("Sisesta oma pakkumine: ").strip().lower()
        if len(guess) != word_length:
            print(f"Sõna peab olema {word_length} tähemärki pikk!")
            continue
        
        clear_console()
        print_colored_text(guess, target_word)
        
        if guess == target_word:
            print("Palju õnne! Sa leidsid õige sõna!")
            break
        
        attempts -= 1
        print(f"Sul on jäänud {attempts} katset.")
        
    if attempts == 0:
        print(f"Kahjuks ei õnnestunud. Õige sõna oli: {target_word}")
    print("Aitäh mängimast!")

if __name__ == "__main__":
    wordle_game()
