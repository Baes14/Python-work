def make_car(brand, model, **optional):
	car = {}
	car['brand_name'] = brand
	car['model_name'] = model
	for key,value in optional.items():
		car[key] = value

	return car