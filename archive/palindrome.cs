public class Solution {
    public bool IsPalindrome(int x) {
        int reverseNum = 0;
        int originNum = x;
        int reminder = 0;

        while(originNum > 0) {
            reminder = originNum%10;
            originNum= originNum / 10;

            reverseNum = reverseNum*10;
            reverseNum+=reminder;
        }

        if(reverseNum == x) return true;

        return false;
    }
}