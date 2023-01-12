import random
food_obj = {
    'rice':145,
    'pasta':120,
    'meat':50,
    'beans':80,
    'salad':15,
    'lasange':200,
    'eggs':25,
    'potatoes':135,
    'chicken':150,
    'lunch menu':250,
    }
def food_info():
    print("Available food:-")
    for i in food_obj:
        print(i,end=' ')

def total_food(orders):
    total=[]
    for choice in orders:
        print(choice)
        total.append(food_obj[choice])
    return sum(total)
def make_payment(card,total_cost):
    if card > total_cost:
        card-=total_cost
        return True
    else:
        return False


def print_reciept(orders,total_cost):
    print("Success!!!")
    reciept_num=random.randint(1000,10000)
    with open(f'somefile{str(reciept_num)}.txt', 'a') as file:
        file.write('Thanks for patronage \n *****SUCCESS******\n')
        for i in orders:
            file.write(f'{i} ------ {food_obj[str(i)]}Kr \n')
        file.write('==================== \n')
        file.write(f'Total cost :{total_cost}Kr')
        file.close()
    print("take your reciept")
def main():
    food_info()
    orders = input("Enter your food of choice seperated by space Example: Rice Beans!!").lower().split(" ")
    card=int(input("Enter your card balance:"))
    total_cost = total_food(orders)
    print(f'Your Food cost {total_cost}')
    payment=make_payment(card,total_cost)
    if payment:
        print_reciept(orders,total_cost)
    else:
        print("payment declined!")

if __name__ == '__main__':
    main();
