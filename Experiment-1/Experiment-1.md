# Experiment 1

## 8.1

- Code

  ```python
  def cal(x):
      if (x <= 0):
          return 3 * x + 5
      elif (0 < x <= 1):
          return x + 5
      elif (x > 1):
          return -2 * x + 8
  
  
  try:
      x = input("Please input x:")
      print("f(x)=", cal(float(x)))
  except ValueError as err:
      print(err, "is not a number")
  
  ```

- Example

  - ![image-20210915165816841](images/image-20210915165816841.png)

    此处原本想用`raise ValueError`语句，但后来发现这里转换不成功就会自动抛出错误。

  - ![image-20210915165657480](images/image-20210915165657480.png)
  - ![image-20210915170132850](images/image-20210915170132850.png)
  - ![image-20210915170150920](images/image-20210915170150920.png)

## 8.2

- Code

  ```python
  def cal_factorial(x):
      factorial = 1
      tmp = 1
      while tmp <= int(x):
          factorial = factorial * tmp
          tmp = tmp + 1
      return factorial
  
  
  i = 1
  while i <= 10:
      print("Factorial of ", str(i), " is ", cal_factorial(i))
      i = i + 1
  
  ```

- Example
  - ![image-20210915170555995](images/image-20210915170555995.png)

## 8.3

- Code

  ```python
  def cal_factorial(x):
      factorial = 1
      for i in range(1, x + 1):
          factorial = factorial * i
      return factorial
  
  
  for i in range(1, 11):
      print("Factorial of ", str(i), " is ", cal_factorial(i))
  
  ```

- Example
  - ![image-20210915171013988](images/image-20210915171013988.png)

## 8.4

- Code

  ```python
  s = input("enter an integer: ")
  try:
      i = int(s)
      print("valid integer entered:", i)
  except ValueError as err:
      print(err)
  
  ```

- Example
  - ![image-20210915171102830](images/image-20210915171102830.png)

  - ![image-20210915171113944](images/image-20210915171113944.png)

    
