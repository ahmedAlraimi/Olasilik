# PIGEONHOLE PRINCIPLE :

The Pigeonhole Principle (`also known as the Dirichlet box principle, Dirichlet principle or box principle`) states that if n + 1 or more pigeons are placed in n holes, then one hole must contain two or more pigeons.

![Figure 1 Pigeonhole Principle Illustration](https://github.com/ahmedAlraimi/Olasilik/raw/master/HW1/img/pigeon.jpg)
Figure 1: Pigeonhole Principle Illustration

> Simply, This principle states If more than _n_ objects are placed into _n_  boxes, then at least one box must contain more than one object.

This principle might appear to be too obvious to be useful; indeed, the power of the principle comes from cleverly choosing the `boxes` and `objects`. Even though the principle itself is quite simple, it is not always clear if it is useful and, if so, how. For instance, consider the following example:

## Fruit Basket

A fruit basket contains 4 different pairs of fruits, 2 Banana, 2 apple, 2 orange and  2 strawberry (TOTAL = 8 fruits). Suppose that I need to grap out the fruits without looking at fruits before taking them out. How many fruits must I grap out to make sure that I will get a two of a kind ?

### *Answer :*

Based on the question, we can figure out the each of the fruit kind is a `boxes, pigeonhole` and each fruit drawn being is `object , pigeon`

According to the question above we can assume that in case graping 1, 2, 3, or 4 fruit(s), it is possible that all may be distinct fruits. Given a selection of let us say 4 fruit, it is likly that one is banana, one is orange one is strawberry ,and one is apple. However, if 5 fruits are chosen, the pigeon principle ensures that two [underline]#must# be the same. Hence the minimum number of fruit to be graped out is **5**.

```python
# Preprocess - check entry
    def preProcess(num):
	if (w_number > 0)  and (w_number  < 9):
		return True
	else:
		return False
#End of preProcess
	
	while True:
	box = 4 # pigeonhole : number of fruit kinds (banana , apple , orange , and strawberry)
	print("Please enter number of fruits withdrawals (Max : Number of fruits = 8 fruits : ")
	w_number = int(input())  # object , pigeon
	if preProcess(w_number) == True:
		if w_number <= box:
			print(" It is possible that all fruits may be distinct - no pigeonhole rule")
		else:
			if w_number == 8:
				print(" all pair matched")
			else:
				minimum = w_number % box
				print(" It is possible that " + str(minimum) + " pair matched")
			
	else:
		print("Range must be between 1 - 8 ")

```
