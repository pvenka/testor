import sys

def overlap(x1,x2,x3,x4):
# Check if x1 and x3 are less than x2 and x4 respectively. If not reverse.
        if (x1 < x2):
		pass
	else:
		x1,x2 = x2,x1

        if (x3 < x4):
                pass
        else:
                x3,x4 = x4,x3
#Check for overlap. if the lower point of 2nd line is less than the larger point of first. 
	if (x1 < x3):
		if (x3 <= x2):
			ans = True
		else:	
			ans = False
	elif (x3 < x1):
		if (x1 <= x4):
			ans = True
		else:
			ans = False
	

	if(ans):
		print "Overlap"
	else: 
		print "Do not overlap"

if len(sys.argv) < 3 or len(sys.argv) > 4:
	print("Enter the coordiates of two points like '(x1,x2)' , '(x3,x4)' as arguments")
	print("Usage Overalp.py '(x1,x2)' , '(x3,x4)'")
else:
	line1, line2  = eval(sys.argv[1]), eval(sys.argv[3])

	x1, x2 = float(line1[0]), float(line1[1])

	x3, x4 = float(line2[0]), float(line2[1])

	overlap(x1,x2,x3,x4)
