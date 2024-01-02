# Hello explorer, you have been selected to be part of an early beta for a new system.
# If you encounter an issues with running, packager, and language server (autocomplete, code diagnostics),
# please email devex@replit.com or post on ask.replit.com
# You can always turn off explorer from https://replit.com/account#roles
# 
# Thank you!

print("Select your option :")
print("1. Create your profile. ")
print("2. Add roster to a month. ")
print("3. Update roster for a month. ")
print("4. See the week's roster. ")
print("5. View calendar. ")
print()
print()
choice = input("Enter your option :  ")
print(type(choice))

def run_roster_ops(chosen):
  match chosen:
    case "5":
      import calendar
      print("")
      _Year = 2023
      _Months = [6,7,8]
      for i in _Months:
        print(calendar.month(_Year, i))
    case "1":
      name=input("Enter your desired profile name : ")
      print(name)
    # case default:
    #         return "something"

  
run_roster_ops(choice)