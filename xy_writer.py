should_draw = False

def line_to(x,y,z):
    global should_draw
    if (should_draw == False):
        print "\n%s %s"%(x,y)
        should_draw=True
    else:
        print "%s %s"%(x,y)
        
def xy_line_to(x,y):
    line_to(x, y, 0)

def xy_arc_to( x,y, r, cx,cy, cw ):
    print "# SVG does not support arc yet"
    
def xy_rapid_to(x,y):
    pass

def pen_up():
    global should_draw
    should_draw=False
    pass

def pen_down(z=0):
#     global should_draw
#     should_draw=False
    plunge(z)

def plunge(z):
    # PG: Do we need to save this point to use later..
    pass

def preamble():
    pass

def postamble():
    pass

if __name__ == "__main__":
    print "Nothing to see here."
