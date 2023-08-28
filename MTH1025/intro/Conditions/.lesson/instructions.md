# Conditions

The built in function `np.sqrt` does not give an answer when the input is negative. Of course, if the input is negative, you should get an imaginary solution.

Define a new function called `better_sqrt` which when given a value `x`, tests it to see if it is positive or negative.

If it is positive, the function should return the square root of that number, as given by `np.sqrt`.

If it is negative, then your function should calculate the square root of `-x`  and then return this value multiplied by the imaginary number (recall that the imaginary number in python is designated by the variable `1j`)

```
>> print(1j)
1j
>> print(7*1j)
7j
>> print(1j**2)
(-1,0j)
```
