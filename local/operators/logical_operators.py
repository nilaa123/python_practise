high_income=False
good_credit=False
criminal_record=True

if ((high_income and good_credit) and not criminal_record):
    print("eligible for loan")
elif (high_income or good_credit) and not criminal_record:
    print("eligible for loan but must sumbit a colateral")
elif ((high_income and good_credit) and criminal_record):
    print("eligible for loan only after police verification")
elif (high_income or good_credit) and  criminal_record:
    print("eligible for loan only after police verification and colateral sumbition")
else:
    print("Not eligible")
