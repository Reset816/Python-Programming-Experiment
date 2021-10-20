# Experiment 3

## 1. 请解释并举例说明以下关键字的意义及用法：global lambda pass raise with assert finally nonlocal yield class from

- `global`

  在函数内部创建全局变量，或者在函数内部改变一个全局变量。

- `lambda`

  `lambda arguments : expression` 可以创建一个匿名函数。该匿名函数可以接受多个参数，但只能有一条语句。

- `pass`

  用作占位符，可以使用在函数、class、if 中

- `raise`

  引发一个异常

- `with`

   适用于对资源进行访问的场合，简化异常处理

- `assert`

   可以触发异常，并提供可指定的说明信息

- `finally`

  被 `finally` 修饰的语句块总会被执行

- `nonlocal`

  让被 `nonlocal` 声明的变量和函数外层的同名变量为同一个，以实现闭包。

  reference: [简谈Python3关键字nonlocal使用场景 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/96508259)

- `yield`

   带 `yield` 的函数是一个迭代器

- `class`

  用来创建一个类

- `from`

  从一个 module 中导入一个特定的 section。


## 2. 对print_unicode.py进行修改，当用户输入多个单词时，打印包含所有用户指定单词的Unicode字符名所在行的信息

- Code

  ```python
  import sys
  import unicodedata
  
  def print_unicode_table(word):
      print("decimal hex chr {0:^40}".format("name"))
      print("------- ----- --- {0:-<40}".format(""))
      #print("------- ----- --- {0}".format("-" * 40))
      code = ord(" ")
      end = sys.maxunicode
      while code < end:
          c = chr(code)
          name = unicodedata.name(c, "*** unknown ***")
          if word is None or word in name.lower():
              print("{0:7} {0:5X} {0:^3c} {1}".format(code, name.title()))
          code += 1
  
  word = None
  if len(sys.argv) > 1:
      if sys.argv[1] in ("-h", "--help"):
          print("usage: {0} [string]".format(sys.argv[0]))
          #print("usage: {0[0]} [string]".format(sys.argv))
          word = 0
      else:
          for i in range(1, len(sys.argv)):
              word = sys.argv[i].lower()
              if word != 0:
                  print_unicode_table(word)
  
  ```
  
- Example
  
  - ![image-20211013202747002](images/image-20211013202747002.png)

## 3. 对quadratic.py进行修改，当b、c为0时，对应的方程项不再输出，系数为负时，输出为-n而不是+-n。

- Code

  ```python
  import cmath
  import math
  import sys
  
  
  def get_float(msg, allow_zero):
      x = None
      while x is None:
          try:
              x = float(input(msg))
              if not allow_zero and abs(x) < sys.float_info.epsilon:
                  print("zero is not allowed")
                  x = None
          except ValueError as err:
              print(err)
      return x
  
  
  print(
      "ax\N{SUPERSCRIPT TWO} + bx + c = 0"
  )  # \N{name} Unicode character with the given name
  a = get_float("enter a: ", False)
  b = get_float("enter b: ", True)
  c = get_float("enter c: ", True)
  
  if not (b == 0 and c == 0):
  
      x1 = None
      x2 = None
      discriminant = (b ** 2) - (4 * a * c)
      if discriminant == 0:
          x1 = -(b / (2 * a))
      else:
          if discriminant > 0:
              root = math.sqrt(discriminant)
          else:  # discriminant < 0
              root = cmath.sqrt(discriminant)
          x1 = (-b + root) / (2 * a)
          x2 = (-b - root) / (2 * a)
  
      get_sign = lambda x: "+ " if x >= 0 else ""
      signb = get_sign(b)
      signc = get_sign(c)
      equation = (
          "{0}x\N{SUPERSCRIPT TWO} {1}{2}x {3}{4} = 0\N{RIGHTWARDS ARROW} x = {3}"
      ).format(a, signb, b, signc, c, x1)
      if x2 is not None:
          equation += " or x = {0}".format(x2)
      print(equation)
  
  ```

- Example
  - ![image-20211013204941801](images/image-20211013204941801.png)
  - ![image-20211013204956637](images/image-20211013204956637.png)

## 4. 从csv2html.py中删除escape_html()，用xml.sax.saxutils模块的xml.sax.saxutils.escape()函数替换。

- Code

  ```python
  import xml.sax.saxutils
  
  
  def main():
      maxwidth = 100
      print_start()
      count = 0
      while True:
          try:
              line = input()  # 输入数据到line
              if count == 0:
                  color = "lightgreen"
              elif count % 2:
                  color = "white"
              else:
                  color = "lightyellow"
              print_line(line, color, maxwidth)  # 输出每行内容
              count += 1
          except EOFError:
              break
      print_end()
  
  
  def print_start():
      print("<table border='1'>")  # 表格开始周围的边框设置为1像素宽
  
  
  def print_end():
      print("</table>")  # 表格结束
  
  
  def print_line(line, color, maxwidth):
      print("<tr bgcolor='{0}'>".format(color))  # tr行，td为单元格内容
      fields = extract_fields(line)  # 提取每行内容到列表fields
      for field in fields:
          if not field:
              print("<td></td>")  # 列表fields的每项若为空，打印空内容
          else:
              number = field.replace(",", "")  # 列表fields的每项若不为空，删除其中的逗号
              try:
                  x = float(number)  # number转换为浮点成功，若为数字，右对齐打印
                  print("<td align='right'>{0:d}</td>".format(round(x)))
              except ValueError:  # number转换为浮点失败，则为字符串
                  field = field.title()  # 字符串首字母大写
                  field = field.replace(" And ", " and ")
                  if len(field) <= maxwidth:  # 长度不超限
                      field = xml.sax.saxutils.escape(field)
                  else:  # 长度超限
                      field = "{0} ...".format(
                          xml.sax.saxutils.escape(field[:maxwidth])
                      )  # 取maxwidth长度替换、输出后加...
                      # field = "{0} ...".format(xml.sax.saxutils.escape (field[:maxwidth]))
                  print("<td>{0}</td>".format(field))  # 加标签生成html代码
      print("</tr>")
  
  
  def extract_fields(line):  # 提取内容到列表fields
      fields = []
      field = ""
      quote = None
      for c in line:  # 遍历line
          if c in "\"'":  # 是否有引号‘“
              if quote is None:  # start of quoted string
                  quote = c
              elif quote == c:  # end of quoted string
                  quote = None
              else:
                  field += c  # other quote inside quoted string
              continue
          if quote is None and c == ",":  # end of a field
              fields.append(field)
              field = ""
          else:
              field += c  # accumulating a field
      if field:
          fields.append(field)  # adding the last field
      return fields
  
  
  def escape_html(text):
      text = text.replace("&", "&amp;")
      text = text.replace("<", "&lt;")
      text = text.replace(">", "&gt;")
      return text
  
  
  main()
  """
  "COUNTRY", "2000", "2001", 2002, 2003, 2004
  "ANTIGUA AND BARBUDA", 0, 0, 0, 0, 0
  """
  
  ```

- Example
  - ![image-20211013210408251](images/image-20211013210408251.png)
  
    得到 `html` 文件
  
    ![image-20211013210458973](images/image-20211013210458973.png)
  
    打开 `html` 文件
  
    ![image-20211013210311784](images/image-20211013210311784.png)

## 5. 再次修改csv2html.py，这一次添加一个名为process_options（）的新函数。此函数应从main（）调用，并返回两个值的元组：maxwidth（一个int）和format（一个str）。 调用process_options（）时，应将默认最大宽度设置为100，默认格式为“.0f”，这将在输出数字时用作格式说明符。 如果用户在命令行上键入“ -h”或“ --help”，则应输出用法消息并返回（None，None）。（在这种情况下，main（）不应执行任何操作。）否则，该函数应读取给定的任何命令行参数并执行适当的分配。 例如，如果给出“maxwidth = n”，则设置maxwidth；如果给出“format = s”，则类似地设置format。显示用法的输出内容略。命令行实例：csv2html2_ans.py maxwidth=20 format=0.2f < mydata.csv > mydata.html

- Code

  重点是增加了函数`process_options`

  ```python
  def process_options():
      maxwidth = 100
      format = ".0f"
      if len(sys.argv) > 1:
          if sys.argv[1] == "-h" or sys.argv[1] == "--help":
              print("Example:")
              print("csv2html2_ans.py maxwidth=20 format=0.2f < mydata.csv > mydata.html")
              return (None, None)
  
          for i in range(1, len(sys.argv)):
              if sys.argv[i][:9] == "maxwidth=":
                  maxwidth = int(sys.argv[i][9:])
                  # print(maxwidth)
              if sys.argv[i][:7] == "format=":
                  format = sys.argv[i][7:]
                  # print(format)
  
      return (maxwidth, format)
  ```

  以及修改了 `print` 的格式控制串

  ```python
  formatter_string = "<td align='right'>{0:" + num_format + "}</td>"
  print(formatter_string.format(round(x)))
  ```

- Code

  ```python
  import xml.sax.saxutils
  import sys
  
  
  def main():
      if process_options() == (None, None):
          return
      else:
          maxwidth = process_options()[0]
          num_format = process_options()[1]
          print_start()
          count = 0
          while True:
              try:
                  line = input()  # 输入数据到line
                  if count == 0:
                      color = "lightgreen"
                  elif count % 2:
                      color = "white"
                  else:
                      color = "lightyellow"
                  print_line(line, color, maxwidth, num_format)  # 输出每行内容
                  count += 1
              except EOFError:
                  break
          print_end()
  
  
  def print_start():
      print("<table border='1'>")  # 表格开始周围的边框设置为1像素宽
  
  
  def print_end():
      print("</table>")  # 表格结束
  
  
  def print_line(line, color, maxwidth, num_format):
      print("<tr bgcolor='{0}'>".format(color))  # tr行，td为单元格内容
      fields = extract_fields(line)  # 提取每行内容到列表fields
      for field in fields:
          if not field:
              print("<td></td>")  # 列表fields的每项若为空，打印空内容
          else:
              number = field.replace(",", "")  # 列表fields的每项若不为空，删除其中的逗号
              try:
                  x = float(number)  # number转换为浮点成功，若为数字，右对齐打印
                  formatter_string = "<td align='right'>{0:" + num_format + "}</td>"
                  # print("<td align='right'>{num_format}</td>".format(round(x)))
                  print(formatter_string.format(x))
  
              except ValueError:  # number转换为浮点失败，则为字符串
                  field = field.title()  # 字符串首字母大写
                  field = field.replace(" And ", " and ")
                  if len(field) <= maxwidth:  # 长度不超限
                      field = xml.sax.saxutils.escape(field)
                  else:  # 长度超限
                      field = "{0} ...".format(
                          xml.sax.saxutils.escape(field[:maxwidth])
                      )  # 取maxwidth长度替换、输出后加...
                      # field = "{0} ...".format(xml.sax.saxutils.escape (field[:maxwidth]))
                  print("<td>{0}</td>".format(field))  # 加标签生成html代码
      print("</tr>")
  
  
  def extract_fields(line):  # 提取内容到列表fields
      fields = []
      field = ""
      quote = None
      for c in line:  # 遍历line
          if c in "\"'":  # 是否有引号‘“
              if quote is None:  # start of quoted string
                  quote = c
              elif quote == c:  # end of quoted string
                  quote = None
              else:
                  field += c  # other quote inside quoted string
              continue
          if quote is None and c == ",":  # end of a field
              fields.append(field)
              field = ""
          else:
              field += c  # accumulating a field
      if field:
          fields.append(field)  # adding the last field
      return fields
  
  
  def escape_html(text):
      text = text.replace("&", "&amp;")
      text = text.replace("<", "&lt;")
      text = text.replace(">", "&gt;")
      return text
  
  
  def process_options():
      maxwidth = 100
      format = ".0f"
      if len(sys.argv) > 1:
          if sys.argv[1] == "-h" or sys.argv[1] == "--help":
              print("Example:")
              print("csv2html2_ans.py maxwidth=20 format=0.2f < mydata.csv > mydata.html")
              return (None, None)
  
          for i in range(1, len(sys.argv)):
              if sys.argv[i][:9] == "maxwidth=":
                  maxwidth = int(sys.argv[i][9:])
                  # print(maxwidth)
              if sys.argv[i][:7] == "format=":
                  format = sys.argv[i][7:]
                  # print(format)
  
      return (maxwidth, format)
  
  
  main()
  ```
  
  
  
- Example

  - 输入：
  
    <img src="images/image-20211020191237004.png" alt="image-20211020191237004" style="zoom:50%;" />
  
    打开得到的html文件：
  
    <img src="images/image-20211020191445464.png" alt="image-20211020191445464" style="zoom:50%;" />
  
  - 输入：
  
    <img src="images/image-20211020191737634.png" alt="image-20211020191737634" style="zoom:50%;" />
  
    打开得到的html文件：
  
    <img src="images/image-20211020191811611.png" alt="image-20211020191811611" style="zoom: 50%;" />

  - 输入：
  
    <img src="images/image-20211020191558572.png" alt="image-20211020191558572" style="zoom:50%;" />