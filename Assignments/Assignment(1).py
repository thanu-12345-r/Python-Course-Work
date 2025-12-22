# BANK SYSTEM – ALL DATA TYPES (EXECUTABLE)

# String
account_holder = input("Enter Account Holder Name: ")

# Integer
account_number = int(input("Enter Account Number: "))

# Float
deposit_amount = float(input("Enter Deposit Amount: "))

# List (string) – Deposit modes
deposit_modes = input("Enter Deposit Modes (Cash Cheque Online): ").split()

# Tuple (integer) – Date (DD MM YYYY)
deposit_date = tuple(map(int, input("Enter Deposit Date (DD MM YYYY): ").split()))

# Set (string) – Bank services
services_used = set(input("Enter Services Used (ATM UPI NetBanking): ").split())

# Dictionary – Bank details
bank_details = {
    "Account Holder": account_holder,
    "Account Number": account_number,
    "Deposit Amount": deposit_amount,
    "Deposit Modes": deposit_modes,
    "Deposit Date": deposit_date,
    "Services Used": services_used
}

print("\n--- BANK DEPOSIT DETAILS ---\n")

# Comma separation
print("Account Holder, Account Number, Amount",
      bank_details["Account Holder"],
      bank_details["Account Number"],
      bank_details["Deposit Amount"],
      sep=", ")

# Percentage / numeric formatting
print("Deposit Amount: ₹%.2f" % bank_details["Deposit Amount"])

# f-string
print(f"Deposit Date: {deposit_date[0]}-{deposit_date[1]}-{deposit_date[2]}")
print(f"Deposit Modes: {deposit_modes}")
print(f"Services Used: {services_used}")

# format() method
print("Account Holder: {}, Account Number: {}".format(
    bank_details["Account Holder"],
    bank_details["Account Number"]
))
             
             


               
