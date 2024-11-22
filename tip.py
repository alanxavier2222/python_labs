bill=float(input("enter your bill:"))
tip=int(input("how much you want to tip,10/20:"))
people=int(input("How many peoples to split the bills with:"))
tip_as_percentage=tip/100
total_tip_amount=tip_as_percentage*bill
total_bill=total_tip_amount+bill
bill_per_person=total_bill/people
final_amount_per_person=round(bill_per_person,2)
print(f'each person has to pay{final_amount_per_person}.')