import random

st=["watermelon", "watermelun","rabit", "raibit","storage","storige"]

for i in range(2):
    if i==1:
        if select_random_index%2==0:
            store_index = select_random_index
            show_random = st[store_index]
            print(show_random, end=" ")
        else:
            show_random = st[select_random_index-1]
            print(show_random, end=" ")
    else:
        select_random = random.choice(st)
        select_random_index = st.index(select_random)
        print(select_random, end=" ")
print()
find=input("Which is correct write correct spelling of this word:\n")

if find==st[select_random_index]:
    print("You Lose")
else:
    print("You Win")