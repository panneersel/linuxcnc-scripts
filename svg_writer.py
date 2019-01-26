dpi = 100
#dpi = 1

minx = 0
maxx = 200
miny = 0
maxy = 300

width = 200
height = 300

prev_x = -1
prev_y = -1

color = 'black'

header_template = '''
<?xml version="1.0" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<svg width="%s" height="%s" xmlns="http://www.w3.org/2000/svg" version="1.1">
'''

path_template = '<path d="M %f %f L %f %f" fill="none" stroke="' + color + '" ' + \
    'stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />'
    
circle_template = '<circle cx="%f" cy="%f" r="%f" fill="none" stroke="' + color + '" stroke-width="%f" />'

def line_to(x,y,z):
    global prev_x
    global prev_y
    if (prev_x == -1 and prev_y == -1):
        prev_x = x
        prev_y = y
        return
    x1 = prev_x
    y1 = prev_y
    x2 = x
    y2 = y
    line = [
        x1, y1,
        x2, y2
    ]
    # print path_template % tuple(line)
    print circle_template % (x,y,2,1)

def xy_line_to(x,y):
    line_to(x, y, 0)

# (endpoint, radius, center, cw?)
def xy_arc_to( x,y, r, cx,cy, cw ):
    print "<!-- SVG does not support arc yet -->"
    # print "G3 X% 8.5f Y% 8.5f R% 8.5f" % (x, y, r)
    # FIXME: optional IJK format arcs
    
def xy_rapid_to(x,y):
    pass

def pen_up():
    pass

def pen_down(z=0):
    plunge(z)

def plunge(z):
    # PG: Do we need to save this point to use later..
    pass

def preamble():
    print header_template % ( width, height )

def postamble():
    print "</svg>"

if __name__ == "__main__":
    print "Nothing to see here."
