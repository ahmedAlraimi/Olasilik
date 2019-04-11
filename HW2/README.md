# Combinations and Permutations

Both terms concern about calculating all the possible ways of doing something. How many times a certain event is going to happen. 

>  SO what is the difference ?!!! 

The difference between Combination & Permutation is :

<img src="https://github.com/ahmedAlraimi/Olasilik/raw/master/HW2/img/order.png" width="100" height="100" />

### "ORDER"	

 

 -  When the order doesn't matter, it is a  **`Combination`**.
 ex. **_fruit salad is a combination of apples, grapes and bananas_**
 
  -   When the order  **does**  matter it is a    **`Permutation`**.
  ex. **_The combination to the safe is 159_**

## Permutation Examples:-

### Ex:1 

```   In how many ways can the letters in the word  ```   **HELLO** ```  be arranged where ``` **L**'s ``` are together ?```   

#### Answer:

In order to solved this example we need to consider both **L**'s as a one member.  as
``` H```   ``` E```  ``` LL```  ``` O``` .  So by doing that simply we can say that the number of arrangement = 4! = 4 X 3 X 2 X 1 = 24

#### -CODE:
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1v1vt9ZJAcLw-IzzyfHTy2RH3vQfQG7m6?authuser=1#scrollTo=VCKLZAWm_Mos)
``` python
import math 
# (H) (E) (LL) (O) : # of arrangement = 4!
elements = 4

# 4! = 4 X 3 X 2 X 1 = 24
Answer = math.factorial(elements) 
print ("  Number of arrangement of letters = ",end="")
print (Answer)
``` 

___

### Ex:2
```   In how many ways can  ```   **3 women** ``` and ``` **4 men** ``` sit in a line if the women always sit together ? ```   

#### Answer:

We can also use the same method of grouping the members that are going to sit together as : (W W W) (M) (M) (M) (M)

plus to identify that they are different we may write a subscript to it,
(W<sub>1</sub> W<sub>2</sub> W<sub>3</sub>) (M<sub>1</sub>) (M<sub>2</sub>) (M<sub>3</sub>) (M<sub>4</sub>) 

as the first example we can say that the number of arrangement = 5!   
>REMINDER:  There are 3 women !!

For the reason above, within the women group, there can be an arrangement of : 3! 

SO, the TOTAL # of arrangement = 5! X 3! = 5 X 4 X 3 X 2 X 3 X 2 =   720 


#### -CODE:
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1v1vt9ZJAcLw-IzzyfHTy2RH3vQfQG7m6?authuser=1#scrollTo=IGVJtNCd_R-u)
``` python
import math 
# (W1 W2 W3) (M1) (M2) (M3) (M4)
overall_elements = 5
# (W1 W2 W3)
women_elements = 3


# the TOTAL # of arrangement = overall_elements(5)! X  women_elements(3)! 
Answer = math.factorial(overall_elements) * math.factorial(women_elements)
print ("  Number of arrangement  = ",end="")
print (Answer)
``` 

## Combination Examples:-

### Ex:1
```   In a lottery, each ticket has   ```   **5**  ``` one-digit numbers (0 - 9) on it, You win if your ticket has the digits in any order. What are you r chances of winning ? ```   

#### Answer:

For each digit there are 10 numbers that can be chosen at a time.

Using the formula, 10 choose 5
C(10,5) = (<sup>10</sup><sub>5</sub>) =
```10! ``` / ```( 10! - 5! ) (5!) ``` = ``` 10 X 9 X 8 X 7 X 6 ``` /  ```5 X 4 X 3 X 2 X 1 ``` = 252

> NOTE : Click on Pascal's Triangle !
>
[![Pascal's Triangle](https://www.mathsisfun.com/numbers/images/pascals-triangle-add.svg)](http://codinglab.huostravelblog.com/math/pascals-triangle-generator/index.php?size=17&alignment=Center&order=0&presentation=1)


#### -CODE:
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1v1vt9ZJAcLw-IzzyfHTy2RH3vQfQG7m6?authuser=1#scrollTo=uHcZrew7_c9D)
```python
import math 
# 10 numbers (0-9) CHOOSE 5 digits	
numbers = 10
digits = 5

# C(10,5) = 10!  / ( 10! - 5! ) (5!) 
Answer = math.factorial(numbers) / (math.factorial(numbers-digits) * math.factorial(digits))
print (" Your chances to win is 1 out of ",end="")
print (Answer)

```
