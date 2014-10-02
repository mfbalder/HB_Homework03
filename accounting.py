def count_melons_sold():
	"""Counts the number of each melon that is sold"""
	f = open("orders_by_type.csv")
	melon_tallies = {"Musk": 0, "Hybrid": 0, "Watermelon": 0, "Winter": 0}
	for line in f:
		data = line.split(",")
		melon_type = data[1]
		melon_count = int(data[2])
		melon_tallies[melon_type] += melon_count
	f.close()
	return melon_tallies
	
def calculate_melon_revenue(melon_tallies):
    melon_prices = { "Musk": 1.15, "Hybrid": 1.30, "Watermelon": 1.75, "Winter": 4.00 }
    total_revenue = 0
    for melon_type in melon_tallies:
        price = melon_prices[melon_type]
        revenue = price * melon_tallies[melon_type]
        total_revenue += revenue
        print "We sold %d %s melons at %0.2f each for a total of %0.2f" % (melon_tallies[melon_type], melon_type, price, revenue)

def online_and_phone_sales():
	f = open("orders_with_sales.csv")
	sales = [0, 0]
	for line in f:
		data = line.split(",")
		if data[1] == "0":
			sales[0] += float(data[3])
		else:
			sales[1] += float(data[3])
	print "Salespeople generated %0.2f in revenue." % sales[1]
	print "Internet sales generated %0.2f in revenue." % sales[0]
	if sales[1] > sales[0]:
		print "Guess there's some value to those salespeople after all."
	else:
		print "Time to fire the sales team! Online sales rule all!"
		
def generate_fancy_sales_report():
	print "Ubermelon Sales Report: October 1, 2014\n"
	print "******************************************"
	
	print "This month's revenue per melon:\n"
	calculate_melon_revenue(count_melons_sold())
	print "******************************************"
	
	print "This month's total sales, for online sales and in person:\n"
	online_and_phone_sales()
	print "******************************************"
	

def main():
    
	generate_fancy_sales_report()


if __name__ == "__main__":
    main()
