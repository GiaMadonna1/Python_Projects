#1
def arb_args(*args):
    for seperate in args:
        print(seperate)
#2
def inner_func (x, y):
    def x_out():
        return x * y

    def y_up():
        return y - x
    
    total_sum = x_out() + y_up()

    print(total_sum)
#3
def lunch_lady(name, lunch="Mystery Meat"):
    print(name, lunch)
     
#4
def sum_n_product(param1, param2):
    value1= param1 + param2
    value2= param1 * param2
    print(value1, value2)  

#5
alias_arb_args = arb_args

#6 doesn't divide by the total right even after trying solution code. 
def arb_mean(*args):
    total= 0
    for all in args:
      total += all
    print(all/len(args))

#7 I didn't quite understand this one. By breaking it down, long seems to be a base line character count.
#  Then, it takes the longest character count string and prints it. 
def arb_longest_string(*args):
    long = 0
    longest = " "
    for a in args:
        if len(a) > long:
            long = len(a)
            longest = a
    print(longest)
    
















arb_args('eminem', 1, 'slim shady', False)

inner_func(20,10)

lunch_lady("Gia", "Chicken Nuggets")
# If you call in an array it will print the = value after your string values.

sum_n_product(24, 5000)

arb_mean(24,25,26)

arb_longest_string("jijsjdsjoa", "mmmmmmmmmmmmmmmmmm", "p")