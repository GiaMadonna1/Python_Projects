def hello():
    print("Greetings User")

def pack(e,f,g):
    return[e,f,g]


def eat_lunch(meal):
    if len(meal) == 0:
        print("My lunchbox is empty!")
    else:
        for i in range(len(meal)):
            if i == 0:
                print(f"First I eat {meal[0]}")
            else:
                print(f"Next i eat {meal[i]}")


hello()
print(pack("e","f","g"))
eat_lunch(meal=["ramen", "pizza","sandwich"])
