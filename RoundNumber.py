# This function rounds numbers n to a specific power of 10 (from 0 to (number of digits -1); OUTPUT is an integer; ONLY for numbers >0
# Ideas for more versatility: 
#   -Choosing if the program should round up or down
#   -Rounding numbers <0 or rounding to a specific decimal point

def rounding(n,q):
    number=n
    digits=0
    before_comma=0
    rounded_number=0
    list=[]
    #counts the digits of the number
    while number !=0:
        number//=10
        digits+=1

    #cheks if input is correct
    if q>digits:
        return "False Input. q cannot be bigger than number of digits!!"
    
    #example: n=1234.56 --> generates list=[0.56,4,30,200,1000]
    for nth_digit in range(digits):
        x=int( (n / 10**nth_digit) % 10) *10**nth_digit
        list.append(x)
        before_comma += x
    list.insert(0,n-before_comma)

    #example for n=1234.56 and q=3 --> cheks if 34 > 50 , 
    # if TRUE--> list doesnt change and rounded number contains added numbers of list FROM index q TO last element of list
    # if FALSE--> list changes at index q (here+100) and rounded number contains added numbers of list FROM index q TO last element of list
    if list[q-1] < 0.5*(10**(q-1)):
        for a in range(q,digits+1):
            rounded_number+=list[a]
    elif list[q-1] >= 0.5*(10**(q-1)):
        list[q]=list[q]+(10**(q-1))
        for a in range(q,digits+1):
            rounded_number+=list[a]
        
    return rounded_number

print(rounding(123,2))