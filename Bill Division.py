def bonAppetit(bill, k, b):
    bill.pop(k)
    anna_share = sum(bill) / 2
    if anna_share == b:
        print("Bon Appetit")
    else:
        print(int(b - anna_share))