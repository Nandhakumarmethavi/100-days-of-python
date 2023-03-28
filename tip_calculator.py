print("WELCOME TO TIP CALCULATOR : ")
bill=float(input("what was the total bill : "))
tip=int(input("how much percent tip you would like to give : "))
people=int(input("how many people to split the bill : "))
bill_with_tip=tip/100*bill+bill
bill_per_person=bill_with_tip/people
final_amount=round(bill_per_person,2)
print(f"each person as to pay {final_amount}")