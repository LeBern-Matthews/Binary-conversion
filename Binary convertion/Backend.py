def binary_convo(base10):
    def binary(base10):
        x=True      #condition for loop
        output=''   #sets up initial string for printing
        
        while x:    
            hold=''
            div=int(base10/2)   #divides the number entered by 2 in div
            remainder=base10%2  #stores the remainder of the number entered by 2
            hold=str(remainder) # converts remainder to a string for easy manipulation
            output=hold+output  #concatonates output to hold and stores it in hold
            base10=div          #stores div in base10 so the process can be repeated with the new number(div)
            
            if base10==0:       #condition for ending process, process should end when div/ base10 =0
                x=False         #stores False in x
        return output      #returns "output as an integer"

    def binary_decimal(base10):
        x=True
        i=0
        output="."
        while i<=5:
            times= base10*2
            int_conv=int(times)
            output=output+str(int_conv)
            if int_conv==1:
                base10=times-1
            else:
                base10=times
            i+=1    
        return output

    num=int(base10)

    if base10-num==0:
        #binary(base10)
        return binary(num)
    else:
        
        decimal=base10-num
        
        binary_output=binary(num)
        decimal_output=binary_decimal(decimal)
        final=binary_output+binary_decimal(decimal)
        return final