package Q1;

public class ArrayMult {
    public int[] mult(int[] array1, int[] array2) {
        // Determine the length of the shorter array
        int minlen = Math.min(array1.length, array2.length);

        // Identify the longer array
        int[] longArray = array1.length > array2.length ? array1 : array2;

        // Initialize the output array with the length of the longer array
        int[] outArray = new int[longArray.length];

        // Perform point-wise multiplication for the length of the shorter array
        for (int i = 0; i < minlen; i++) {
            outArray[i] = array1[i] * array2[i];
        }

        // Copy the remaining elements from the longer array
        for (int j = minlen; j < longArray.length; j++) {
            outArray[j] = longArray[j];
        }

        // Return the resulting array
        return outArray;
    }
}
