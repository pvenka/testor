
# Making the assumption that vesrsions will only have numbers. 
# Can be doen if alphabets are there like beta alpha vers etc. 
# 
def compver(a,b):
        a1 = a.split(".")
        a2 = float(''.join(a1[0:]))
        b1 = b.split(".")
        b2 = float(''.join(b1[0:]))
	print a2,b2,a1,b1

	if a1 > b1:
		ans = '"%s" greater than "%s"' % (a,b)
	else:
		ans = '"%s" greater than "%s"' % (b,a)
	return ans
def main():
	print(compver("1.1", "1.2"))
	print(compver("2.0.1.3", "2.0.1.5"))
if __name__ == '__main__':
	main()
