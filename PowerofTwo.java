class Solution {
    public boolean isPowerOfTwo(int n) {
        if (n <= 0) { // Negative numbers and zero are not power of two
            return false;
        } 
        while (n > 1) {
            if (n % 2 != 0) {
                return false;
            }
            n = n / 2;
        }
        return true; // If we reach 1, it's a power of two
    }
}
