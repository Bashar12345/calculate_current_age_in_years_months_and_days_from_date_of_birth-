"""Write a short program to calculate current age in years, 
months, and days from date of birth in JavaScript or Python.
*Note: Users must enter their date of birth from the input.
"""
"""We discourage you from using any built-in functions to solve the task.
 Also, submit the task if it is partially complete."""

class today:
    def __init__(self, din, mash, bosor):
        self.din = din
        self.mash = mash
        self.bosor = bosor
    # i did not use timezone.now() built-in

    def __repr__(self):
        return f'day: {self.din}, month: {self.mash}, year: {self.bosor}'

def din_dise():
    date=int(input()) 
    if 0<date<32:
        return date
    else:
        print("Enter a valid day")
        din_dise()

def mash_dise():
    month = int(input())
    if 0<month<13:
        return month
    else:
        print("Enter a valid month")
        mash_dise()

def bosor_dise(today):
    year = int(input())
    if 0 < year <= today.bosor:
        return year
    else:
        print("Enter a valid year/ Year cannot be after Birth year.")
        bosor_dise(today)


# given same name for better understanding
def current_age(today, jnmer_din, jnmer_mash, jnmer_bosor):
    if today.bosor > jnmer_bosor:
        bosor = today.bosor-jnmer_bosor
        if today.mash > jnmer_mash and today.din < jnmer_din:
            mash = today.mash-jnmer_mash
            mash -= 1
            din = (today.din + 30)-jnmer_din
        elif today.mash < jnmer_mash and today.din < jnmer_din:
            bosor = today.bosor-jnmer_bosor
            bosor -= 1
            mash = (today.mash + 12)-jnmer_mash
            mash -= 1
            din = (today.din + 30)-jnmer_din
        else:
            mash = today.mash-jnmer_mash
            din = today.din-jnmer_din

        y = 'years' if (bosor % 2) == 0 else 'year'
        m = 'months' if (mash % 2) == 0 else 'month'
        d = 'days' if (din % 2) == 0 else 'day'

        leap_days = int(bosor/4)
        # print(leap_days)

        print(f'Current age: {bosor} {y}, {mash} {m}, {din+leap_days} {d}')
    if today.bosor == jnmer_bosor and today.mash > jnmer_mash:
        print('Enter valid Date, You can"t born in the near future')



ajker_din = today(11, 3, 2022) # todays date
print(ajker_din)

print("Enter Date (0 to 31)")
jnmer_din = din_dise()  # print(din)

print("Enter Month like: 03 or 05")
jnmer_mash = mash_dise()

print("Enter Year like: 1964 or 2005")
jnmer_bosor = bosor_dise(ajker_din)

current_age(ajker_din, jnmer_din, jnmer_mash, jnmer_bosor)






# if today.bosor>jnmer_bosor and today.mash>jnmer_mash and today.din>jnmer_din:
#     bosor =today.bosor-jnmer_bosor
#     mash = today.mash-jnmer_mash
#     din = today.din-jnmer_din
#     print(f'Current age {bosor} year, {mash} month, {din} days')
    

# if today.bosor>jnmer_bosor and today.mash>jnmer_mash and today.din<jnmer_din:
#     bosor =today.bosor-jnmer_bosor
#     mash = today.mash-jnmer_mash
#     mash -=1
#     din = (today.din + 30)-jnmer_din
#     print(f'Current age {bosor} year, {mash} month, {din} days')
    

# if today.bosor>jnmer_bosor and today.mash<jnmer_mash and today.din<jnmer_din:
#     bosor =today.bosor-jnmer_bosor
#     bosor -=1
#     mash = (today.mash + 12)-jnmer_mash
#     mash -=1
#     din = (today.din + 30)-jnmer_din 
#     print(f'Current age {bosor} year, {mash} month, {din} days')
