from pizzapy import *
customer = Customer('KEVIN', 'NGUYEN', 'KevinNguyen@gmail.com', '2024561111', 'The UTSA, San Antonio, TX, 78249')
print (customer)
my_local_dominos = StoreLocator.find_closest_store_to_customer(customer)
menu = my_local_dominos.get_menu()
print ("\n" + str (my_local_dominos) + "\n")

print ("Would you like to order ? ")

print (menu.search (Name='Pizza'))
