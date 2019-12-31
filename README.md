# Graphics
All function in class Text...XXX
[
test = '\n\n\ntext\ntext\ntext\ntext\n\n\n'
print( Text(test) )

{figlet}:
Text('text').figlet

{toilet}:
Text('text').toilet

{SlowText}:(end)
Text('text').SlowText()

{SlowLine}:(time)>
Text(test).SlowLine()

{GetSpace}:
print( Text(test).GetSpace )

{DeleteSpace}:
print( Text(test).DeleteSpace )

{ChangeLocation}:(bottom,top,right,DeleteSpace)>
print( Text(test).ChangeLocation(bottom=0,right=2,top=1,DeleteSpace=True) )
]

All function in class Style...XXX
[
{Square}:(Square, padding_x, padding_y, Space,Color,Equal)>
Style('example','example').Square()

{Center}:
Style('title1','tool tool tool tool tool','exit').Center
]

All function in class Animation...XXX
[
{Loading}:(Animation,text,time,repeat)>
Animation.Loading()

{Downloading}:(Animation,Color,text,time,width)>
Animation.Downloading()

{Text}:(Animation,text,time,UpperTextColor,LowerTextColor,repeat)>
Animation.Text(Animation='Loading...',text='v7x',repeat=5)
]
