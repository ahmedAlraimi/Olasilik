

# Bernoulli Distribution:


a discrete distribtuion having two possible outcomes labelled by ``` n = 0 ``` & ``` n = 1 ```=>success. ``` n = 1 'success'``` occurs with probability ``` p ``` and ``` n = 0 'failure '``` occurs with probability ``` q = 1 - p ``` , ``` 0 < p < 1 ``` . Bernoulli distribution is a special case of binomial distribution, specially when ``` n = 1 ``` the binomial distribution becomes Bernoulli distribution.


### Ex:

```
You sell sandwiches. 70% of people choose chicken, the rest choose something else. What is the probability of selling 2 chicken sandwiches to the next 3 customers?
```

The probabilities for "two chickens" all work out to be 0.147, because we are multiplying two 0.7s and one 0.3 in each case. In other words

``` 0.147 = 0.7 × 0.7 × 0.3 ```

The 0.7 is the probability of each choice we want, call it p

The 2 is the number of choices we want, call it k

And we have (so far) : pk × 0.31

The 0.3 is the probability of the opposite choice, so it is: 1−p

The 1 is the number of opposite choices, so it is: n−k

Which gives us: ``` p<sup>k</sup>(1-p)<sup>(n-k)</sup> ```

Where

p is the probability of each choice we want

k is the the number of choices we want

n is the total number of choices

p = 0.7 (chance of chicken)
k = 2 (chicken choices)
n = 3 (total choices)

p<sup>k</sup>(1-p)<sup>(n-k)</sup> = 0.7<sup>2</sup>(1 - 0.7)<sup>(3-2)</sup>

p<sup>k</sup>(1-p)<sup>(n-k)</sup>  = 0.7 x 0.7 x 0.3 = 0.147

#### -CODE:
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1DJd2KOTW-KooQS-_8xDHL7RJ7DS0ub2T#scrollTo=7WCI3T5eu9Qg&line=3&uniqifier=1)


``` python
import math


# p is the probability of each choice we want
p = 0.7

# k is the the number of choices we want
k = 2

# n is the total number of choices
n = 3


# p^k (1-p)^(n-k) = 0.7^2(1 - 0.7)^(3-2)
Answer = (p**k)*((1-p)**(n-k))

print ("  The probabilities for - two chickens- all work out to be= ",end="")
print (Answer)

``` 

#### Answer :
``` 
The probabilities for - two chickens- all work out to be= 0.147

``` 

# Variance:

### Ex:

```
A company makes sports bikes. 90% pass final inspection (and 10% fail and need to be fixed). What is the expected ``` Mean ``` and ``` Variance ``` of the 4 next inspections?
```
Variance: σ2 = n p (1-p)

#### -CODE:
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1DJd2KOTW-KooQS-_8xDHL7RJ7DS0ub2T#scrollTo=1Zdov-7f6Ygu&line=12&uniqifier=1)


``` python

# p = P(pass)
p = 0.9

n = 4


Answer =  n * p * (1-p)

print (" For the sports bikes, Variance = ",end="")
print (round(Answer, 2))

``` 

#### Answer :
``` 
 For the sports bikes, Variance = 0.36

``` 

# Binomial Distribution:

A binomial distribution can be thought of as simply the probability of a SUCCESS or FAILURE outcome in an experiment or survey that is repeated multiple times. The binomial is a type of distribution that has two possible outcomes (the prefix “bi” means two, or twice). For example, a coin toss has only two possible outcomes: heads or tails and taking a test could have two possible outcomes: pass or fail. 

### Ex:

```
The chances of a team winning a match is 0.7. Find the probability that the team will win at least one match out of three.
```
Probability of winning a match, p = 0.7


Probability of winning zero matches, P(X = 0) = n!/(k!(n-k)! ) * (0.7)<sup>0</sup>(0.3)<sup>3</sup> = 0.027

Probability of winning at least one match = 1 - 0.027 = 0.973

#### -CODE:
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1DJd2KOTW-KooQS-_8xDHL7RJ7DS0ub2T#scrollTo=4TFuA_7Q9LpV&line=23&uniqifier=1)


``` python

import math

# Probability of winning a match
p = 0.7

n = 3
k = 0


#Probability of winning zero matches, P(X = 0) = C(3,0) (0.7)0(0.3)3 = 0.027

Zero_match = (math.factorial(n) / (math.factorial(n-k) * math.factorial(k))) * ((p**k)*((1-p)**(n-k)))

print ("Probability of winning zero matches = ",end="")
print (round(Zero_match, 3))


# Probability of winning at least one match = 1 - Zero_match = 

print ("Probability of winning at least one match = ",end="")
print (round(1- Zero_match, 3))

``` 

#### Answer :
``` 
Probability of winning zero matches = 0.027
Probability of winning at least one match = 0.973

``` 
