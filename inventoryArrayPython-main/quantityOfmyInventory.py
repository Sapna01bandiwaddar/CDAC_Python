def findQuantity(product_code):
for item in myInventory:
if item["product_code"]==product_code:
return item["Qunatity"]
return None
x = findQuantity("S2106")
print(x)
