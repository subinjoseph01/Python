

model = ["car","type","horsepower","colour"]

spec = ["bmw","diesel","898","biege"]



car = dict(zip(model,spec))

print(car)


# here to assign keys and values  use zip concept 


model = ["car","type","horsepower","colour"]

spec = ["bmw","diesel","898","biege"]



car = dict.fromkeys(model,spec)

print(car)

# here to assign all values of  values in keys use from keys 
# eg .  {'car': ['bmw', 'diesel', '898', 'biege'], 'type': ['bmw', 'diesel', '898', 'biege']