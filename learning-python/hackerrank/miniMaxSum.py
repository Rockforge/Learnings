"""
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers.
Then print the respective minimum and maximum values as a single line of two space-separated long integers.
"""
def miniMaxSum(arr):

    holder = []

    for item in arr:
        holder.append(sum(arr) - item)

    print("{} {}".format(min(holder), max(holder)))


if __name__ == '__main__':

    arr = [1,2,3,4,5]
    miniMaxSum(arr)
