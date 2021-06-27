print("Hello Bittu !!!")
first = input("How are you ?  ")
password = input("Please inter your code  ")
if password != "Bittu@391":
    print("enter the correct code")
print("Enter the required data for Weekly covid positive cases graph in india ")
day = []
covid = []
for i in range(7):
    day.append(input("enter the name of days.  "))
    covid.append(int(input("Enter the covid positive cases accourding to day ")))
import matplotlib.pyplot as plt
plt.plot(day,covid)
plt.ylabel('covid cases')
plt.xlabel('day')
plt.title('Weekly Covid positive cases graph of india')
plt.show()
plt.hist(covid,bins=7)
plt.show()