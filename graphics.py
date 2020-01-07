import time ,sys ,os
# color...
BL,Bl,R,G,Y,B,P,C,W = [
    '\033[0;30m', # black
    '\033[1;30m', # grey
    '\033[0;31m', # red
    '\033[0;32m', # green
    '\033[0;33m', # yellow
    '\033[0;34m', # blue
    '\033[0;35m', # purple
    '\033[0;36m', # cyan
    '\033[0;37m', # white
]
Color_C = []

class Color:
    def c(self,text):
        text = text.replace('Bl#',Bl)
        text = text.replace('R#',R)
        text = text.replace('G#',G)
        text = text.replace('Y#',Y)
        text = text.replace('B#',B)
        text = text.replace('P#',P)
        text = text.replace('C#',C)
        text = text.replace('W#',W)
        return text

    def remove_c(self,text):
        remove_c = [BL,Bl,R,G,Y,B,P,C,W]+Color_C
        for i in remove_c:
            text = text.replace(i,'')
        return text

class text:
    # figlet ...
    def figlet(self,text):
        os.system('figlet "%s"'%text)

    # toilet ...
    def toilet(self,text):
        os.system('toilet -f mono12 "%s"'%text)

    # to write text by index as slow motion
    def Incremental_Small_Text(self,text):
        for i in text:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.1)

    # to write text by line as slow motion
    def Incremental_Big_Text(self,text,Time=0.01):
        for i in range(0,len(text)):
            time.sleep(Time)
            print(text[i],end='')
        print('')

    def Measure_Sides_text(self,text):
        text = Color().remove_c(text)
        text = text.split('\n')
        top = 0
        right = 0
        down = 0
        width = 0

        # height
        temp2 = []
        height = []
        temp = False
        for i in text:
            if i == '' and temp is False:
                pass
            else:
                temp = True
                temp2.append(i)
        temp = False
        for i in temp2[::-1]:
            if i == '' and temp is False:
                pass
            else:
                temp = True
                height.append(i)

        check_up = []
        # to git the top
        for i in text:
            if i == '':
                top += 1
            else:
                break
        # to git the down
        for i in range(1,len(text)):
            i = int('-'+str(i))
            if text[i] == '':
                down += 1
            else:
                break
        # to git the right
        text = text[top:len(text)]
        text = text[0:len(text)-down]
        for i in text:
            if i == '':
                check_up.append(999) # if text is None it will take 999
            else:
                for space in i:
                    if space == ' ':
                        right += 1
                    else:
                        break
                check_up.append(right)
                right = 0
        right = sorted(check_up)[0]
        check_up.clear()
        # to git the width
        for i in text:
            for Width in i:
                width += 1
            check_up.append(width)
            width = 0
        width = sorted(check_up)[-1]-right
        check_up.clear()

        return [top,right,down,width,len(height)]

    # to add spaces in any text
    def Change_Sides_text(self,text,top,right,down):
        style = ''
        text = text.split('\n')
        # spaces top
        style = style+('\n'*top)
        # spaces right
        for i in text:
            style = style+(' '*right)+i+'\n'
        # spaces down
        style = style+'\n'*(down)

        return style[0:-2]

    def Delete_Spaces(self,text):
        sides = self.Measure_Sides_text(text)
        text = text.split('\n')
        style = ''
        check_up = 0
        # delete top spaces [\n]
        for i in range(sides[0]):
            text.remove(text[0])
        for i in text:
            if i == '':
                style += '\n'
                text.remove(text[0])
            else:
                break
        # delete right spaces
        for i in text:
            check_up = sides[1]
            for x in i:
                if check_up>0:
                    check_up -= 1
                else:
                    style += x
            style += '\n'
        check_up = 0
        # delete down spaces
        style = style[0:len(style)-sides[2]-1]
        return style

class style(text):
    def square(self,text,Square,Colors):
        Width = self.Measure_Sides_text(text)
        Width = Width[3]+Width[1]
        height = len(text.split('\n'))
        Sides = text.split('\n')
        style = ''
        style += Colors+Square[0]+Square[7]*Width+Square[6]
        for i in Sides:
            style += '\n'+Colors+Square[1]+W+i+' '*(Width-len(i))+Colors+Square[5]
        style += '\n'+Colors+Square[2]+Square[3]*Width+Square[4]

        return self.Delete_Spaces(style)

    def Mix_Squares_text(self,text,space):
        how_many_squars = len(text)
        style = ''
        check_up = []
        check_up_int = 0
        # to delete spaces and put evre square in list alone
        for txt in text:
            txt = self.Delete_Spaces(txt)
            txt = txt.split('\n')
            check_up.append(txt)
        # to put squares to gather and delete spaces...
        for i in range(0,len(check_up[0])):
            for Square in range(0,how_many_squars):
                style +=  check_up[Square][i]+' '*space
            style += '\n'
        style = self.Delete_Spaces(style)
        return self.delete_left_spase(style)

    def MultSquares(self,*text,Square=['┌','│','└','─','┘','│','┐','─'],space=1,padding_x=0,padding_y=0,Color=R,cols=False):
        Style = []
        xs = []
        STYLE = ''
        if not cols:
            cols = len(text)
        for i in text:
            Style.append(self.square(str( ('\n'*padding_y)+(' '*padding_x)+i+(' '*padding_x)+('\n'*padding_y)),Square,Color))
        cols = cols
        temp = 0
        for i in range(0,len(Style),cols):
            temp += cols
            xs.append(Style[i:temp])

        for i in xs:
            STYLE += self.Mix_Squares_text(i,space)+'\n'

        return STYLE[0:-1]

    def text_In_The_Middle(self,*args):
        style = ''
        temp = [text().Measure_Sides_text(i)[3] for i in args]
        temp2 = sorted(temp)[-1]
        bigest = text().Measure_Sides_text(args[temp.index(temp2)])

        for i in args:
            i += ' '
            width = text().Measure_Sides_text(i)[3]
            right = text().Measure_Sides_text(i)[1]
            style += text().Change_Sides_text(i,0,(((temp2+1)//2)-(width//2)),0)+'\n'

        return style[0:-1]

    def delete_left_spase(self,text):
        text_x = ''
        text_y = ''
        style = ''
        for i in text.split('\n'):
            text_x += i[::-1]+'\n'
        text_x = text_x[0:-1]
        sides = self.Measure_Sides_text(text_x)
        check_up = 0
        for i in text_x.split('\n'):
            check_up = sides[1]
            for x in i:
                if check_up>0:
                    check_up -= 1
                else:
                    style += x
            style += '\n'

        for i in style[0:-1].split('\n'):
            text_y += i[::-1]+'\n'

        return text_y[0:-1]

class animation:
    def A(self,color_text,color_TEXT,t,Num=' [A1]',color_Num=W,text=' python for ever ',Range=2):
        print(color_Num+Num+color_text+text,end='\r')
        for i in range(Range):
            for i in range(0,len(text)):
                print(color_Num+Num+color_text+text[:i].lower()+color_TEXT+text[i].upper(),end='\r')
                time.sleep(t)
        print('')

    # Loading animation...
    def B(self,Animation,Num=' [B1]',t=0.1,Range=10):
        for i in range(Range):
            for i in range(0,len(Animation)):
                print(W+Num+Animation[i],end='\r')
                time.sleep(t)
        print('')

    # Downloading animation...
    # Animation and colors should be list
    def C(self,Animation,Colors,Num='',t=0.1,width=25):
        y = width+1
        for i in range(width+1):
            print('\r'+W+Num+
            Colors[0]+Animation[0]+
            Colors[1]+(i)*Animation[1]+
            Colors[2]+Animation[2]*(y-1)+
            Colors[3]+Animation[3]+
            ' ',end='')
            time.sleep(t)
            y -= 1
        print('')

class Text:
    def __init__(self,text):
        self.text = Color().c(text)

    def __str__(self):
        return str(self.text)

    @property
    def figlet(self):
        text().figlet(self.text)

    @property
    def toilet(self):
        text().toilet(self.text)

    @property
    def GetSpace(self):
        size = text().Measure_Sides_text(self.text)
        return {
                'top':size[0],
                'right':size[1],
                'bottom':size[2],
                'width':size[3],
                'height':size[4]
                }

    def ChangeLocation(self,top=0,right=0,bottom=0,DeleteSpace=False):
        text_ = self.text
        if DeleteSpace:
            text_ = text().Delete_Spaces(self.text)
        return text().Change_Sides_text(text_,top,right,bottom+1)

    @property
    def DeleteSpace(self):
        return text().Delete_Spaces(self.text)


class Style():
    def __init__(self,*args):
        super(Style,self).__init__()
        self.args = [Color().c(i) for i in args]

    # Square Equal...
    def Equal(self,*text):
        tmp = []
        for Int,Str in enumerate(text):
            tmp += [f'{Str}']
        text = tmp
        tmp = []
        for i in text:
            tmp += [len(Color().remove_c(i))]
        Len = sorted(tmp)[-1]
        tmp = []
        for i in text:
            i = f"{' '*((Len-len(Color().remove_c(i)))//2)}{i}"
            tmp += [f'{i}{" "*(Len-len(Color().remove_c(i)))}']
        text = tmp
        return text

    Square_Style = False
    def Square(self,Square=['╔','║','╚','═','╝','║','╗','═'],padding_x=0,padding_y=0,Space=0,Color=R,Equal=True,cols=False):
        if Equal:
            self.args = self.Equal(*self.args)
        return style().MultSquares(*self.args,Square=Square,padding_x=padding_x,padding_y=padding_y,space=Space,Color=Color,cols=cols)

    # put text in the middle...
    @property
    def Center(self):
        return style().text_In_The_Middle(*self.args)

class Animation:
    @classmethod
    def SlowLine(self,Text,time=0.001):
        text().Incremental_Big_Text(Text,Time=time)

    @classmethod
    def SlowText(self,Text,end=False):
        text().Incremental_Small_Text(Text)
        if not end:
            print('')

    def Loading(Animation=['/','-','\\','|'],text='',time=0.1,repeat=10):
        return animation().B(Animation,Num=Color().c(text),t=time,Range=repeat)

    def Downloading(Animation=['│','█','▒','│'],Colors=[W,G,W,W],text='Loading',time=0.2,width=25):
        return animation().C(Animation,Colors,Num=Color().c(text),t=time,width=width)

    def Text(UpperTextColor=R,LowerTextColor=W,Animation=False,text='',time=0.2,repeat=2):
        if Animation:
            return animation().A(LowerTextColor,UpperTextColor,time,Num=Color().c(text),color_Num=W,text=Animation+' ',Range=repeat)
        else:
            return None
