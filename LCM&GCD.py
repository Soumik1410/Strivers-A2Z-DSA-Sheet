bool isPalindrome(int x) {
    if(x<0)
        return false;
    int rev = 0, dig, num = x;
    while(x > 0)
    {
        dig = x % 10;
        if(214748364.7 < rev)
            return false;
        rev = rev * 10 + dig;
        x = x / 10;
    }
    if(rev == num)
        return true;
    else
        return false;
}
