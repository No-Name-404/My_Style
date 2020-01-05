from V7xStyle import Text

text = '''
example...
We use cookies and other tracking
technologies to improve your brow
sing experience on our site, show
personalized content and targeted
ads, analyze site traffic, and un
derstand where our audiences come
'''

# example 1
T = Text( text ).GetSpace
print (T)

# example 2
Text( 'example' ).figlet

# example 3
Text( 'example' ).toilet

# example 4
T = Text( text ).DeleteSpace
print (T)

# example 5
T = Text( text ).ChangeLocation(top=0,
                                right=10,
                                bottom=0,
                                DeleteSpace=False)
print (T)

#===================================#
from V7xStyle import Style

# example 1
a = '12345'
b = '123'
c = '1'

S = Style( a,b,c ).Center
print (S)

# example 2
squares = ['A1','B22','C333']
S = Style( *squares ).Square()
print (S)
#---------
S = Style( *squares ).Square(padding_x=5)
print (S)
#---------
S = Style( *squares ).Square(padding_y=3)
print (S)
#---------
S = Style( *squares ).Square(Equal=False)
print (S)
S = Style( *squares ).Square(Equal=True)
print (S)
#---------
S = Style( *squares ).Square(Color='\033[0;33m')
print (S)
#or
from V7xStyle import (R,G,W,B,P,C,Bl,Y)
S = Style( *squares ).Square(Color=Y)
print (S)
#---------
S = Style( *squares ).Square(Space=2)
print (S)
#---------
SQ = ['╔','|','╚','-','╝','|','╗','-']
S = Style( *squares ).Square(Square=SQ)
print (S)
#---------
squares = ['tools']*20
S = Style( *squares ).Square(cols=4)
print (S)

#===================================#
from V7xStyle import Animation

# example 1
Animation.Loading( text=' Hi ' )
#---------
AQ = [ str(i+1) for i in range(100) ]
Animation.Loading( text=' Hi %',Animation=AQ,repeat=1 )
#---------
AQ = ['V','7','x']
Animation.Loading( text=' V7x-|',
                   Animation=AQ,
                   repeat=10,
                   time=0.5 )
# example 2
from V7xStyle import (R,G,W,B,P,C,Bl,Y)
Animation.Text( UpperTextColor=R,
                LowerTextColor=W,
                Animation='texttttt',
                text=' My- ',
                time=0.2,
                repeat=2 )
# example 3
Animation.Downloading( Animation=['|','█','▒','|'],
                       Colors=[W,G,W,W],
                       text='Loading',
                       time=0.2,
                       width=25 )
#---------
Animation.Downloading()

# example 4
Animation.SlowLine( text,time=0.001 )

# example 5
Animation.SlowText( text,end=False )
