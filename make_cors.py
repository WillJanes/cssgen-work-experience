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

def key(keyx, keyy, keytext):
	l = widgets.Label(keyx, keyy, 21, 18, keytext)
	l.set_font(fonts.FINE_PRINT)
	l.set_bg_color(colors.CANVAS)
	l.set_fg_color(colors.TEXT_FG)
	l.transparent = False
	l.border_width = 1
	l.border_color = colors.BLACK
	l.border_style = 1
	d.add_child(l)

key(558,6,"SH")
key(578,6,"SV")
key(558,23,"FH")
key(578,23,"FV")

l = widgets.Label(360, 82, 240, 16, "RF feedback always uses all correctors")
l.set_font(fonts.FINE_PRINT)
l.set_fg_color(colors.TEXT_FG)
d.add_child(l)

for topnumber in range(1,25):
	topx = 28 + 24 * (topnumber - 1)
	l = widgets.Label(topx, 48, 20, 24, '{:02d}'.format(topnumber))
	l.set_font(fonts.FINE_PRINT)
	l.set_fg_color(colors.TEXT_FG)
	l.set_bg_color(colors.GREY_50_)
	l.transparent = False
	d.add_child(l)

sidelist = ['S1', 'S2', '01', '02', '03', '04', '05', 'C1', 'C2', '06', '07', '08', '10']
for sidenumber in range(1,14):
	sidey = 76 + 28 * (sidenumber - 1)
	l = widgets.Label(4, sidey, 20, 24, sidelist[sidenumber - 1])
	l.set_font(fonts.FINE_PRINT)
	l.set_fg_color(colors.TEXT_FG)
	l.set_bg_color(colors.GREY_50_)
	l.transparent = False
	d.add_child(l)

def createbutton(buttonx, buttony, pv_prefix):
	w = widgets.Led(buttonx, buttony, 11, 13, pv_prefix.format('H')+'SLOW:DISABLED')
	w.set_bg_color(colors.GREEN)
	w.line_width = 1
	w.line_color = colors.BLACK
	w.square_led = True
	w.effect_3d = False
	w.border_alarm_sensitive = False
	w.bulb_border = 1
	d.add_child(w)
	w = widgets.Led(buttonx + 10, buttony, 11, 13, pv_prefix.format('V')+'SLOW:DISABLED')
	w.set_bg_color(colors.GREEN)
	w.line_width = 1
	w.line_color = colors.BLACK
	w.square_led = True
	w.effect_3d = False
	w.border_alarm_sensitive = False
	w.bulb_border = 1
	d.add_child(w)
	w = widgets.Led(buttonx, buttony + 12, 11, 13, pv_prefix.format('H')+'FAST:DISABLED')
	w.set_bg_color(colors.GREEN)
	w.line_width = 1
	w.line_color = colors.BLACK
	w.square_led = True
	w.effect_3d = False
	w.border_alarm_sensitive = False
	w.bulb_border = 1
	d.add_child(w)
	w = widgets.Led(buttonx + 10, buttony + 12, 11, 13, pv_prefix.format('V')+'FAST:DISABLED')
	w.set_bg_color(colors.GREEN)
	w.line_width = 1
	w.line_color = colors.BLACK
	w.square_led = True
	w.effect_3d = False
	w.border_alarm_sensitive = False
	w.bulb_border = 1
	d.add_child(w)
	w = widgets.Rectangle(buttonx, buttony, 21, 25,)
	w.set_bg_color(colors.GREEN)
	w.transparent = True
	d.add_child(w)
#SR01A-PC-VSTR-01:SLOW:DISABLED

def generate_prefix(i, j, mini_beta = False, slow = False):
	if mini_beta:
		pv = "SR{:02d}S-PC-{}STR-{:02d}:".format(i, '{}', j)
	elif slow:
		pv = "SR{:02d}A-PC-{}SCOR-{:02d}:".format(i, '{}', j)
	else:
		pv = "SR{:02d}A-PC-{}STR-{:02d}:".format(i, '{}', j)
	return  pv

for buttonnumber in range(1,25):
	x = 4 + 24 * buttonnumber
	if buttonnumber == 9 or buttonnumber == 13:
		createbutton(x,  76, generate_prefix(buttonnumber, 1, mini_beta = True))
		createbutton(x, 104, generate_prefix(buttonnumber, 2, mini_beta = True))
	if buttonnumber != 2:
		createbutton(x, 160, generate_prefix(buttonnumber, 2))
		createbutton(x, 188, generate_prefix(buttonnumber, 3))
		createbutton(x, 328, generate_prefix(buttonnumber, 6))
	if buttonnumber == 2:
		createbutton(x, 272, generate_prefix(buttonnumber, 1, slow = True))
		createbutton(x, 300, generate_prefix(buttonnumber, 2, slow = True))
		createbutton(x, 384, generate_prefix(buttonnumber, 8))
		createbutton(x, 412, generate_prefix(buttonnumber, 10))
	createbutton(x, 132, generate_prefix(buttonnumber, 1))
	createbutton(x, 216, generate_prefix(buttonnumber, 4))
	createbutton(x, 244, generate_prefix(buttonnumber, 5))
	createbutton(x, 356, generate_prefix(buttonnumber, 7))

o = render.get_opi_renderer(d)
o.write_to_file("cors.opi")
