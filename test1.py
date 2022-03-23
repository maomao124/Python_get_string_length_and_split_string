"""
 * Project name(项目名称)：Python获取字符串长度和分割字符串
 * Package(包名): 
 * File(文件名): test1
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/23 
 * Time(创建时间)： 19:31
 * Version(版本): 1.0
 * Description(描述)： 要想知道一个字符串有多少个字符（获得字符串长度），或者一个字符串占用多少个字节，可以使用 len 函数。
 len（string）
其中 string 用于指定要进行长度统计的字符串。
 """

if __name__ == '__main__':
    str1 = "To find out how many characters a string has (to get the string length)," \
           " or how many bytes a string occupies, use the len function."
    print(str1)
    print(len(str1))

    # 字节数
    print(len(str1.encode()))

    # utf-16be编码
    print(len(str1.encode("utf-16be")))

    str2 = "string用于指定要进行长度统计的字符串"
    print(str2)
    print(len(str2))

    # 字节数
    print(len(str2.encode()))

    # utf-16be编码
    print(len(str2.encode("utf-16be")))

    input()
