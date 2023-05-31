salary=int(input("enter your annual salary:"))
if salary <= 300000:
    print("you need not to pay tax..")
elif 300000 < salary <= 600000:
    tax=0.05
    print(f"you need to pay {salary*tax} from your {salary}")
elif 60000 < salary <= 900000:
    tax=0.10
    print(f"you need to pay {salary*tax} from your {salary}")
elif 900000 < salary <= 1200000:
    tax=0.15
    print(f"you need to pay {salary*tax} from your {salary}")
elif 1200000 < salary <= 1500000:
    print(f"you need to pay {salary*tax} from your {salary}")
else:
    tax=0.30
    print(f"you need to pay {salary*tax} from your {salary}")

    output:
      enter your annual salary:400000
you need to pay 20000.0 from your 400000
enter your annual salary:100000
you need not to pay tax..
enter your annual salary:600000
you need to pay 30000.0 from your 600000
enter your annual salary:1200000
you need to pay 180000.0 from your 1200000
