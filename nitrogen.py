import requests
import random
import string

print("Dies ist ein Discord-Nitro-Code-Generator und -Checker, der mit Python erstellt wurde. Dadurch werden Nitro-Codes generiert und überprüft, ob der Code gültig ist oder nicht. Wenn der Code gültig ist, wird der Code gedruckt, wobei 2 Zeilen übrig bleiben, und wenn nicht, wird '*' gedruckt.\n\n\n")
num = int(input
 '-------------------------------------------------------------------------------------------------------------------------------------\n'
 '#     #  #######  #######  #######   #####             #      #     #  ###  #######  ######   #######       #####   #######  #     # \n'
 '##    #  #     #  #     #       #   #     #           #       ##    #   #      #     #     #  #     #      #     #  #        ##    # \n'
 '# #   #  #     #  #     #      #    #     #          #        # #   #   #      #     #     #  #     #      #        #        # #   # \n'
 '#  #  #  #     #  #     #     #     #     #         #         #  #  #   #      #     ######   #     #      #  ####  #####    #  #  # \n'
 '#   # #  #     #  #     #    #      #   # #        #          #   # #   #      #     #   #    #     #      #     #  #        #   # # \n'
 '#    ##  #     #  #     #   #       #    #        #           #    ##   #      #     #    #   #     #      #     #  #        #    ## \n'
 '#     #  #######  #######  #######   #### #      #            #     #  ###     #     #     #  #######       #####   #######  #     # \n'
 '-------------------------------------------------------------------------------------------------------------------------------------\n'
 '----------------------------Geben Sie ein, wie viele Codes generiert und überprüft werden sollen:------------------------------------\n'
 ))


with open("Nitro Codes.txt", "w", encoding='utf-8') as file:
    print("Ihre Nitro-Codes werden generiert, haben Sie etwas Geduld!")

    for i in range(num):
        code = "".join(random.choices(
            string.ascii_uppercase + string.digits + string.ascii_lowercase,
            k = 16
        ))

        file.write(f"https://discord.gift/{code}\n")
    print(f"Generated {num} codes\n")

with open("Nitro Codes.txt") as file:
    for line in file.readlines():
        nitro = line.strip("\n")

        url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            print(f"\n\n Valid | {nitro}\n\n")
        else:
            print(f"*", end = "")

print("\n\n\nSie haben Codes generiert und erfolgreich überprüft, ich hoffe, Sie haben einige gültige")
