import math
import random


class BigO():
	count = 0

	def start(self, n):
		self.n = n
		self.orders = [
			{'calc': 1, 'name': 'O(1) Constant'},
			{'calc': self.n, 'name': 'O(n) Linear'},
			{'calc': self.n * math.log(self.n) / math.log(2), 'name': 'O(n*log(n)) Logarithmic'},
			{'calc': pow(self.n, 2), 'name': 'O(n^2) Quadratic'},
			{'calc': pow(2, self.n), 'name': 'O(2^n) Exponential'},
			{'calc': math.factorial(self.n), 'name': 'O(n!) Factorial'},
		]

	def add(self):
		self.count += 1
	
	def get_order_index(self, count=None, prnt=None):
		if not count: count = self.count
		for i in range(1, len(self.orders)):
			if self.orders[i-1]['calc'] <= count <= self.orders[i]['calc']:
				if prnt: print(f"{prnt} | {self.orders[i-1]['name']} {self.orders[i-1]['calc']} <= {count} <= {self.orders[i]['name']} {self.orders[i]['calc']}")
				return i


def make_array():
	n = random.randrange(100, 1000)  # with random array size
	arr = []
	for _ in range(n):
		arr += [random.randrange(-1000, 1000)]  # and random array elements
	return arr


def check_results(expected, result):
	if result != expected:
		print(f"ERROR:\n{result=}\n{expected=}")  # print an ERROR if the algorithm didn't do what it's suppsoed to


def run_all(run_list, prnt=False):
	for algorithm in run_list:  # for every algorithm in run_list
		avg_order_index = 0
		for i in range(20):  # run 20 times
			o = BigO()
			algorithm(o)
			avg_order_index = (avg_order_index * i + o.get_order_index(prnt=algorithm.__name__ if prnt else None)) / (i + 1)  # caluclate average order index
		# after running 20 times, output the average order index and a bit of info about that
		order_int = math.ceil(avg_order_index)
		print(f"{algorithm.__name__} | {o.orders[order_int]['name']}")


#####ALGORITHMS##########ALGORITHMS##########ALGORITHMS##########ALGORITHMS##########ALGORITHMS##########ALGORITHMS#####
##########ALGORITHMS##########ALGORITHMS##########ALGORITHMS##########ALGORITHMS##########ALGORITHMS##########ALGORITHMS


def insertion_sort(o, arr=None):
	if arr:
		check = False
	else:
		check = True
		arr = make_array()
		o.start(n=len(arr))
	result = arr  # can do all with 1 array, just need to keep arr for check_results

	# function: sort a given array arr in ascending order
	# approach: incremental
	# methodology: for each element, move it down until it's its between two that are less and greater than it
	for j in range(1, len(result)):
		key = result[j]
		for i in reversed(range(1, j+1)):  # j to 0
			if result[i-1] > key:
				result[i] = result[i-1]
				#arr[i-1] = key  # don't need set every time, set once at the end
				o.add()
			else:
				break
		result[i-1] = key
	
	# wrap-up
	if check:
		arr.sort()
		check_results(expected=arr, result=result)
	else:
		return arr


def merge(o, arr1=None, arr2=None):
	if arr1 and arr2:
		check = False
	else:
		check = True
		arr1 = make_array()
		arr2 = make_array()
		arr1.sort()
		arr2.sort()
		o.start(n=len(arr1)+len(arr2))

	# function: merge together two already sorted arrays, but make sure the final array is also sorted
	# approach: incremental
	# methodology: grab the first (lowest) element of each, and put the lowest of the 2 into the result array, pull another, repeat
	a = len(arr1)
	b = len(arr2)
	n = a + b
	i, j = 0, 0
	result = []
	if arr1[a-1] <= arr2[0]:
		result = arr1 + arr2
		o.add()
	elif arr2[b-1] <= arr1[0]:
		result = arr2 + arr1
		o.add()
	else:
		for _ in range(n):
			if j >= b or (i < a and arr1[i] <= arr2[j]):  # add from arr1 if
				result += [arr1[i]]
				i += 1
				o.add()
			elif i >= a or (j < b and arr1[i] >= arr2[j]):
				result += [arr2[j]]
				j += 1
				o.add()

	# wrap-up
	if check:
		arr = arr1 + arr2
		arr.sort()
		check_results(expected=arr, result=result)
	else:
		return result


def merge_sort(o, arr=None):
	if arr:
		check = False
	else:
		check = True
		arr = make_array()
		o.start(n=len(arr))

	# function: sort a given array arr in ascending order
	# approach: divide and conquer (recursive)
	# methodology: 
	n = len(arr)
	if n <= 1:  # if down to 1-element array, it is sorted, just set it, this ends the recursion
		result = arr
	else:  # if 2 or more elements, divide into 2 arrays and sort (merge_sort) them each and merge them 
		a = int(n / 2)  # this rounds down
		arr1 = merge_sort(o, arr[:a])
		arr2 = merge_sort(o, arr[a:])
		result = merge(o, arr1, arr2)
	
	# wrap-up
	if check:
		arr.sort()
		check_results(expected=arr, result=result)
	else:
		return result


run_list = [
	insertion_sort,
	merge,
	merge_sort,
]

run_all(run_list, prnt=False)
