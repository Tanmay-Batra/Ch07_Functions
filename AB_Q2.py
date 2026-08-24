def netPay(amount,isMem):
    if amount>=500 and amount<1000:
        disP=0.05
    elif amount>=1000 and amount<2000:
        disP=0.08
    else:
        disP=0.1
    #if store member
    if isMem==True:
        disP=disP+0.05
    
    #discount calculation
    discount=amount*disP
    netAmount=amount-discount
    return netAmount

amount=int(input("Enter the shopping amount: "))
isMem=input("Is store member(True/False): ").lower()=="true"
print("Net Payable Amount: ",netPay(amount,isMem))

