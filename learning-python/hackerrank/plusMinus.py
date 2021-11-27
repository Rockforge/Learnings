def plusMinus(n):
    positives = list(filter(lambda item: item > 0, n))
    negatives = list(filter(lambda item: item < 0, n))
    zeros = list(filter(lambda item: item == 0, n))

    print("{:.6f}".format(len(positives)/len(n)))
    print("{:.6f}".format(len(negatives)/len(n)))
    print("{:.6f}".format(len(zeros)/len(n)))

if __name__ == "__main__":
    # Input
    n = [1,2,3,-1,-2,-3,0,0]

    # Run our method
    plusMinus(n)
