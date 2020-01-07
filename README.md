# V7xStyle
Input...
```python3
from V7xStyle import Style,Animation,Text

title = Style('My Tool B#{C#2.10B#}')
title = title.Square(padding_x=20)

tools = ['tools']*30
tools = [f'[{N+1}] G#{T}' for N,T in enumerate(tools)]
tools = Style(*tools)
tools = tools.Square(cols=3,padding_x=2,Space=2)

end = Style('Y#Exit').Square(padding_x=25)

MyStyle = [title,tools,end]
MyStyle = Style(*MyStyle).Center

print (MyStyle)
```
Output...
![Screenshot_٢٠٢٠٠١٠٦_٢٣٥٧٤٧](https://user-images.githubusercontent.com/56244233/71855293-ecb03580-30e0-11ea-998d-b953375514ba.jpg)
#### There are 3 classes that you can work on
* [Animation](https://github.com/No-Name-404/V7xStyle/blob/master/README.md#animation-class)
  * [SlowLine](https://github.com/No-Name-404/V7xStyle/blob/master/README.md#slowline-function)
  * [SlowText](https://github.com/No-Name-404/V7xStyle/blob/master/README.md#slowtext-function)
  * [Loading](https://github.com/No-Name-404/V7xStyle/blob/master/README.md#loading-function)
  * [Text](https://github.com/No-Name-404/V7xStyle/blob/master/README.md#text-function)
  * [Downloading](https://github.com/No-Name-404/V7xStyle/blob/master/README.md#downloading-function)
* [Style](https://github.com/No-Name-404/V7xStyle/blob/master/README.md#style-class)
  * [Center](https://github.com/No-Name-404/V7xStyle/blob/master/README.md#center-function)
  * [Square](https://github.com/No-Name-404/V7xStyle/blob/master/README.md#square-function)
* [Text](https://github.com/No-Name-404/V7xStyle/blob/master/README.md#text-class)
  * [figlet](https://github.com/No-Name-404/V7xStyle/blob/master/README.md#figlet-function)
  * [toilet](https://github.com/No-Name-404/V7xStyle/blob/master/README.md#toilet-function)
  * [GetSpace](https://github.com/No-Name-404/V7xStyle/blob/master/README.md#getspace-function)
  * [ChangeLocation](https://github.com/No-Name-404/V7xStyle/blob/master/README.md#changelocation-function)
  * [DeleteSpace](https://github.com/No-Name-404/V7xStyle/blob/master/README.md#deletespace-function)

Also, you can control the colors easily
* [Colors](https://github.com/No-Name-404/V7xStyle/blob/master/README.md#colors)


# The method of work
## Animation class
####  SlowLine function
```python3
from V7xStyle import Animation
text = '''
text text text text text text
text text text text text text
text text text text text text
text text text text text text
text text text text text text
text text text text text text
'''
Animation.SlowLine(text, time=0.001)
```
Only 2 values in this function
__________________________
####  SlowText function
```python3
from V7xStyle import Animation
text = 'text text text text text text'

Animation.SlowText(text, end=False)
```
Only 2 values in this function
__________________________
####  Loading function

example 1...
```python3
from V7xStyle import Animation

Animation.Loading( text=' text ' )
```
example 2...
```python3
from V7xStyle import Animation

AQ = [ str(i+1) for i in range(100) ]
Animation.Loading(text=' Hi %',
                  Animation=AQ,
                  repeat=1)
```
example 3...
```python3
from V7xStyle import Animation

AQ = ['a','b','c']
Animation.Loading( text=' text - ',
                   Animation=AQ,
                   repeat=10,
                   time=0.5 )
```
Only 4 values in this function
__________________________
####  Text function
```python3
from V7xStyle import Animation
from V7xStyle import (R,G,W,B,P,C,Bl,Y)

Animation.Text( UpperTextColor=R,
                LowerTextColor=W,
                Animation='text.text...',
                text=' My text- ',
                time=0.2,
                repeat=2 )
```
Only 6 values in this function
__________________________
####  Downloading function

example 1...
```python3
from V7xStyle import Animation

Animation.Downloading()
```
example 2...
```python3
from V7xStyle import Animation
from V7xStyle import (R,G,W,B,P,C,Bl,Y)

AQ = ['|','█','▒','|']
CQ = [W,G,W,W]
Animation.Downloading( Animation=AQ,
                       Colors=CQ,
                       text='Loading',
                       time=0.2,
                       width=25 )
```
Only 5 values in this function

___
## Style class
#### Center function
```python3
from V7xStyle import Style

a = '12345'
b = '123'
c = '1'

S = Style( a,b,c ).Center
print (S)
```
No values in this function
___
####  Square function
example 1...
```python3
from V7xStyle import Style

S = Style('text').Square()
print(S)
```
example 2...
```python3
from V7xStyle import Style

S = Style('A','B','C').Square()
print(S)

SQ = ['text']*10
S = Style(*SQ).Square()
print(S)
```
example 3...
```python3
from V7xStyle import Style
from V7xStyle import (R,G,W,B,P,C,Bl,Y)

SQ = ['B#A','P#B','R#C']
S = Style(*SQ).Square(Color=G,
                      padding_x=5,
                      padding_y=2)
print(S)
```
example 4...
```python3
from V7xStyle import Style

SQ = ['A1','B22','C333']
S = Style( *SQ ).Square(Equal=False)
print (S)

S = Style( *SQ ).Square(Equal=True)
print (S)
```
example 5...
```python3
from V7xStyle import Style

SQS = ['#','|','#','-','#','|','#','-']
SQ = ['text\ntext']*3
S = Style(*SQ).Square(Square=SQS)
print (S)
```
example 6...
```python3
from V7xStyle import Style

S = Style('A','B','C').Square(Space=4)
print (S)
```
example 7...
```python3
from V7xStyle import Style

SQ = ['text']*9
S = Style( *SQ ).Square(cols=False)
print (S)

S = Style( *SQ ).Square(cols=3)
print ('\n\n\n'+S)
```
Only 7 values in this function
___
## Text class
####  figlet function

before use this function you must install figlet...

Install in kali:`sudo apt-get install figlet`

Install in termux:`pkg install figlet`

example...
```python3
from V7xStyle import Text

Text('Hi').figlet
```
No values in this function
___
####  toilet function

before use this function you must install toilet...

Install in kali:`sudo apt-get install toilet`

Install in termux:`pkg install toilet`

example...
```python3
from V7xStyle import Text

Text('Hi').toilet
```
No values in this function
___
####  GetSpace function
This function gives you Space text for example...

`\ntext\n`

the function will give this results..
```python3
{
'top':1,
'right':0,
'bottom':1,
'width':4,
'height':1               
}
```
example 1...
```python3
from V7xStyle import Text

T = '''text
text
text'''
Space = Text(T).GetSpace
print(Space)
```
example 2...
```python3
from V7xStyle import Text

T = '''
 text
text
 textt
'''
Space = Text(T).GetSpace
print(Space)
```
example 3...
```python3
from V7xStyle import Text

T = '''
 text
  text
 text
'''
Space = Text(T).GetSpace
print(Space)
```
No values in this function
___
#### ChangeLocation function
```python3
from V7xStyle import Text

T = '''
AAAAA
AAAAA
AAAAA
'''

T = Text(T).ChangeLocation(top=0,
                           right=5,
                           bottom=0,
                           DeleteSpace=True)
print(T)
```
Only 4 values in this function
___
#### DeleteSpace function
```python3
from V7xStyle import Text

T = '\n    t e x t\n\n'
T = Text(T).DeleteSpace
print(T)
```
No values in this function
___
# Colors

There are 9 primary colors in the library...
```python3
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
```
You can import it this way...
```python3
from V7xStyle import (BL,R,G,W,B,P,C,Bl,Y)
```
How to use colors?
example 1...
```python3
from V7xStyle import (BL,R,G,W,B,P,C,Bl,Y)
print (R+'Hi')

# or
from V7xStyle import Text
print ( Text('R#Hi') )
print ( Text('G#Hi') )
print ( Text('B#Hi') )
print ( Text('P#Hi') )
```
example 2...
if you want to add a new color...
```python3
from V7xStyle import Style
import V7xStyle

V7xStyle.graphics.Color_C += ['\003[88m']
S = Style('text').Square(color='\003[88m')
print(S)
```
