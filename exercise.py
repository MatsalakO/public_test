# def is_year_leap (year):
# 	if year == 366:
# 		return print(True)
# 	else:
# 		return print(False)

# is_year_leap(365)

def season ():
	season = int(input("Введите номер месяца: "))
	if season >= 13 or season==0:
		print("Такого месяца не существует")
	elif season == 2 or season==1 or season == 12:
		print("Это зимний месяц")
	elif season == 3 or season==4 or season==5:
		print("Это весенний месяц")
	elif season == 6 or season==7 or season==8:
		print("Это летний месяц")
	elif season == 9 or season==10 or season==11:
		print("Это осенний месяц")

season()