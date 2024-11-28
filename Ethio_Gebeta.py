print("""Welcome to Ethio Gebeta
       1.Student Package
       2.Happy Hour Package
       3.5G Package
       4.Package
       5.You Package
       6.ethio 130 Promo
       7.Telebirr Service
       8.Entertainment Service

       #.Next page
    """) 

package_choice = int(input("Please enter a package"))

if package_choice == 1:
    print(""" Student package
         1. Monthly
         * back
         """ )
    monthly = int(input(" Please enter a number"))
    if monthly == 1:
        print(""" Monthly
                1.Birr 34 for 195Min + 100SMS plus
                 195Min night bonus pack
                2.Birr 64 for 365Min + 1GB + 150SMS
                 plus 365min night bonus pack 

                 #.Next page

                """)

elif package_choice == 2:
    print(""" Happy Hour package
         1.For yourself
         2.For gift
         *.Back
         """ )
    

elif package_choice == 3:
    print(""" 5G package
         1.For yourself
         2.For gift
         *.Back
         """ )

elif package_choice == 4:
    print(""" Package
         1.For yourself
         2.For gift
         *.Back
         """ )

elif package_choice == 5:
    print(""" Youth package
         1.For yourself
         2.For gift
         *.Back
         """ )

elif package_choice == 6:
    print(""" ethio 130 Promo
         Welcome to Ethio 130 Promo
         Coins: 0
         Points: 0
         Gold: 0
         1.Daily Subscribe(3 ETB)
         2.Weekly and Monthly
         3.Buy Coins
         4.Spin $ Win
         5.Prizes
         6.My Account
         """ )

elif package_choice == 7:
    print(""" Telebirr Services
         Welcome to telebirr
         0.Change PIN
         1.Financial Services
         2.Send Money
         3.Airtime/Package
         #.Next
         """ )

elif package_choice == 8:
    print(""" Entertainment Service
          Igado+ IPTV Service for Yourself
          Recurring Packages
         1.Igado+ IPTV Weekly Package
         2.Igado+ IPTV Monthly Package
         
         **.Main menu
         """ )
