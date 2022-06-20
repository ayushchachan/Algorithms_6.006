def count_long_subarray(A):
    '''
    Input:  A     | Python Tuple of positive integers
    Output: count | number of longest increasing subarrays of A
    '''
    count = 0
    ##################
    # YOUR CODE HERE #
    ##################

    maxSize = 1;
    i = 0;
    while i < len(A) - 1:
        if (A[i + 1] > A[i]):
            maxCount = 2;
            j = i + 1;
            while (j < len(A) - 1 and A[j + 1] > A[j]):
                maxCount += 1;
                j = j + 1;

            if (maxCount > maxSize):
                maxSize = maxCount;
                count = 1;
            elif (maxCount == maxSize):
                count += 1;
            i = j;
        i =  i + 1;

    return count
