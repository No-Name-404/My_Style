# V7xStyle
#### There are 3 classes that you can work on
* [Animation](https://github.com/No-Name-404/V7xStyle/blob/master/README.md#animation-class)
* [Style](https://github.com/No-Name-404/V7xStyle/blob/master/README.md#style-class) 
* Text

Also, you can control the colors easily
* Colors


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
```python3
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

S = Style( *squares ).Square(Equal=False)
print (S)

S = Style( *squares ).Square(Equal=True)
print (S)
```
example 5...
```python3
from V7xStyle import Style

SQS = ['#','|','#','-','#','|','#','-']
SQ = ['text\ntext']*3
S = Style().Square(Square=SQS)
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
####  figlet
```python3
from V7xStyle import Text

Text('Hi').figlet
```
No values in this function
___
####  toilet
```python3
from V7xStyle import Text

Text('Hi').toilet
```
No values in this function
___
####  GetSpace
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
