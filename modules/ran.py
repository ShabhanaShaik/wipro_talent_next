#random
import random
print("random num from 10 to 50",random.randint(10,50))
print("random num from 0 to 1",random.random())
#for floating random num(uniform)
print("random num from 1.5 to 5.5",random.uniform(1.5,5.5))
#choice
fruits=['banana','app','orange','mango']
print("random fruit",random.choice(fruits))
#more than one choice
print("random fruit",random.choices(fruits,k=3))
num=[1,2,3]
random.shuffle(num)
print("shuffle list",num)
print("sampled elements",random.sample(num,k=2))
#seed -->random num generated is fixed and that random value is same repetaed always
random.seed(24)
print("random  same number",random.randint(10,50))