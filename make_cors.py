from opimodel import colors, fonts, rules, widgets
from renderers.css import render
import os

example_dir = os.path.dirname(os.path.realpath(__file__))
colors.parse_css_color_file(os.path.join(example_dir, 'examples', 'color.def'))
fonts.parse_css_font_file(os.path.join(example_dir, 'examples', 'font.def'))

d = widgets.Display(604, 440)
d.set_bg_color(colors.CANVAS)

l = widgets.Label(4, 4, 596, 40, "SOFB and FOFB Corrector Enable")
l.set_font(fonts.DEFAULT)
l.set_bg_color(colors.Color(rgb=(198,181,198)))
l.set_fg_color(colors.TEXT_FG)
l.transparent = False
d.add_child(l)

def toprightbox(boxx, boxy, boxtext):
	l = widgets.Label(boxx, boxy, 21, 18, boxtext)
	l.set_font(fonts.FINE_PRINT)
	l.set_bg_color(colors.CANVAS)
	l.set_fg_color(colors.TEXT_FG)
	l.transparent = False
	l.border_width = 1
	l.border_color = colors.BLACK
	l.border_style = 1
	d.add_child(l)

toprightbox(558,6,"SH")
toprightbox(578,6,"SV")
toprightbox(558,23,"FH")
toprightbox(578,23,"FV")

l = widgets.Label(360, 82, 240, 16, "RF feedback always uses all correctors")
l.set_font(fonts.FINE_PRINT)
l.set_fg_color(colors.TEXT_FG)
d.add_child(l)

toplist = ['01','02','03','04','05','06','07', '08', '09', '10', '11', '12', '13', 
           '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24']
for topnumber in range(1,25):
	topx = 28 + 24 * (topnumber - 1)
	l = widgets.Label(topx, 48, 20, 24, toplist[topnumber - 1])
	l.set_font(fonts.FINE_PRINT)
	l.set_fg_color(colors.TEXT_FG)
	l.set_bg_color(colors.GREY_50_)
	l.transparent = False
	d.add_child(l)

sidelist = ['S1', 'S2', '01', '02', '03', '04', '05', 'C1', 'C2', '06', '07', '08', '09', '10']
for sidenumber in range(1,14):
	sidey = 76 + 28 * (sidenumber - 1)
	l = widgets.Label(4, sidey, 20, 24, sidelist[sidenumber - 1])
	l.set_font(fonts.FINE_PRINT)
	l.set_fg_color(colors.TEXT_FG)
	l.set_bg_color(colors.GREY_50_)
	l.transparent = False
	d.add_child(l)

def createbutton(buttonx, buttony):
	w = widgets.Rectangle(buttonx, buttony, 11, 13)
	w.set_bg_color(colors.GREEN)
	w.line_width = 1
	w.line_color = colors.BLACK
	d.add_child(w)
	w = widgets.Rectangle(buttonx + 10, buttony, 11, 13)
	w.set_bg_color(colors.GREEN)
	w.line_width = 1
	w.line_color = colors.BLACK
	d.add_child(w)
	w = widgets.Rectangle(buttonx, buttony + 12, 11, 13)
	w.set_bg_color(colors.GREEN)
	w.line_width = 1
	w.line_color = colors.BLACK
	d.add_child(w)
	w = widgets.Rectangle(buttonx + 10, buttony + 12, 11, 13)
	w.set_bg_color(colors.GREEN)
	w.line_width = 1
	w.line_color = colors.BLACK
	d.add_child(w)
	w = widgets.Rectangle(buttonx, buttony, 21, 25)
	w.set_bg_color(colors.GREEN)
	w.transparent = True
	d.add_child(w)

for buttonnumber in range(1,25):
	if buttonnumber == 9:
		createbutton(220, 76)
	elif buttonnumber == 13:
		createbutton(316, 76)
	if buttonnumber == 9:
		createbutton(220, 104)
	elif buttonnumber == 13:
		createbutton(316, 104)
	createbutton(28 + 24 * (buttonnumber - 1), 132)
	if buttonnumber == 2:
		pass
	else:
		createbutton(76 + 24 * (buttonnumber - 3), 160)
	if buttonnumber == 2:
		pass
	else:
		createbutton(76 + 24 * (buttonnumber - 3), 188)
	createbutton(28 + 24 * (buttonnumber - 1), 216)
	createbutton(28 + 24 * (buttonnumber - 1), 244)
	if buttonnumber == 2:
		createbutton(52, 272)
		createbutton(52, 300)
	if buttonnumber == 2:
		pass
	else:
		createbutton(76 + 24 * (buttonnumber - 3), 328)
	createbutton(28 + 24 * (buttonnumber - 1), 356)
	if buttonnumber == 2:
		createbutton(52, 384)
		createbutton(52, 412)

o = render.get_opi_renderer(d)
o.write_to_file("cors.opi")
