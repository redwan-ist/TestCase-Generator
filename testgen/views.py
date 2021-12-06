from django.shortcuts import render
import random
# Create your views here.


def index(request):
    return render(request, 'index.html')


def gen1d(request):
    if request.method == 'POST':
        try:
            total_testcase = int(request.POST['total_testcase'])
            single_testcase = int(request.POST['single_testcase'])
            maximum = int(request.POST['max'])
            minimum = int(request.POST['min'])
            flag = 0 if "hideItemNo" in request.POST else 1
            src = str(total_testcase)+"\n" + \
                (str(single_testcase)+"\n" if flag else "")

        except:
            src = "wrong Data Type"
            return render(request, 'options/gen1d.html', {'data': src})

        if 'unique' in request.POST:
            for i in range(total_testcase):
                try:
                    sub = random.sample(
                        range(minimum, maximum+1), single_testcase)
                    print(sub)
                    src += ' '.join(str(x) for x in sub)
                    if(i < total_testcase-1) and flag:
                        src += "\n" + str(single_testcase)+"\n"
                    else:
                        src += "\n"

                except:
                    src = "Sorry \nmaximum - minimum < total unique number"
                    break
        else:
            for i in range(total_testcase):

                sub = []
                for j in range(single_testcase):
                    sub.append(random.randint(minimum, maximum))
                src += ' '.join(str(x) for x in sub)
                if(i < total_testcase-1) and flag:
                    src += "\n" + str(single_testcase)+"\n"
                else:
                    src += "\n"

        return render(request, 'options/gen1d.html', {'data': src})

    return render(request, 'options/gen1d.html')


def gen2d(request):
    if request.method == 'POST':
        try:
            total_testcase = int(request.POST['total_testcase'])
            row = int(request.POST['row'])
            column = int(request.POST['columm'])
            maximum = int(request.POST['max'])
            minimum = int(request.POST['min'])
            src = str(total_testcase)+"\n" + str(row) + " "+str(column)+"\n"
        except:
            src = "wrong Data Type"
            return render(request, 'options/gen2d.html', {'data': src})
        if "unique" in request.POST:
            for i in range(total_testcase):
                try:
                    sub = random.sample(range(minimum, maximum+1), row*column)
                    for j in range(row*column):
                        src += str(sub.pop(0))+" "
                        if((j+1) % column == 0):
                            src += "\n"

                    if(i < total_testcase-1):
                        src += "\n" + str(row) + " "+str(column)+"\n"
                    else:
                        src += "\n"
                except:
                    src = "Sorry \nmaximum - minimum < total unique number"
                    break
        else:

            for i in range(total_testcase):
                sub = []
                for j in range(row*column):
                    sub.append(random.randint(minimum, maximum))
                for j in range(row*column):
                    src += str(sub.pop(0))+" "
                    if((j+1) % column == 0):
                        src += "\n"

                if(i < total_testcase-1):
                    src += "\n" + str(row) + " "+str(column)+"\n"
                else:
                    src += "\n"

        return render(request, 'options/gen2d.html', {'data': src})
    return render(request, 'options/gen2d.html')


def bigint(request):
    if request.method == 'POST':
        try:
            a = int(request.POST['first'])
            operator = request.POST['inlineRadioOptions']
            src = str(a) + " "+operator
            res = 1
            if operator == '!':
                for i in range(1, a+1):
                    res *= i
            else:
                b = int(request.POST['second'])
                src += " "+str(b)+'\n'
                if operator == '+':
                    res = a+b
                elif operator == '-':
                    res = a-b
                elif operator == '*':
                    res = a*b
                elif operator == '/':
                    res = a/b
                elif operator == '%':
                    res = a % b
                else:
                    res = a**b
            src += "="+"\n"+str(res)

        except:
            src = "wrong datatype"

        return render(request, 'options/bigint.html', {'data': src})

    return render(request, 'options/bigint.html')


def tree(request):
    if request.method == 'POST':
        if 'wg' in request.POST:
            try:
                node = int(request.POST['node'])
                min = int(request.POST['min'])
                max = int(request.POST['max'])
                byd = int(random.randrange(1, node+1))
                cyd = byd+1 if (byd == 1) else byd-1
                already = [byd]
                remain = [cyd]
                for i in range(1, node+1):
                    if i != byd and i != cyd:
                        remain.append(i)

                src = str(node) + "\n"
                for i in range(node-1):
                    x = random.choice(already)
                    y = remain.pop(0)
                    already.append(y)
                    w = random.randrange(min, max+1)
                    src += str(x)+" "+str(y)+" "+str(w)+"\n"
            except:
                src = "sorry Wrong Input"
        else:

            try:
                node = int(request.POST['node'])
                byd = int(random.randrange(1, node+1))
                cyd = byd+1 if (byd == 1) else byd-1
                already = [byd]
                remain = [cyd]
                for i in range(1, node+1):
                    if i != byd and i != cyd:
                        remain.append(i)

                random.shuffle(remain)
                src = str(node) + "\n"
                for i in range(node-1):
                    x = random.choice(already)
                    y = remain.pop(0)
                    already.append(y)
                    src += str(x)+" "+str(y)+"\n"
                print("done")
            except:
                src = "sorry Wrong Input"
        return render(request, 'options/tree.html', {'data': src})

    return render(request, 'options/tree.html')


def graph(request):
    if request.method == 'POST':
        node = int(request.POST['node'])
        if node == 1:
            return render(request, 'options/graph.html', {'data': "1"})

        if 'wg' in request.POST:
            edge = 1 if node == 2 else random.randint(
                node, int(node * (node-1)/2))
            edge = 249750 if (edge > 249750) else edge
            min = int(request.POST['min'])
            max = int(request.POST['max'])
            already = set([1])
            remain = []
            for i in range(2, node+1):
                remain.append(i)
            random.shuffle(remain)
            noOfEdge = edge
            src = str(node) + " "+str(edge)+"\n"
            path = dict()
            path[1] = dict()
            while noOfEdge > 0:
                d = random.randint(0, 1)
                if d == 0 and len(remain) < 1:
                    if len(already) >= 2:
                        while(True):
                            x = random.choice(tuple(already))
                            y = random.choice(tuple(already))
                            if x != y:
                                if (x in path and y in path[x]) or (y in path and x in path[y]):
                                    continue
                                else:
                                    if x in path:
                                        path[x][y] = 1
                                    else:
                                        path[x] = dict()
                                        path[x][y] = 1
                                    src += str(x) + " "+str(y)+" " + \
                                        str(random.randint(min, max))+"\n"
                                    noOfEdge -= 1
                                    break
                else:
                    if len(remain) >= 1:
                        x = random.choice(tuple(already))
                        y = remain.pop()
                        already.add(y)
                        if x in path:
                            path[x][y] = 1
                        else:
                            path[x] = dict()
                            path[x][y] = 1
                        src += str(x) + " "+str(y)+" " + \
                            str(random.randint(min, max))+"\n"
                        noOfEdge -= 1
                    else:
                        while(True):
                            x = random.choice(tuple(already))
                            y = random.choice(tuple(already))
                            if x != y:
                                if (x in path and y in path[x]) or (y in path and x in path[y]):
                                    continue
                                else:
                                    if x in path:
                                        path[x][y] = 1
                                    else:
                                        path[x] = dict()
                                        path[x][y] = 1
                                    src += str(x) + " "+str(y)+" " + \
                                        str(random.randint(min, max))+"\n"
                                    noOfEdge -= 1
                                    break

            return render(request, 'options/graph.html', {'data': src})
        else:
            edge = 1 if node == 2 else random.randint(
                node, int(node * (node-1)/2))
            edge = 249750 if (edge > 249750) else edge
            already = set([1])
            remain = []
            for i in range(2, node+1):
                remain.append(i)
            random.shuffle(remain)
            noOfEdge = edge
            src = str(node) + " "+str(edge)+"\n"
            path = dict()
            path[1] = dict()
            while noOfEdge > 0:
                d = random.randint(0, 1)
                if d == 0 and len(remain) < 1:
                    if len(already) >= 2:
                        while(True):
                            x = random.choice(tuple(already))
                            y = random.choice(tuple(already))
                            if x != y:
                                if (x in path and y in path[x]) or (y in path and x in path[y]):
                                    continue
                                else:
                                    if x in path:
                                        path[x][y] = 1
                                    else:
                                        path[x] = dict()
                                        path[x][y] = 1
                                    src += str(x) + " "+str(y)+"\n"
                                    noOfEdge -= 1
                                    break
                else:
                    if len(remain) >= 1:
                        x = random.choice(tuple(already))
                        y = remain.pop()
                        already.add(y)
                        if x in path:
                            path[x][y] = 1
                        else:
                            path[x] = dict()
                            path[x][y] = 1
                        src += str(x) + " "+str(y)+"\n"
                        noOfEdge -= 1
                    else:
                        while(True):
                            x = random.choice(tuple(already))
                            y = random.choice(tuple(already))
                            if x != y:
                                if (x in path and y in path[x]) or (y in path and x in path[y]):
                                    continue
                                else:
                                    if x in path:
                                        path[x][y] = 1
                                    else:
                                        path[x] = dict()
                                        path[x][y] = 1
                                    src += str(x) + " "+str(y)+"\n"
                                    noOfEdge -= 1
                                    break

            return render(request, 'options/graph.html', {'data': src})

    return render(request, 'options/graph.html')


def string(request):
    if request.method == 'POST':
        try:
            total_testcase = int(request.POST['total_testcase'])
            single_testcase = int(request.POST['single_testcase'])
            Cset = str(request.POST['Cset'])
            flag = 0 if "hideItemNo" in request.POST else 1
            src = str(total_testcase)+"\n"

        except:
            return render(request, 'options/string.html', {'data': "something went wrong"})

        while(total_testcase):
            if flag:
                src += str(single_testcase)+"\n"

            temp = ""
            for i in range(len(Cset)):
                temp += Cset[i] * random.randint(1, int(single_testcase/2))
            while(len(temp) < single_testcase):
                temp += temp
            vs = list(temp)
            random.shuffle(vs)
            fstring = ''.join(vs)
            src += fstring[0:single_testcase] + "\n"
            total_testcase -= 1

        return render(request, 'options/string.html', {'data': src})
    return render(request, 'options/string.html')
