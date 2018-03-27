import re

numlist=[]##用于存储行数
def getlist(filename):
    pattern = re.compile(r'.{,3}因为.*所以.{,3}')#正则表达式对象
    text = open(filename, 'r')
    result_list = []
    num=0
    for line in text:
        num+=1
        result = pattern.findall(line)
        if result:
            result_list.append(line)#存储含有因为所以的句子
            numlist.append(num)
        else:
            continue
    return result_list

if __name__ == '__main__':

    output = open('output.txt', 'w')
    flag = 0
    acc = []

    for i,each in enumerate(getlist('input.txt')):
        tmp = []
        tmp.append(str(numlist[i]))
        split0 = each.split('因为', 1)[0][-3:]#靠左分割，分割次数为1
        while len(split0) < 3:
            split0 += '　'#长度补全 全角空格
        tmp.append(split0)
        tmp.append('*因为*')
        split1 = each.split('因为', 1)[1].rsplit('所以', 1)[0]
        if flag < len(split1):
            flag = len(split1)
        tmp.append(split1)
        tmp.append('*所以*')
        tmp.append(each.rsplit('所以', 1)[1][:3])#所以后三个自负
        acc.append(tmp)

    for i,each in enumerate(acc):#因为和所以中间长度 格式一致
        while len(each[3])<flag:
            each[3] += '　'
        acc[i] = each
        output.write('\t'.join(each)+'\n')#插入空格和换行符



