# Probability Mass Function

Before defining the probability mass function, recall that Recall that a ```random variable``` is a variable whose value is the outcome of a random event. For example : a random variable could be the outcome of the flip of a coin or the roll of a die. and also remember that a ```probabiliy distribution``` is a list of all of the possible outcomes of a random variable along with their corresponding probability values.
 
 For example, the following table represents the probability distribution of a fair 6 sided die.




|Outcome of die roll  | 1 | 2 | 3 | 4 | 5 | 6 |  
| -- | -- | -- | -- | -- | -- | -- 
| Probability | 1/6 | 1/6 | 1/6 | 1/6 | 1/6 | 1/6 |
|  |  |  |  |  |  |  

In the above example of rolling a six-sided die, there were only six possible outcomes so we could write down the entire probability distribution in a table. In many scenarios, the number of outcomes can be much larger and hence a table would be tedious to write down. Worse still, the number of possible outcomes could be infinite. 

To get around the problem of writing a table for every distribution, we can define a function instead. The function allows us to define a probability distribution succinctly.

## probability mass function definition:

When we use a probability function to describe a discrete probability distribution we call it a probability mass function (commonly abbreviated as pmf).

A probability mass function, which we’ll call “f” returns the probability of an outcome. Therefore, a probability mass function is written as:

``` math
f(x) = P(X = x) 
```
pmf 'f' just returns the probability of the outcome x.

Since a probability mass function returns probabilities it must obey the rules of probability. Namely, the probability mass function outputs values between 0 and 1 inclusive and the sum of the probability mass function (pmf) over all outcomes is equal to 1. 
 
``` math
 0 <= f(x) <= 1
```


### Ex:

Let's toss a fair coin **3** times, where the ``` Random variable ``` X is the number of tosses. therefore the sample space :: S = {HHH , HHT, HTH, HTT, THH, THT, TTH, TTT}
Thus X : S -> R looks like :

X(HHH) = 3 heads
X(HHT) = X(HTH) = X(THH) = 2 heads
X(HTT) = X(THT) = X(TTH) = 1 head
X(TTT) = 0 heads

Thus RANGE(X) = {0 , 1, 2, 3} so 
probability mass function is given by : 
P(X = 0) = 1/8, P(X = 1) = 3/8, P(X = 2) = 3/8, P(X = 3) = 1/8

so,

Px(0) = 1/8, 
Px(1) = 3/8, 
Px(2) = 3/8, 
Px(3) = 1/8


#### -CODE:
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1_5ClkaNf2q2m29TcEI1deBcVMOWQ1XEI#scrollTo=7WCI3T5eu9Qg)


``` python

import numpy as np
import pandas as pd

# S = {HHH , HHT, HTH, HTT, THH, THT, TTH, TTT}

# X(HHH) = 3 heads
# X(HHT) = X(HTH) = X(THH) = 2 heads
# X(HTT) = X(THT) = X(TTH) = 1 head
# X(TTT) = 0 heads

S = np.array([3, 2, 2, 1, 2, 1, 1, 0])

print(S)

df = pd.DataFrame(S)

df = pd.DataFrame(df[0].value_counts())
df

length = len(S)
print(length)

data = pd.DataFrame(df[0])

data.columns = ["Counts"]

#PMF
data["Prob"] = data["Counts"]/length

data


``` 

#### Answer :
``` 

[3 2 2 1 2 1 1 0]
8
Counts	Prob
2	3	0.375
1	3	0.375
3	1	0.125
0	1	0.125

``` 

___
