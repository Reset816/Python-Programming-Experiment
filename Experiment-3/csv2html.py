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
"""
"COUNTRY", "2000", "2001", 2002, 2003, 2004
"ANTIGUA AND BARBUDA", 0, 0, 0, 0, 0
"""
