
steps = int(input("enter a number:"))

def ways(n):
	if n <= 1:
		return n
	return ways(n-1) + ways(n-2)

def countWays(s):
	return ways(steps + 1)

print ("Number of ways = ",countWays(steps))
