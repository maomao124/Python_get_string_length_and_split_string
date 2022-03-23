"""
 * Project name(项目名称)：Python获取字符串长度和分割字符串
 * Package(包名): 
 * File(文件名): test2
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/23 
 * Time(创建时间)： 19:38
 * Version(版本): 1.0
 * Description(描述)： 分割字符串

 split() 方法可以实现将一个字符串按照指定的分隔符切分成多个子串，这些子串会被保存到列表中（不包含分隔符），作为方法的返回值反馈回来。
str.split(sep,maxsplit)
str：表示要进行分割的字符串；
sep：用于指定分隔符，可以包含多个字符。此参数默认为 None，表示所有空字符，包括空格、换行符“\n”、制表符“\t”等。
maxsplit：可选参数，用于指定分割的次数，最后列表中子串的个数最多为 maxsplit+1。如果不指定或者指定为 -1，则表示分割次数没有限制。

在 split 方法中，如果不指定 sep 参数，需要以str.split(maxsplit=xxx)的格式指定 maxsplit 参数。
 """

if __name__ == '__main__':
    str1 = "12121341214214535352534534523546234"
    list1 = str1.split("2")
    print(list1)
    print(type(list1))
    list1 = str1.split("2", 3)
    print(list1)

    input()
