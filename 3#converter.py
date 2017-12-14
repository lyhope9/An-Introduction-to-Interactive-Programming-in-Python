import simplegui

value=12.34
def convert_unit(val,name):
    result=str(val)+' '+name
    if val>1:
        result=result+'s'
    return result

def convert(val):
    dollars=int(val)
    cents=int(round(100*(val-dollars)))
    dollar_str=convert_unit(dollars,'dollar')
    cent_str=convert_unit(cents,'cent')
    if dollars==0 and cents==0:
        return 'broken'
    elif dollars==0:
        return cent_str
    elif cents==0:
        return dollar_str
    else:
        return dollar_str +' and '+ cent_str

       
    
    
def draw_handler(canvas):
    canvas.draw_text(convert(value),[50,120],24,'White')
    

def input_handler(inp):
    global value
    value=float(inp)
    
    
frame=simplegui.create_frame('converter',400,200)
frame.set_draw_handler(draw_handler)
frame.add_input('Enter value',input_handler,100)

frame.start()
    
    
