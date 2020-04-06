from My_Style import Style,Text,Color,Animation
from My_Style.Library import ProFunctions
Color.Theme('dark')

tools = [
'-TREMUX TOOLS',      '-LINUX ON ANDROID',
'-DOS,DDOS ATTACK',   'INFO GATHRING',
'-SCAN--EVERYTHING',  '-SOCIAL ENGNEER',
'-V7X [MeTaSpLoIt]',  '-HASH AnyThing',
'-INFO  ABOUT US',    '-EXIT THE  V7X',
]
tools = [f'Y#{name} C#[R#{num+1}C#]'
        for num ,name in enumerate(tools)]
tools = ProFunctions().Equal(*tools)

def my_square(index,text):
    return Style(*tools[index:index+2]).Square(
    Square=['╔','╢','╚','═','╝','╟','╗','═'],
    cols=2,
    space=9,
    padding_y=2,
    padding_x=1,
    ).replace('══',text)

def my_tool():
    S = ''
    text = lambda x,y,z:(f'\n{x}|-|-|-|-|-|-|-|-|-|-|{y}V7X-Team{z}|-|-|-|-|-|-|-|-|-|-|\n')
    temp = True
    for i in range(0,len(tools),2):
        if temp:
            S += my_square(i,'╧╤')+text('  ','- ',' - ')
            temp = False
        else:
            S += my_square(i,'╤╧')+text(' ',' - ',' -')
            temp = True
    return (S[0:-len(text('','',''))-7]).replace(
    Color.reader(' R#╟         R#╢'),
    Color.reader(' R#╟--[Y#V7xR#]--╢'))

# my style...
Intro = Text('VAIROUS7X').Figlet()+'\n'
tools = my_tool()
end = Style('Y#REPAIR PROBLEMS - REPAIR TERMUX C#[R#11C#]')
end = end.Square(
Square=['╔','╢','╚','═','╝','╟','╗','═'],
padding_y=1,
padding_x=1,
).replace('══','╤╧')

my_style = Style(Intro,tools,end).Center()
Animation.SlowLine(my_style,t=0.05)
