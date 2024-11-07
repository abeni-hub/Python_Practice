def calculate_cost(cart):
    total_cost = 0
    for item in cart:
        total_cost=total_cost+item['price']* item['quantity']
        
    return total_cost    
        
        
cart = [
     {'name':'Banan','price': 50 , 'quantity': 4},
     {'name':'Orange','price': 50, 'quantity': 5},
     {'name':'Apple','price':40 , 'quantity': 3}
     ] 
 
 ## Calling the Function    
 
total_cost = calculate_cost(cart)
print(total_cost)  
