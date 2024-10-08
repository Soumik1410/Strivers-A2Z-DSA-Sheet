int reverse(int x){
    int sign = x>0?1:-1;
    int dig,count=0,rev=0;
    while(x!=0)
    {
        dig = x%10;
        if(dig < 0)
            dig = -1 * dig;
        if(214748364.7 < rev)
            return 0;
        rev=rev*10+dig;
        x=x/10;
    }
    int sg = rev>0?1:-1;
    if(sign != sg)
        rev = -1 * rev;
    return rev;
}
