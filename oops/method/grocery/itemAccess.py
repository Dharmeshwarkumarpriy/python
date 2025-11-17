from oops.method.grocery.Item import Item as items
n=int(input("enter the no. of items record:"))

for i in range(n):
    s=items()
    print("______ ______ _______")
    print("enter the item details ..")
    gyName=input("enter the name:")
    gyCode=input("enter the code:")
    gyWeight=input("enter the weight:")
    gyPrice=input("enter the price:")

    s.setItemName(gyName)
    s.setItemCode(gyCode)
    s.setItemWeight(gyWeight)
    s.setItemPrice(gyPrice)
    print(" item record...")
    print("item is...",s.getItemName(),s.getItemCode(),
          s.getItemWeight(),s.getItemPrice())