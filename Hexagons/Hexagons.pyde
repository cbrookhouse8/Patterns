# Recreates a pattern from this article
# on Islamic Geometric Design
# https://www.theguardian.com/science/alexs-adventures-in-numberland/2015/feb/10/muslim-rule-and-compass-the-magic-of-islamic-geometric-design

def setup():
    size(800,800)
    background(118,185,214)
    
def draw():
    background(118,185,214)
    
    # draw thick white lines
    fill(255)
    pattern(80,10)
        
    # then on top draw the thin lines
    fill(115,110,107)
    pattern(80,3)
    
def pattern(rad,stroke_weight):
    # radius to generate
    # the hexagon vertices

    # half the interior angle
    theta = TWO_PI/12
    
    # perpendicular distance
    # from centre to a side
    base = rad * cos(theta)
    opp = rad * sin(theta)
    
    # horizontal overlap of the hexagons
    xOverlap = 15
        
    for i in range(0,10):
        for j in range(0,10):
            # For the i'th row, the position of 
            # the centre of the first hexagon
            cxStart = i%2 * (base-xOverlap)
            
            # gap between the centres of
            # hexagons on the same row
            cxGap = 2*base - 2*xOverlap
            
            # 3/4 the diameter of a hexagon
            # of 'base' xOverlap
            u = 3*xOverlap*tan(theta)
            
            # Three vertical translations:
            #   1. top vertex of i'th row hexagon
            #      to be in line with bottom vertex
            #      of i-1 row hexaxon
            #   2. top vertex of i'th row hexagon
            #      to be in line with second from 
            #      bottom vertices of i-1 row hexagon
            #   3. 'u': 3/4 the diameter of a hexagon
            #      of base length xOverlap
            
            cyGap = (2*rad) - opp - u
            
            hexagon(cxStart+j*cxGap,i*cyGap,rad,stroke_weight)
    
def hexagon(x,y,r,w):
    theta = (TWO_PI/6) / 2
    
    # the gap between the inner and outer
    # radii is the stroke weight, w
    inner_rad = r - w/2
    outer_rad = r + w/2
    
    noStroke()
    
    # clockwise along the
    # outer radius
    
    beginShape()
    
    for i in range(0,7):
        xp = x + cos(theta) * outer_rad
        yp = y + sin(theta) * outer_rad
        vertex(xp, yp)
        theta = theta + TWO_PI / 6
    
    # wind back by an increment
    theta = theta - TWO_PI / 6 
    
    # anti-clockwise along
    # the inner radius
    
    for i in range(0,7):
        xp = x + cos(theta) * inner_rad
        yp = y + sin(theta) * inner_rad
        vertex(xp, yp)
        theta = theta - TWO_PI / 6
    
    endShape()