TypeSelect = False
AdressSelect = False
AmmountSelect = False

print(""" 
 _      _____   ___  ______   _____  _____  _____  _____ 
| |    |  _  | / _ \ |  _  \ |_   _||  ___|/  ___||_   _|
| |    | | | |/ /_\ \| | | |   | |  | |__  \ `--.   | |  
| |    | | | ||  _  || | | |   | |  |  __|  `--. \  | |  
| |____\ \_/ /| | | || |/ /    | |  | |___ /\__/ /  | |  
\_____/ \___/ \_| |_/|___/     \_/  \____/ \____/   \_/  
                                                         
""")

print("Welcome To Load Test. Version Beta 1.0 \nPlease Select a type for load: \n1. DOS-attack")

while not TypeSelect:
    inp = input()
    match inp:
        case "1":
            TypeSelect = True
            while not AdressSelect:
                print("You've selected a DOS-attack. Input an address for attack:")
                attackAdres = input()
                
                if "http://" in attackAdres or "https://" in attackAdres:
                    AdressSelect = True
                    print("Address is Valid.\nInput amount request per second (default:10).")
                    
                    while not AmmountSelect:
                        AmmountAttack = input() or "10"
                        if AmmountAttack.isdigit():
                            AmmountSelect = True
                            print(f"You want to send {AmmountAttack} requests per {attackAdres}. Are you sure?")
                        else:
                            print("Amount not valid. Try again.")
                else:
                    print("Your address is not valid, try again")
        
        case _:
            print("No answer. Please try again")