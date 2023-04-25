# python find_matching_pair.py

def funtion_find_matching_pair(arr, sum):
    '''
    Find the first Pair in sequence.
    The solution is linear, it can receive a large amount of input numbers.
    '''
    t = set()
    for i in range(len(arr)):
        delta = sum - arr[i]
        #print(i, delta, arr[i], t)
        if (delta in t):
            #print("OK, matching pair", "(", delta, ",", arr[i], ")")
            message = "OK, matching pair" + "( " + str(delta) + " , " + str(arr[i]) + " )"			
            return message
        t.add(arr[i])
    return "No"

if __name__ == '__main__':
	arr = [2,3,6,7]
	sum = 9
	print(funtion_find_matching_pair(arr, sum))
