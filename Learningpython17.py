
# k & v

model={"car":"bmw","engine":"diesel","colour":"black"}

add ={"showroom":"kerala"}
add1 ={"region":"south"}

model.update(add)
model.update(add1)
model.pop("colour")
print(model)


# HERE : I have added 2 new  key and value and deleted a particular key and value from it 