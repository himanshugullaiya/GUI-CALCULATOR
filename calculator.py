from tkinter import *

root = Tk()

root.title("Calculator")
operator = ""
txt_input = StringVar()

buttons = []

def buttonclick(no):
	global operator
	operator = operator + str(no)
	txt_input.set(operator)

def cleardisplay():
	global operator
	operator = ''
	txt_input.set(operator)

def abc(idx):
	buttonclick(idx)

def equals():
	global operator
	try:
		equal = str(eval(operator))
		txt_input.set(equal)
		operator = equal
	except  ZeroDivisionError:
		txt_input.set("INVALID")
	except  SyntaxError:
		txt_input.set("INVALID")

		

def rmv():
	try:
		global operator
		temp = list(operator)
		temp.pop()
		operator = ''.join(temp)
		txt_input.set(operator)
	except IndexError:
		txt_input.set("")



txt_display = Entry(root, font = "Times 25 bold", textvariable = txt_input, bd = 30, insertwidth = 4, bg = "powder blue", justify = "right").grid(columnspan = 4)
colors = {
	'num': "white", "oprts": "medium purple", "del":"pale green"
	}

operators = ['+','-','*','/']
symbols = ['=','C','<=']
for x in range(4):
	for y in range(3):
		idx = 9-(3*x+y)
		buttons.append(Button(root, text = str(idx), command = lambda name=idx: abc(name), padx = 16, pady = 16,bd = 8, bg = colors['num'], fg = "black", font = "Times 20 bold").grid(row = x+1, column = y, sticky = N+S+E+W))
		if idx <= 0:
			break

for x in range(4):
	Button(root, text = operators[x], command = lambda name=operators[x]: abc(name), padx = 16, pady = 16, bd = 8, bg = colors['oprts'], fg = 'black', font = "Times 20 bold").grid(row = x+1, column = 3, sticky = N+S+E+W)
for x in range(2):
	if x==0:
		Button(root, text = symbols[x], command = equals, padx = 15, pady = 16, bd = 8, bg = colors['del'], fg = 'black', font = "Times 20 bold").grid(row = 4, column = x+1, sticky = N+S+E+W)
	else:

		Button(root, text = symbols[x], command = cleardisplay, pady = 16, bd = 8, bg = colors['del'], fg = 'black', font = "Times 15 bold").grid(row = 4, column = x+1, sticky = N+S+W)
		Button(root, text = symbols[x+1], command = rmv, pady = 16, bd = 8, bg = colors['del'], fg = 'black', font = "Times 15 bold").grid(row = 4, column = x+1, sticky = N+S+E)
##########################
'''
text="Made by - H i m a n s h u   G u l l a i y a"
text = (' '*10) + text + (' '*10)
marquee = Text(root, height=1, width=0)
marquee.grid(row = 6, columnspan = 4)
i = 0
def command(x, i):
    marquee.insert("1.1", x)
    if i == len(text):
        i = 0
    else:
        i = i+1
    root.after(100, lambda:command(text[i:i+10], i))

command(text[i:i+10], i)
'''
#########marquee #####

class Marquee(Canvas):
    def __init__(self, parent, text, margin=2, borderwidth=1, relief='flat', fps=45):
        Canvas.__init__(self, parent, borderwidth=borderwidth, relief=relief)
        self.fps = fps

        # start by drawing the text off screen, then asking the canvas
        # how much space we need. Use that to compute the initial size
        # of the canvas. 
        text = self.create_text(0, -1000, text=text, font= ("Purisa", 10), anchor="w", tags=("text",))
        (x0, y0, x1, y1) = self.bbox("text")
        width = (x1 - x0) + (2*margin) + (2*borderwidth)
        height = (y1 - y0) + (2*margin) + (2*borderwidth)
        self.configure(width=width, height=height)

        # start the animation
        self.animate()

    def animate(self):
        (x0, y0, x1, y1) = self.bbox("text")
        if x1 < 0 or y0 < 0:
            # everything is off the screen; reset the X
            # to be just past the right margin
            x0 = self.winfo_width()
            y0 = int(self.winfo_height()/2)
            self.coords("text", x0, y0)
        else:
            self.move("text", -1, 0)

        # do again in a few milliseconds
        self.after_id = self.after(int(1000/self.fps), self.animate)

txt = "HIMANSHU GULLAIYA"
txt = ' '.join(list(txt))
marquee = Marquee(root, text = txt, borderwidth=1, relief="sunken")
marquee.grid(row = 6, columnspan = 4)
root.mainloop()
