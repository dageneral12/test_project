def vat_calculation(price):
    
    try: 
        price = float(price)
        return print(price * 0.18)
    except(ValueError, TypeError): 
        return print ("Please check the value or the data type")

if __name__ == '__main__': 
    vat_calculation('some number') 



    
        