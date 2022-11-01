def highest_revenue_item( data ):
	count_dict = {}
	price_dict = {}
	
	row_data = data.split(' ')
	for row in row_data:
		txn = row.split(',')
		product_id = txn[0]
		price = int(txn[1]) #casting it to integer
		
		if product_id in count_dict.keys():
			count_dict[product_id] += 1 #add on to the count
			price_dict[product_id] += price #add on to the price
		else:
			count_dict[product_id] = 1 #initializing
			price_dict[product_id] = price #initializing price
		
	most_common_item = 0
	most_revenue = 0
	
	for product in count_dict.keys():
		product_revenue = price_dict[product] * 					count_dict[product]
		if product_revenue > most_revenue: # has to be greater
			most_revenue = product_revenue
			most_common_item = int(product)
		
	if most_revenue != 0:
		return most_common_item

print(highest_revenue_item(("33,2 32,1 55,5, 33,3")))
