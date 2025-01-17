class ArrayMult:
    def mult(self, array1, array2):
        # Determine the length of the shorter array
        minlen = min(len(array1), len(array2))
        
        # Determine which array is longer
        longArray = array1 if len(array1) > len(array2) else array2
        
        # Initialize the output array with the length of the longer array, filled with zeros
        outArray = [0] * len(longArray)
        
        # Perform point-wise multiplication for the elements up to the length of the shorter array
        for i in range(minlen):
            outArray[i] = array1[i] * array2[i]
        
        # Copy the remaining elements from the longer array to the output array
        for j in range(minlen, len(longArray)):
            outArray[j] = longArray[j]
        
        # Return the resulting output array
        return outArray