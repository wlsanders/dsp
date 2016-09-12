# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

Python Lists: 
Sequence of values. They can be any type, the values in a list are called elements or sometimes items. 
Lists are mutable


Tuples: They are immutable (Big Difference). They can be any type. 

Tuples will work as keys in a dictionary, lists can't be used as a key in a dictionary. 

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

sets: unordered, a set requires items to be hashable but a list does not. Sets can't contain duplicates, sets do not allow indexing. 

Sets are significantly faster if determining if an object is located in the set but are slower when you iterate over the contens. 

tryingSets = set([1,2,3,4, 4,5,6,5,4,3,2,1])
tryingLists = list([1,2,3,4,4,4,3,2,5])

print tryingSets prints [set([1, 2, 3, 4, 5, 6]) and print tryingLists prints [1, 2, 3, 4, 4, 4, 3, 2, 5]]

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> The lambda function is a way to create small anonymous functions, i.e. functions without a name. 

A quick example would be f = lambda x, y: x + y
print f(1,1) -> prints 2

Another example is taken from [link](https://docs.python.org/2.7/howto/sorting.html). 

student_tuples = [
('john', 'A', 15),
('jane', 'B', 12),
('dave', 'B', 10),
]
print sorted(student_tuples, key=lambda student: student[2])   # sort by age
# prints [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]






---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> REPLACE THIS TEXT WITH YOUR RESPONSE

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937 days

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513 days

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850 days

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





