// Last updated: 8/7/2025, 9:27:58 PM
class Solution {
public:
    bool isPalindrome(int x) {
    if (x < 0) return false; // Negative numbers are not palindromes

    long original = x;
    long reversed = 0;

    while (x != 0) {
        int digit = x % 10;
        reversed = reversed * 10 + digit;
        x /= 10;
    }

    return original == reversed;
    }

};