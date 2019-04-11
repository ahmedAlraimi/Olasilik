# Bayes’ Theorem

is a way to figure out ```conditional probability```. which is the probability of an event happening, given that it has some relationship to one or more other events.
 
>  Simply, is a way of finding a probability when we know certain other probabilities!



### Ex:

In three different schools, students entered the final exams. in school A there were 60 students, school B 90 students, and school C 100 students.

knowing that the students success rate in school A is 70%, school B 60%, and school C is 60%. 

If a randomly selected student which has succeeded  in the exams, what is the probability that the student is from school B ?

#### Answer:


Using Bayes' Theorm formula, 

<img src="https://github.com/ahmedAlraimi/Olasilik/raw/master/HW3/img/Bayes_Theorem.png" />
 
Pr(H|E) = Chance of being a student in school B (H) given that passing the exams(E). This is what we want to know: How likely is it to have a student in school B who passed all exams?.

Pr(E|H) = Chance of successfull student (E) given that student from school B (H). 

Pr(H) = Chance of school B student.
Pr(not H) = Chance of other schools students.
Pr(E|not H) = Chance of successfull student (E) given that is not from school B (not H). 

* School A student: 


Pr(H<sub>A</sub>)/E = 60/250

Pr(H<sub>B</sub>)/E = 90/250

Pr(H<sub>C</sub>)/E = 100/250


Pr(H|E) = (90/250) x 0.6 / [  (90/250) × 0.60 + (60/250) × 0.70 + (100/250) × 0.50 ]

Pr(H|E) = 0.216 / 0.168 + 0.22 = 0.216/0.604 = 0.358


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
