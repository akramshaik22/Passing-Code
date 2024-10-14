'''
   Code by Akram
'''

from tkinter import*
from tkinter import ttk
import subprocess
import os
from zipfile import ZipFile
import shutil
import time


location = os.getcwd()
loc = location + '\\data\\'
jn = 'JntuNo'
nm = 'name'
yr = 'year'
sec = 'section'

que_time = {1: 525, 2: 525, 3: 525, 4: 775, 5: 775, 6: 1025, 7: 1}
# que_time = {1: 1, 2: 1, 3: 1, 4: 1, 5: 250, 6: 1, 7: 250, 8: 250, 9: 250, 10: 250}
que_tc = {1: 5, 2: 5, 3: 5, 4: 5, 5: 5, 6: 5, 7: 5}
que_sc = {1: 2, 2: 2, 3: 2, 4: 4, 5: 4, 6: 6, 7: 0}
que_score = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0}
timer = que_time[1]
last_que = 6

os.chdir('data')
subprocess.run('QRes.exe /x 1280 /y 720', shell=False)
os.chdir('..')
subprocess.call('cls', shell=True)


def self_destruct():
    os.chdir('data')
    subprocess.run('QRes.exe /x 1920 /y 1080', shell=True)
    os.chdir('..')

    save_score()

    # shutil.rmtree(location, ignore_errors=True)

    win.wm_forget(win)


win = Tk()
win.title("Passing Code")
win.geometry('1280x720')

c1, c2 = 1, 2
q = c1

compile_Lang = 4
program_File = "PyProgram.py"
compileResult1 = ''
compileResult2 = ''
compileInput1 = ''
compileInput2 = ''
lang_dict = {'C': 1, 'C++': 2, 'Java': 3, 'Python': 4}
selc = StringVar()

img = PhotoImage(file=location+"\\data\\0.png")
can = Canvas(win, width=1280, height=700)
can.place(x=0, y=0)
can.create_image(0, 0, image=img, anchor='nw')


def selc_lang(arg):
    global compile_Lang, program_File
    compile_Lang = lang_dict[selc.get()]
    if compile_Lang == 1:
        program_File = "CProgram.c"
    elif compile_Lang == 2:
        program_File = "CppProgram.cpp"
    elif compile_Lang == 3:
        program_File = "JavaProgram.java"
    else:
        program_File = "PyProgram.py"


frame1 = Frame(win, width=900, height=500, bg='skyblue')
x1, y1 = 590, 125

l1 = Text(frame1, font=('calibri', 14), bd=8, relief='groove', width=34, height=21, bg='#9d8692')
l1.place(x=0, y=0)

t1 = Text(frame1, font=('Calibri', 14), width=53, height=14, bd=7, relief='groove', bg='#7a888e')
t1.place(x=354, y=0)

l11 = Text(frame1, font=('Calibri', 13), width=59, height=7, bd=7, relief='groove', bg='#c6846d')
l11.place(x=354, y=337)

runButton1 = Button(frame1, text="Compile \n& Run", font=('Calibri', 9, 'bold'), width=8, height=2, activebackground='cyan', bd=4, relief='groove', bg='skyblue', command=lambda: run(1))
runButton1.place(x=760, y=340)

runTest1 = Button(frame1, text=" Run \nTest Cases", font=('Calibri', 9, 'bold'), width=8, height=2, activebackground='cyan', bd=4, relief='groove', bg='skyblue', command=lambda: runTestCases())
runTest1.place(x=825, y=340)

langSelc1 = ttk.Combobox(frame1, width=10, textvariable=selc, state='readonly')
langSelc1['values'] = (['C', 'Java', 'Python'])
langSelc1.current(2)
langSelc1.place(x=260, y=10)
langSelc1.bind('<<ComboboxSelected>>', selc_lang)

sub_code1 = Button(frame1, text="Submit", font=('Calibri', 12, 'bold'), width=6, height=1, activebackground='cyan', bd=4, relief='groove', bg='skyblue', command=lambda: submit_code())
sub_code1.place(x=825, y=390)

frame2 = Frame(win, width=900, height=500, bg='skyblue')
x2, y2 = 1300, 125

l2 = Text(frame2, font=('calibri', 14), bd=8, relief='groove', width=34, height=21, bg='#9d8692')
l2.place(x=0, y=0)

t2 = Text(frame2, font=('Calibri', 14), width=53, height=14, bd=7, relief='groove', bg='#7a888e')
t2.place(x=354, y=0)

l22 = Text(frame2, font=('Calibri', 13), width=59, height=7, bd=7, relief='groove', bg='#c6846d')
l22.place(x=354, y=337)

runButton2 = Button(frame2, text="Compile \n& Run", font=('Calibri', 9, 'bold'), width=8, height=2, activebackground='cyan', bd=4, relief='groove', bg='skyblue', command=lambda: run(2))
runButton2.place(x=760, y=340)

runTest2 = Button(frame2, text=" Run \nTest Cases", font=('Calibri', 9, 'bold'), width=8, height=2, activebackground='cyan', bd=4, relief='groove', bg='skyblue', command=lambda: runTestCases())
runTest2.place(x=825, y=340)

langSelc2 = ttk.Combobox(frame2, width=10, textvariable=selc, state='readonly')
langSelc2['values'] = (['C', 'Java', 'Python'])
langSelc2.current(2)
langSelc2.place(x=260, y=10)
langSelc2.bind('<<ComboboxSelected>>', selc_lang)

sub_code2 = Button(frame2, text="Submit", font=('Calibri', 12, 'bold'), width=6, height=1, activebackground='cyan', bd=4, relief='groove', bg='skyblue', command=lambda: submit_code())
sub_code2.place(x=825, y=390)

selc1 = StringVar()
selc2 = StringVar()

frame3 = Frame(win, width=400, height=340, bg='#f2a904', bd=8, relief='groove')
frame3.place(x=440, y=180)

img3 = PhotoImage(file=location+"\\data\\1.png")
can3 = Canvas(frame3, width=400, height=340)
can3.place(x=0, y=0)
can3.create_image(0, 0, image=img3, anchor='nw')

tb1 = Text(frame3, font=('Calibri', 14),width=17, height=1)
tb1.place(x=195,y=60)

tb2 = Text(frame3, font=('Calibri', 14),width=17, height=1)
tb2.place(x=195, y=100)

cb1 = ttk.Combobox(frame3, width=15, font=('calibri', 14), textvariable=selc1, state='readonly')
cb1['values'] = ('1', '2', '3', '4')
cb1.place(x=195, y=140)

cb2 = ttk.Combobox(frame3, width=15, font=('calibri', 14), textvariable=selc2, state='readonly')
cb2['values'] = ('AIML', 'AIDS', 'CSE - A', 'CSE - B', 'CSE - C', 'IT - A', 'IT - B')
cb2.place(x=195, y=180)

l35 = Label(frame3,text='!! Enter Correct Details !!', font=('calibri', 14, 'bold'), bg='red')

submitButton = Button(frame3, text='Submit', font=('calibri', 14, 'bold'), bg='cyan', width=6, height=1, command=lambda: submit())
submitButton.place(x=155, y=220)

startButton = Button(frame3, text='Start', font=('calibri', 14, 'bold'), bg='#00c2cb', width=6, height=1, command=lambda: start())
# startButton.place(x=155, y=272)

frame4 = Frame(win, width=900, height=500, bg='#6e6387')
# frame4.place(x=190,y=125)
final_submit = Button(frame4, text='Submit', font=('calibri', 14, 'bold'), bg='cyan', width=6, height=1, command=lambda: self_destruct())
final_submit.place(x=420, y=400)
lb = Label(frame4, font=('calibri', 32), text='** Thanks for Participating in Our Event ** \n \n *Click on Submit Button to Submit Your Answers*', bg='#6e6387')
lb.place(x=2, y=150)


def submit():
    global jn, nm, yr, sec
    jn = rem_n(tb1.get(1.0, END))
    nm = rem_n(tb2.get(1.0, END))
    yr = selc1.get()
    sec = selc2.get()
    if len(jn) == 10 and len(nm) > 3 and yr and sec:
        l35.place_forget()
        startButton.place(x=155, y=272)
    else:
        startButton.place_forget()
        l35.place(x=95, y=280)


def start():
    # startButton.place_forget()
    frame3.place_forget()
    frame1.place(x=350, y=125)
    frame2.place(x=1400, y=125)
    move()


def move():
    global x1, x2, c1, c2, timer, q
    if x1 >= -920 and c1 == 1:
        x1 -= 1
        frame1.place_configure(x=x1)

    if (x2 < -200 or x1<920) and 1<c1<=last_que-1:
        x1 -= 1
        frame1.place_configure(x=x1)

    if (x1 < -200 or x2<920) and c2 <= last_que:
        x2 -= 1
        frame2.place_configure(x=x2)

    if x1 <= -920:
        q = c2
        timer = que_time[q]
        x1 = 1300
        c1 += 2
        load(1, c1) if c1 <= last_que-1 else None

    if x2 <= -920:
        q = c1
        timer = que_time[q]
        x2 = 1300
        c2 += 2
        load(2, c2) if c2 <= last_que else None

    if c2 > last_que:
        frame4.place(x=190, y=125)
        # self_destruct()

    win.after(timer, move) if c2 <= last_que else None


def load(fr, q):
    global compileResult1, compileResult2, compileInput1, compileInput2
    qu = str(q) + '.txt'
    inp = str(q) + 'in0' + '.txt'
    outp = str(q) + 'out0' + '.txt'

    f1 = open(loc + qu, 'r')
    f2 = open(loc + inp, 'r')
    f3 = open(loc + outp, 'r')

    que = f1.read()
    inpt = f2.read()
    outpt = ''

    for i in f3.read().split('\n'):
        outpt += rem_n(i) + '\n'

    f1.close()
    f2.close()
    f3.close()

    if fr == 1:
        qt, t, ot = l1, t1, l11
        compileResult1 = outpt
        compileInput1 = inpt
    else:
        qt, t, ot = l2, t2, l22
        compileResult2 = outpt
        compileInput2 = inpt

    qt.configure(state='normal')
    qt.replace(1.0, END, chars='')
    qt.insert(INSERT, que)
    qt.configure(state='disabled')
    t.replace(1.0, END, chars='')
    ot.configure(state='normal')
    ot.replace(1.0, END, chars='')
    ot.insert(END, 'Sample Input: \n' + inpt + '\nSample Output:\n' + outpt)
    ot.configure(state='disabled')


def compile(inpt):
    try:
        if compile_Lang == 1:
            p = subprocess.Popen([loc + "c_c\\bin\\./gcc.exe", "CProgram.c", "-o", "C_out"], stderr=subprocess.PIPE,
                                 stdout=subprocess.PIPE, text=True, shell=True)
            p.stdout, p.stderr = p.communicate()
            if p.stderr:
                return p.stderr
            p = subprocess.run("./C_out.exe", stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True, input=inpt, timeout=1)

        elif compile_Lang == 2:
            p = subprocess.Popen([loc + "j_c\\bin\\./javac.exe", "JavaProgram.java"], stderr=subprocess.PIPE,
                                 stdout=subprocess.PIPE, text=True, shell=True)
            p.stdout, p.stderr = p.communicate()
            if p.stderr:
                return p.stderr
            p = subprocess.run("./Cpp_out.exe", stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True, input=inpt, timeout=1)

        elif compile_Lang == 3:
            p = subprocess.Popen([loc + "j_c\\bin\\./javac.exe", "JavaProgram.java"], stderr=subprocess.PIPE,
                                 stdout=subprocess.PIPE, text=True, shell=True)
            p.stdout, p.stderr = p.communicate()
            if p.stderr:
                return p.stderr
            p = subprocess.run(["java", "JavaProgram"], stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True, input=inpt, timeout=1)

        else:
            p = subprocess.run(["python", "PyProgram.py"], text=True, input=inpt, timeout=1, stderr=subprocess.PIPE, stdout=subprocess.PIPE)

    except subprocess.TimeoutExpired:
        return "TimeLimitExceeded(TLE)"

    if p.stderr:
        return p.stderr

    return p.stdout


def run(td):
    file = open(program_File, "w")
    if td == 1:
        file.write(t1.get(1.0, END))
        result = compileResult1
        inpt = compileInput1
        ot = l11
    else:
        file.write(t2.get(1.0, END))
        result = compileResult2
        inpt = compileInput2
        ot = l22
    file.close()
    otput = compile(inpt)
    output = ''
    for i in otput.split('\n'):
        output += rem_n(i) + '\n'
    ans = 'Correct Answer\n' if rem_n(output) == rem_n(result) else 'Wrong Answer\n'

    ot.configure(state='normal')
    ot.replace(1.0, END, chars='')
    ot.insert(INSERT, ans + 'Sample Input: \n' + inpt + '\nSample Output:\n' + result + '\nYour Output : \n' + output)
    ot.configure(state='disabled')


def runTestCases():
    tc = que_tc[q]
    file = open(program_File, "w")
    if q % 2 != 0:
        file.write(t1.get(1.0, END))
        ot = l11
    else:
        file.write(t2.get(1.0, END))
        ot = l22
    file.close()
    ot.configure(state='normal')
    ot.replace(1.0, END, chars='')
    score = 0
    for i in range(tc):
        test = str(q) + 'in' + str(i) + '.txt'
        reslt = str(q) + 'out' + str(i) + '.txt'
        f2 = open(loc + test, 'r')
        f3 = open(loc + reslt, 'r')
        inpt = f2.read()
        outpt = ''
        for j in f3.read().split('\n'):
            outpt += rem_n(j) + '\n'
        f2.close()
        f3.close()
        otput = compile(inpt)
        output = ''
        for j in otput.split('\n'):
            output += rem_n(j) + '\n'
        score += que_sc[q] if rem_n(output) == rem_n(outpt) else 0
        ans = ' : Correct Answer\n' if rem_n(output) == rem_n(outpt) else ' : Wrong Answer\n'
        if otput == "TimeLimitExceeded(TLE)":
            ans = " : TimeLimitExceeded(TLE)\n"
        ot.insert(END, 'Test Case - ' + str(i) + ans)

    update_score(q, score)
    ot.configure(state='disabled')


def submit_code():
    global timer
    timer = 2


def update_score(q, score):
    if score > que_score[q]:
        que_score[q] = score


def total_score():
    total = 0
    for i in que_score:
        total += que_score[i]

    return total


def save_score():
    os.chdir('..')
    loc = os.getcwd()
    file = open(loc + '\\' + jn, 'w')
    file.write(score_enc(total_score()))
    file.write(score_enc('\n' + jn + '\n' + nm + '\n' + yr + '\n' + sec + '\n' + time.ctime()))
    file.close()


def score_enc(score):
    enc = ''
    sc = str(score)
    for i in sc:
        enc += '0x' + str(ord(i))

    return enc


def que_extract(data):
    file = open(loc+data, 'r')
    data = file.readline()

    cnt = 1
    f = open(loc + str(cnt) + '.txt', 'w')
    while data:
        if data == '  Question - ' + str(cnt + 1) + ':\n':
            f.close()
            cnt += 1
            f = open(loc + str(cnt) + '.txt', 'w')

        f.write(data)
        data = file.readline()

    f.close()
    file.close()


def i_o_extract(data, typ):
    file = open(loc + data, 'r')
    data = file.readline()
    q = 1
    tc = 1
    f = open(loc + str(1) + typ + str(0) + '.txt', 'w')
    while data:
        data = file.readline()
        if data == str(q) + typ + str(tc) + '\n':
            f.close()
            f = open(loc + str(q) + typ + str(tc) + '.txt', 'w')
            data = file.readline()
            tc += 1

        f.write(data)

        if tc >= que_tc[q]:
            q += 1
            tc = 0
    f.close()
    file.close()


def compiler_extract(com):
    with ZipFile(loc + com, 'r') as zObject:
        zObject.extractall(path=location + "\\data")


def decrypt_data(f):
    with open(loc+'enc_'+f,'r') as file:
        enc = file.read()
        dec = ''
        for i in enc[2:].split('0x'):
            dec += chr(int(i))

    with open(loc + 'dec_'+f, 'w') as file:
        file.write(dec)


def rem_n(s):
    ln = len(s)
    c = 0
    for i in s[ln::-1]:
        if i not in ['\n', '\t', ' ']:
            break
        c += 1
    return s[:ln-c]


if (c1, c2) == (1, 2):
    decrypt_data('0.txt')
    decrypt_data('0in.txt')
    decrypt_data('0out.txt')

    que_extract('dec_0.txt')
    i_o_extract('dec_0in.txt', 'in')
    i_o_extract('dec_0out.txt', 'out')

    compiler_extract('c_c.zip')
    compiler_extract('j_c.zip')
    load(1, 1)
    load(2, 2)


win.mainloop()

self_destruct()

