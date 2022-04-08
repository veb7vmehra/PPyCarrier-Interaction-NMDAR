import sys, pygame
import math
import random
import numpy as np

pygame.init()

size = width, height = 1280, 720
speed = [2, 2]
bg_color = 255, 242, 204
black = 0, 0, 0
white = 255, 255, 255
red = 255, 0, 0
green = 0, 255, 0
dark_green = 0, 100, 0
green3 = 0, 175, 0
blue = 0, 0, 250
dark_blue = 0, 0, 100
yellow = 255, 255, 0
pink = 255, 192, 203
pink2 = 255,204,246
gray = 	128, 128, 128
maroon = 128, 0, 0
pink3 = 100, 5, 28

def gety(point1, point2, x):
    m = (point2[1] - point1[1])/(point2[0] - point1[0])
    y = ((x - point1[0])*m) + point1[1]
    return y

def getx(point1, point2, y):
    m = (point2[1] - point1[1])/(point2[0] - point1[0])
    x = ((y - point1[1])/m) + point1[0]
    return x

def getAngle(point1, point2):
    m = (point2[1] - point1[1])/(point2[0] - point1[0])
    a = math.degrees(math.atan(m))
    return a

def checkLine(point1, point2, point, dir):
    m = (point2[1] - point1[1])/(point2[0] - point1[0])
    if dir == 1:
        if m >= 0:
            if point[1] - m*point[0] + m*point1[0] - point1[1] >= 0:
                point[1] = m*(point[0] - point1[0]) + point1[1] - random.randint(1, 6)
        else:
            if point[1] - m*point[0] + m*point1[0] - point1[1] <= 0:
                point[1] = m*(point[0] - point1[0]) + point1[1] + random.randint(1, 6)
    elif dir == -1:
        if m >= 0:
            if point[1] - m*point[0] + m*point1[0] - point1[1] <= 0:
                point[0] = (point[1] - point1[1] + m*point1[0])/m - random.randint(1, 6)
        else:
            if point[1] - m*point[0] + m*point1[0] - point1[1] >= 0:
                point[0] = (point[1] - point1[1] + m*point1[0])/m - random.randint(1, 6)
    elif dir == 2:
        if m >= 0:
            if point[1] - m*point[0] + m*point1[0] - point1[1] >= 0:
                point[1] = m*(point[0] - point1[0]) + point1[1] - 70 - random.randint(1, 6)
        else:
            if point[1] - m*point[0] + m*point1[0] - point1[1] <= 0:
                point[1] = m*(point[0] - point1[0]) + point1[1] + 140 + random.randint(1, 6)
    elif dir == -2:
        if m >= 0:
            if point[1] - m*point[0] + m*point1[0] - point1[1] <= 0:
                point[0] = (point[1] - point1[1] + m*point1[0] - 70)/m - random.randint(1, 6)
        else:
            if point[1] - m*point[0] + m*point1[0] - point1[1] >= 0:
                point[0] = (point[1] - point1[1] + m*point1[0] - 70)/m - random.randint(1, 6)
    return point

def checkGate(point1, point2, midpoint, point):
    m = (point2[1] - point1[1])/(point2[0] - point1[0])
    a = math.atan(m)
    xs = (midpoint[0] - 76) + (100* math.sin(a))
    ys = gety(point1, point2, midpoint[0] - 76) + (100*math.cos(a))
    if (xs <= point[0] <= xs + 52) and (ys <= point[1] <= ys + 202):
        if abs(xs + 52 - point[0]) >= abs(ys + 101 - point[1]):
            point[0] = point[0] - (point[0] - (xs + random.randint(1, 6)))
        else:
            point[1] = point[1] - (point[1] - (ys + random.randint(1, 6)))

    xs = (midpoint[0] + 14) + (100* math.sin(a))
    ys = gety(point1, point2, midpoint[0] + 14) + (100*math.cos(a))
    if (xs <= point[0] <= xs + 52) and (ys <= point[1] <= ys + 202):
        if abs(xs + 52 - point[0]) >= abs(ys + 101 - point[1]):
            point[0] = point[0] - (point[0] - (xs + random.randint(1, 6)))
        else:
            point[1] = point[1] - (point[1] - (ys + random.randint(1, 6)))
    return point

nPoints = 3

points = []
t1 = random.uniform(900, 1280)
t2 = 0
points.append([t1, t2])
t1 = random.uniform(900, 1280)
t2 = 720
points.append([t1, t2])
t1 = 0
t2 = random.uniform(0, 720)
points.append([t1, t2])

midpoints = [[(points[0][0]+points[1][0])/2, (points[0][1]+points[1][1])/2], [(points[1][0]+points[2][0])/2, (points[1][1]+points[2][1])/2], [(points[2][0]+points[0][0])/2, (points[2][1]+points[0][1])/2]]

voltage = int(input("Give Voltage: "))

center = [100, 100]
broken = 0

ca_no = 1
mg_no = 1
na_no = 145
cl_no = 120
k_no = 4
gl_no = 3
ur_no = 2

T=10000
#CPK Coloring
ca=5 #green
mg = 3 #dark green
na = 4 #blue
cl = 4 #green3
k = 6 #pink3
gl = 1 #red
ur = 2 #dark blue
carrier = 4
if voltage < -70:
    carrier = 2
elif -40 >= voltage > -70:
    carrier = 5
elif voltage > -40:
    carrier = 6

f = random.randint(4000, 5000) #to be changed
s = random.randint(f+500, T + 3000)

ca_pos = []
mg_pos = []
na_pos = []
k_pos = []
cl_pos = []
carrier_pos = []
carr_pos = []
gl_pos = []
ur_pos = []
pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8 = [], [], [], [], [], [], [], []

drb3 = 15
d1 = []
d2 = []
d3 = []

for i in range(drb3):
    ls = [random.randint(100, 500), random.randint(100, 500), [], False, False, False]
    d1.append(ls)
    ls = [random.randint(100, 500), random.randint(100, 500), [], False, False, False]
    d2.append(ls)
    ls = [random.randint(100, 500), random.randint(100, 500), [], False, False, False]
    d2.append(ls)

blocked = [False, False, False]

first, second, third, fourth = T+1, T+1, T+1, T+1
brk = 0

def tryBlock(point1, point2, midpoint, dx1, dy1, z, v, i):
    global first
    m = (point2[1] - point1[1])/(point2[0] - point1[0])
    a = math.atan(m)
    xs = (midpoint[0] - 76) + (100* math.sin(a))
    ys = gety(point1, point2, midpoint[0] - 76) + (100*math.cos(a))
    xl = (midpoint[0] + 14) + (100* math.sin(a)) + 52
    yl = gety(point1, point2, midpoint[0] + 14) + (100*math.cos(a)) + 202
    if (xs <= dx1 <= xl and ys <= dy1 <= yl) or z[v+3] == True:
        dx1 = (z[2][i - (first+1)][0]) + (midpoint[0] - z[2][i - (first+1)][0] + random.randint(-10, 10))/z[1]
        dy1 = (z[2][i - (first+1)][1]) + (midpoint[1] - z[2][i - (first+1)][1] + random.randint(-10, 10))/z[1]
        z[1] = z[1] - 1
        z[v+3] = True
    return dx1, dy1

def carr():
    global first, second, third, fourth, pos1, pos2
    carrier_pos.append({})
    carrier_pos[0]["x"]=np.array([])
    carrier_pos[0]["y"]=np.array([])
    carrier_pos[0]["x"]=np.insert(carrier_pos[0]["x"],0,640)
    carrier_pos[0]["y"]=np.insert(carrier_pos[0]["y"],0,360)

    for j in range(0,T):
        angle = random.uniform(0, 4*np.pi)
        r =carrier*np.cos(angle)
        b =carrier*np.sin(angle)
        carrier_pos[0]["x"]=np.insert(carrier_pos[0]["x"],len(carrier_pos[0]["x"]),carrier_pos[0]["x"][j]+r)
        carrier_pos[0]["y"]=np.insert(carrier_pos[0]["y"],len(carrier_pos[0]["y"]),carrier_pos[0]["y"][j]+b)
    
    for i in range(0, T):
        carr_pos.append([])
        carr_pos[i].append(carrier_pos[0]["x"][i].item())
        carr_pos[i].append(carrier_pos[0]["y"][i].item())
        
        if carr_pos[i][0] > 1280:
            carr_pos[i][0] = carr_pos[i][0] - (carr_pos[i][0] - (1280 + random.randint(1, 6)))
        elif carr_pos[i][0] < 0:
            carr_pos[i][0] = random.randint(1, 6)
        
        if carr_pos[i][1] > 650:
            carr_pos[i][1] = carr_pos[i][1] - (carr_pos[i][1] - (650 + random.randint(0, 5)))
        elif carr_pos[i][1] < 70:
            carr_pos[i][1] = random.randint(70, 76)

        for v in range(nPoints):
            q = v + 1
            dr = 2
            if q >= nPoints:
                q = 0
            if v == 0:
                dr = -2
            checkLine(points[v], points[q], carr_pos[i], dr)
        
        if i == f and voltage < -69 and first == T+1:
            first = i
            if abs(carr_pos[i][1] - midpoints[1][1]) > abs(carr_pos[i][1] - midpoints[2][1]):
                if abs(carr_pos[i][0] - midpoints[0][0]) > abs(carr_pos[i][0] - midpoints[2][0]):
                    brk = 2
                else:
                    brk = 0
            else:
                if abs(carr_pos[i][0] - midpoints[0][0]) > abs(carr_pos[i][0] - midpoints[1][0]):
                    brk = 1
                else:
                    brk = 0

        if i == s and voltage < -69 and second == T+1:
            second = i
            pos1.append({})
            pos1[0]["x"]=np.array([])
            pos1[0]["y"]=np.array([])
            if brk == 0:
                pos1[0]["x"]=np.insert(pos1[0]["x"],0,carr_pos[i][0]+(50/math.sqrt(2))+40)
                pos1[0]["y"]=np.insert(pos1[0]["y"],0,carr_pos[i][1]-(50/math.sqrt(2)))    
            elif brk == 1:
                pos1[0]["x"]=np.insert(pos1[0]["x"],0,carr_pos[i][0]+50)
                pos1[0]["y"]=np.insert(pos1[0]["y"],0,carr_pos[i][1]+40)
            else:
                pos1[0]["x"]=np.insert(pos1[0]["x"],0,carr_pos[i][0]+50/math.sqrt(2))
                pos1[0]["y"]=np.insert(pos1[0]["y"],0,carr_pos[i][1]-40-(50/math.sqrt(2)))

            for j in range(0,T-i):
                angle = random.uniform(0, 4*np.pi)
                r =carrier*np.cos(angle)
                b =carrier*np.sin(angle)
                pos1[0]["x"]=np.insert(pos1[0]["x"],len(pos1[0]["x"]),pos1[0]["x"][j]+r)
                pos1[0]["y"]=np.insert(pos1[0]["y"],len(pos1[0]["y"]),pos1[0]["y"][j]+b)

            pos2.append({})
            pos2[0]["x"]=np.array([])
            pos2[0]["y"]=np.array([])
            if brk == 0:
                pos2[0]["x"]=np.insert(pos2[0]["x"],0,carr_pos[i][0]+40)
                pos2[0]["y"]=np.insert(pos2[0]["y"],0,carr_pos[i][1]+50)
            elif brk == 1:
                pos2[0]["x"]=np.insert(pos2[0]["x"],0,carr_pos[i][0]-50/math.sqrt(2))
                pos2[0]["y"]=np.insert(pos2[0]["y"],0,carr_pos[i][1]+40+50/math.sqrt(2))
            else:
                pos2[0]["x"]=np.insert(pos2[0]["x"],0,carr_pos[i][0]-50)
                pos2[0]["y"]=np.insert(pos2[0]["y"],0,carr_pos[i][1]-40)
            for j in range(0,T-i):
                angle = random.uniform(0, 4*np.pi)
                r =carrier*np.cos(angle)
                b =carrier*np.sin(angle)
                pos2[0]["x"]=np.insert(pos2[0]["x"],len(pos2[0]["x"]),pos2[0]["x"][j]+r)
                pos2[0]["y"]=np.insert(pos2[0]["y"],len(pos2[0]["y"]),pos2[0]["y"][j]+b)

for i in range(ca_no):
    ca_pos.append({})
    ca_pos[i]["x"]=np.array([])
    ca_pos[i]["y"]=np.array([])
    ca_pos[i]["x"]=np.insert(ca_pos[i]["x"],0,random.uniform(20, 1260))
    ca_pos[i]["y"]=np.insert(ca_pos[i]["y"],0,random.uniform(120, 600))

    for j in range(0,T):
        angle = random.uniform(0, 4*np.pi)
        r =ca*np.cos(angle)
        b =ca*np.sin(angle)
        ca_pos[i]["x"]=np.insert(ca_pos[i]["x"],len(ca_pos[i]["x"]),ca_pos[i]["x"][j]+r)
        ca_pos[i]["y"]=np.insert(ca_pos[i]["y"],len(ca_pos[i]["y"]),ca_pos[i]["y"][j]+b)

for i in range(mg_no):
    mg_pos.append({})
    mg_pos[i]["x"]=np.array([])
    mg_pos[i]["y"]=np.array([])
    mg_pos[i]["x"]=np.insert(mg_pos[i]["x"],0,random.uniform(20,1260))
    mg_pos[i]["y"]=np.insert(mg_pos[i]["y"],0,random.uniform(120,600))

    for j in range(0,T):
        angle = random.uniform(0, 4*np.pi)
        r =mg*np.cos(angle)
        b =mg*np.sin(angle)
        mg_pos[i]["x"]=np.insert(mg_pos[i]["x"],len(mg_pos[i]["x"]),mg_pos[i]["x"][j]+r)
        mg_pos[i]["y"]=np.insert(mg_pos[i]["y"],len(mg_pos[i]["y"]),mg_pos[i]["y"][j]+b)

for i in range(na_no):
    na_pos.append({})
    na_pos[i]["x"]=np.array([])
    na_pos[i]["y"]=np.array([])
    na_pos[i]["x"]=np.insert(na_pos[i]["x"],0,random.uniform(20,1260))
    na_pos[i]["y"]=np.insert(na_pos[i]["y"],0,random.uniform(120,600))

    for j in range(0,T):
        angle = random.uniform(0, 4*np.pi)
        r =na*np.cos(angle)
        b =na*np.sin(angle)
        na_pos[i]["x"]=np.insert(na_pos[i]["x"],len(na_pos[i]["x"]),na_pos[i]["x"][j]+r)
        na_pos[i]["y"]=np.insert(na_pos[i]["y"],len(na_pos[i]["y"]),na_pos[i]["y"][j]+b)

for i in range(cl_no):
    cl_pos.append({})
    cl_pos[i]["x"]=np.array([])
    cl_pos[i]["y"]=np.array([])
    cl_pos[i]["x"]=np.insert(cl_pos[i]["x"],0,random.uniform(20,1260))
    cl_pos[i]["y"]=np.insert(cl_pos[i]["y"],0,random.uniform(120,600))

    for j in range(0,T):
        angle = random.uniform(0, 4*np.pi)
        r =cl*np.cos(angle)
        b =cl*np.sin(angle)
        cl_pos[i]["x"]=np.insert(cl_pos[i]["x"],len(cl_pos[i]["x"]),cl_pos[i]["x"][j]+r)
        cl_pos[i]["y"]=np.insert(cl_pos[i]["y"],len(cl_pos[i]["y"]),cl_pos[i]["y"][j]+b)

for i in range(k_no):
    k_pos.append({})
    k_pos[i]["x"]=np.array([])
    k_pos[i]["y"]=np.array([])
    k_pos[i]["x"]=np.insert(k_pos[i]["x"],0,random.uniform(20,1260))
    k_pos[i]["y"]=np.insert(k_pos[i]["y"],0,random.uniform(120,600))

    for j in range(0,T):
        angle = random.uniform(0, 4*np.pi)
        r =k*np.cos(angle)
        b =k*np.sin(angle)
        k_pos[i]["x"]=np.insert(k_pos[i]["x"],len(k_pos[i]["x"]),k_pos[i]["x"][j]+r)
        k_pos[i]["y"]=np.insert(k_pos[i]["y"],len(k_pos[i]["y"]),k_pos[i]["y"][j]+b)

for i in range(gl_no):
    gl_pos.append({})
    gl_pos[i]["x"]=np.array([])
    gl_pos[i]["y"]=np.array([])
    gl_pos[i]["x"]=np.insert(gl_pos[i]["x"],0,random.uniform(20,1260))
    gl_pos[i]["y"]=np.insert(gl_pos[i]["y"],0,random.uniform(120,600))

    for j in range(0,T):
        angle = random.uniform(0, 4*np.pi)
        r =gl*np.cos(angle)
        b =gl*np.sin(angle)
        gl_pos[i]["x"]=np.insert(gl_pos[i]["x"],len(gl_pos[i]["x"]),gl_pos[i]["x"][j]+r)
        gl_pos[i]["y"]=np.insert(gl_pos[i]["y"],len(gl_pos[i]["y"]),gl_pos[i]["y"][j]+b)

for i in range(ur_no):
    ur_pos.append({})
    ur_pos[i]["x"]=np.array([])
    ur_pos[i]["y"]=np.array([])
    ur_pos[i]["x"]=np.insert(ur_pos[i]["x"],0,random.uniform(20,1260))
    ur_pos[i]["y"]=np.insert(ur_pos[i]["y"],0,random.uniform(120,600))

    for j in range(0,T):
        angle = random.uniform(0, 4*np.pi)
        r =ur*np.cos(angle)
        b =ur*np.sin(angle)
        ur_pos[i]["x"]=np.insert(ur_pos[i]["x"],len(ur_pos[i]["x"]),ur_pos[i]["x"][j]+r)
        ur_pos[i]["y"]=np.insert(ur_pos[i]["y"],len(ur_pos[i]["y"]),ur_pos[i]["y"][j]+b)

def render(i):
    global blocked, pos1, pos2, pos3, pos4, pos5
    screen.fill(pink2)
    pygame.draw.polygon(screen, bg_color, points)
    pygame.draw.line(screen, black, [points[0][0], points[0][1]], [getx(points[0], points[1], midpoints[0][1] - 75), midpoints[0][1] - 75])
    pygame.draw.line(screen, black, [getx(points[0], points[1], midpoints[0][1] + 75), midpoints[0][1] + 75], [points[1][0], points[1][1]])
    pygame.draw.line(screen, black, [points[1][0], points[1][1]], [midpoints[1][0] + 75, gety(points[1], points[2], midpoints[1][0] + 75)])
    pygame.draw.line(screen, black, [midpoints[1][0] - 75, gety(points[1], points[2], midpoints[1][0] - 75)], [points[2][0], points[2][1]])
    pygame.draw.line(screen, black, [points[2][0], points[2][1]], [midpoints[2][0] - 75, gety(points[2], points[0], midpoints[2][0] - 75)])
    pygame.draw.line(screen, black, [midpoints[2][0] + 75, gety(points[2], points[0], midpoints[2][0] + 75)], [points[0][0], points[0][1]])
    
    center = [carr_pos[i][0], carr_pos[i][1]]

    for j in ca_pos:
        x = j["x"][i].item()
        y = j["y"][i].item()
        if x > 1280:
            x = x - (x - (1280+random.randint(1, 6)))
        elif x < 0:
            x = random.randint(1, 6)
        if y > 720:
            y = y - (y - (720 + random.randint(1, 6)))
        elif y < 0:
            y = random.randint(1, 6)

        for v in range(nPoints):
            q = v + 1
            dr = 1
            if q >= nPoints:
                q = 0
            if v == 0:
                dr = -1
            point = checkLine(points[v], points[q], [x, y], dr)
            x = point[0]
            y = point[1]

            point = checkGate(points[v], points[q], midpoints[v], [x, y])
            x = point[0]
            y = point[1]
        
        if center[0] - 70 < x < center[0] + 70 and center[1] - 70 < y < center[1] + 70:
            if abs(center[0] - x) < abs(center[1] - y):
                if center[1] - y < 0:
                    y = y + random.randint(1, 6)
                else:
                    y = y - random.randint(1, 6)
            else:
                if center[0] - x < 0:
                    x = x + random.randint(1, 6)
                else:
                    x = x - random.randint(1, 6)        
        pygame.draw.circle(screen, black, [x, y], 9, 1)
        pygame.draw.circle(screen, green, [x, y], 8)
    for j in mg_pos:
        x = j["x"][i].item()
        y = j["y"][i].item()
        if x > 1280:
            x = x - (x - (1280+random.randint(1, 6)))
        elif x < 0:
            x = random.randint(1, 6)
        if y > 720:
            y = y - (y - (720 + random.randint(1, 6)))
        elif y < 0:
            y = random.randint(1, 6)

        for v in range(nPoints):
            q = v + 1
            dr = 1
            if q >= nPoints:
                q = 0
            if v == 0:
                dr = -1
            point = checkLine(points[v], points[q], [x, y], dr)
            x = point[0]
            y = point[1]

            point = checkGate(points[v], points[q], midpoints[v], [x, y])
            x = point[0]
            y = point[1]
        if center[0] - 70 < x < center[0] + 70 and center[1] - 70 < y < center[1] + 70:
            if abs(center[0] - x) < abs(center[1] - y):
                if center[1] - y < 0:
                    y = y + random.randint(1, 6)
                else:
                    y = y - random.randint(1, 6)
            else:
                if center[0] - x < 0:
                    x = x + random.randint(1, 6)
                else:
                    x = x - random.randint(1, 6)
        pygame.draw.circle(screen, black, [x, y], 4, 1)
        pygame.draw.circle(screen, dark_green, [x, y], 3)
    for j in na_pos:
        x = j["x"][i].item()
        y = j["y"][i].item()
        if x > 1280:
            x = x - (x - (1280+random.randint(1, 6)))
        elif x < 0:
            x = random.randint(1, 6)
        if y > 720:
            y = y - (y - (720 + random.randint(1, 6)))
        elif y < 0:
            y = random.randint(1, 6)

        for v in range(nPoints):
            q = v + 1
            dr = 1
            if q >= nPoints:
                q = 0
            if v == 0:
                dr = -1
            point = checkLine(points[v], points[q], [x, y], dr)
            x = point[0]
            y = point[1]

            point = checkGate(points[v], points[q], midpoints[v], [x, y])
            x = point[0]
            y = point[1]

        if center[0] - 70 < x < center[0] + 70 and center[1] - 70 < y < center[1] + 70:
            if abs(center[0] - x) < abs(center[1] - y):
                if center[1] - y < 0:
                    y = y + random.randint(1, 6)
                else:
                    y = y - random.randint(1, 6)
            else:
                if center[0] - x < 0:
                    x = x + random.randint(1, 6)
                else:
                    x = x - random.randint(1, 6)
        pygame.draw.circle(screen, black, [x, y], 6, 1)
        pygame.draw.circle(screen, blue, [x, y], 5)

    for j in cl_pos:
        x = j["x"][i].item()
        y = j["y"][i].item()
        if x > 1280:
            x = x - (x - (1280+random.randint(1, 6)))
        elif x < 0:
            x = random.randint(1, 6)
        if y > 720:
            y = y - (y - (720 + random.randint(1, 6)))
        elif y < 0:
            y = random.randint(1, 6)

        for v in range(nPoints):
            q = v + 1
            dr = 1
            if q >= nPoints:
                q = 0
            if v == 0:
                dr = -1
            point = checkLine(points[v], points[q], [x, y], dr)
            x = point[0]
            y = point[1]

            point = checkGate(points[v], points[q], midpoints[v], [x, y])
            x = point[0]
            y = point[1]
        if center[0] - 70 < x < center[0] + 70 and center[1] - 70 < y < center[1] + 70:
            if abs(center[0] - x) < abs(center[1] - y):
                if center[1] - y < 0:
                    y = y + random.randint(1, 6)
                else:
                    y = y - random.randint(1, 6)
            else:
                if center[0] - x < 0:
                    x = x + random.randint(1, 6)
                else:
                    x = x - random.randint(1, 6)
        pygame.draw.circle(screen, black, [x, y], 6, 1)
        pygame.draw.circle(screen, green3, [x, y], 5)

    for j in k_pos:
        x = j["x"][i].item()
        y = j["y"][i].item()
        if x > 1280:
            x = x - (x - (1280+random.randint(1, 6)))
        elif x < 0:
            x = random.randint(1, 6)
        if y > 720:
            y = y - (y - (720 + random.randint(1, 6)))
        elif y < 0:
            y = random.randint(1, 6)

        for v in range(nPoints):
            q = v + 1
            dr = 1
            if q >= nPoints:
                q = 0
            if v == 0:
                dr = -1
            point = checkLine(points[v], points[q], [x, y], dr)
            x = point[0]
            y = point[1]

            point = checkGate(points[v], points[q], midpoints[v], [x, y])
            x = point[0]
            y = point[1]
        if center[0] - 70 < x < center[0] + 70 and center[1] - 70 < y < center[1] + 70:
            if abs(center[0] - x) < abs(center[1] - y):
                if center[1] - y < 0:
                    y = y + random.randint(1, 6)
                else:
                    y = y - random.randint(1, 6)
            else:
                if center[0] - x < 0:
                    x = x + random.randint(1, 6)
                else:
                    x = x - random.randint(1, 6)
        pygame.draw.circle(screen, black, [x, y], 7, 1)
        pygame.draw.circle(screen, pink3, [x, y], 6)

    for j in gl_pos:
        x = j["x"][i].item()
        y = j["y"][i].item()
        if x > 1280:
            x = x - (x - (1280+random.randint(1, 6)))
        elif x < 0:
            x = random.randint(1, 6)
        if y > 720:
            y = y - (y - (720 + random.randint(1, 6)))
        elif y < 0:
            y = random.randint(1, 6)

        for v in range(nPoints):
            q = v + 1
            dr = 1
            if q >= nPoints:
                q = 0
            if v == 0:
                dr = -1
            point = checkLine(points[v], points[q], [x, y], dr)
            x = point[0]
            y = point[1]

            point = checkGate(points[v], points[q], midpoints[v], [x, y])
            x = point[0]
            y = point[1]
        if center[0] - 70 < x < center[0] + 70 and center[1] - 70 < y < center[1] + 70:
            if abs(center[0] - x) < abs(center[1] - y):
                if center[1] - y < 0:
                    y = y + random.randint(1, 6)
                else:
                    y = y - random.randint(1, 6)
            else:
                if center[0] - x < 0:
                    x = x + random.randint(1, 6)
                else:
                    x = x - random.randint(1, 6)
        pygame.draw.circle(screen, black, [x, y], 18, 1)
        pygame.draw.circle(screen, red, [x, y], 17)

    for j in ur_pos:
        x = j["x"][i].item()
        y = j["y"][i].item()
        if x > 1280:
            x = x - (x - (1280+random.randint(1, 6)))
        elif x < 0:
            x = random.randint(1, 6)
        if y > 720:
            y = y - (y - (720 + random.randint(1, 6)))
        elif y < 0:
            y = random.randint(1, 6)

        for v in range(nPoints):
            q = v + 1
            dr = 1
            if q >= nPoints:
                q = 0
            if v == 0:
                dr = -1
            point = checkLine(points[v], points[q], [x, y], dr)
            x = point[0]
            y = point[1]

            point = checkGate(points[v], points[q], midpoints[v], [x, y])
            x = point[0]
            y = point[1]
        if center[0] - 70 < x < center[0] + 70 and center[1] - 70 < y < center[1] + 70:
            if abs(center[0] - x) < abs(center[1] - y):
                if center[1] - y < 0:
                    y = y + random.randint(1, 6)
                else:
                    y = y - random.randint(1, 6)
            else:
                if center[0] - x < 0:
                    x = x + random.randint(1, 6)
                else:
                    x = x - random.randint(1, 6)
        pygame.draw.circle(screen, black, [x, y], 9, 1)
        pygame.draw.circle(screen, dark_blue, [x, y], 8)

    pygame.draw.circle(screen, black,[getx(points[0], points[1], midpoints[0][1] - 75),  midpoints[0][1] - 75], 51, 2)
    pygame.draw.circle(screen, pink,[getx(points[0], points[1], midpoints[0][1] - 75),  midpoints[0][1] - 75], 50)
    pygame.draw.circle(screen, black,[getx(points[0], points[1], midpoints[0][1] + 75),  midpoints[0][1] + 75], 51, 2)
    pygame.draw.circle(screen, pink,[getx(points[0], points[1], midpoints[0][1] + 75),  midpoints[0][1] + 75], 50)
    pygame.draw.circle(screen, black,[midpoints[1][0] + 75, gety(points[1], points[2], midpoints[1][0] + 75)], 51, 2)
    pygame.draw.circle(screen, pink,[midpoints[1][0] + 75, gety(points[1], points[2], midpoints[1][0] + 75)], 50)
    pygame.draw.circle(screen, black,[midpoints[1][0] - 75, gety(points[1], points[2], midpoints[1][0] - 75)], 51, 2)
    pygame.draw.circle(screen, pink,[midpoints[1][0] - 75, gety(points[1], points[2], midpoints[1][0] - 75)], 50)
    pygame.draw.circle(screen, black,[midpoints[2][0] - 75, gety(points[2], points[0], midpoints[2][0] - 75)], 51, 2)
    pygame.draw.circle(screen, pink,[midpoints[2][0] - 75, gety(points[2], points[0], midpoints[2][0] - 75)], 50)
    pygame.draw.circle(screen, black,[midpoints[2][0] + 75, gety(points[2], points[0], midpoints[2][0] + 75)], 51, 2)
    pygame.draw.circle(screen, pink,[midpoints[2][0] + 75, gety(points[2], points[0], midpoints[2][0] + 75)], 50)

    if i < first:
        pygame.draw.circle(screen, black, [center[0]-50, center[1]], 20, 2)
        pygame.draw.circle(screen, black, [center[0]+50/math.sqrt(2), center[1]+50/math.sqrt(2)], 20, 2)
        pygame.draw.circle(screen, black, [center[0]+50, center[1]], 20, 2)
        pygame.draw.circle(screen, black, [center[0]-50/math.sqrt(2), center[1]-50/math.sqrt(2)], 20, 2)
        pygame.draw.circle(screen, black, [center[0], center[1]-50], 20, 2)
        pygame.draw.circle(screen, black, [center[0]+50/math.sqrt(2), center[1]-50/math.sqrt(2)], 20, 2)
        pygame.draw.circle(screen, black, [center[0], center[1]+50], 20, 2)
        pygame.draw.circle(screen, black, [center[0]-50/math.sqrt(2), center[1]+50/math.sqrt(2)], 20, 2)

        pygame.draw.circle(screen, gray, [center[0]-50, center[1]], 19)
        pygame.draw.circle(screen, gray, [center[0]+50/math.sqrt(2), center[1]+50/math.sqrt(2)], 19)
        pygame.draw.circle(screen, gray, [center[0]+50, center[1]], 19)
        pygame.draw.circle(screen, gray, [center[0]-50/math.sqrt(2), center[1]-50/math.sqrt(2)], 19)
        pygame.draw.circle(screen, gray, [center[0], center[1]-50], 19)
        pygame.draw.circle(screen, gray, [center[0]+50/math.sqrt(2), center[1]-50/math.sqrt(2)], 19)
        pygame.draw.circle(screen, gray, [center[0], center[1]+50], 19)
        pygame.draw.circle(screen, gray, [center[0]-50/math.sqrt(2), center[1]+50/math.sqrt(2)], 19)

        dx1 = random.uniform(center[0]-30, center[0]-27)
        dy1 = random.uniform(center[1]-27, center[1]-24)
        dx2 = random.uniform(center[0]-3, center[0])
        dy2 = random.uniform(center[1], center[1]+3)
        dx3 = random.uniform(center[0]+2, center[0]+5)
        dy3 = random.uniform(center[1]-20, center[1]-17)

        pygame.draw.ellipse(screen, black, [[dx1-2, dy1-2], [32, 17]], 2)
        pygame.draw.ellipse(screen, maroon, [[dx1, dy1], [30, 15]])
        pygame.draw.ellipse(screen, black, [[dx2-2, dy2-2], [32, 17]], 2)
        pygame.draw.ellipse(screen, maroon, [[dx2, dy2], [30, 15]])
        pygame.draw.ellipse(screen, black, [[dx3-2, dy3-2], [32, 17]], 2)
        pygame.draw.ellipse(screen, maroon, [[dx3, dy3], [30, 15]])

    elif first <= i < second:
        if brk == 0:
            pygame.draw.circle(screen, black, [center[0]-50/math.sqrt(2), center[1]+50/math.sqrt(2)], 20, 2)
            pygame.draw.circle(screen, black, [center[0]-50, center[1]], 20, 2)
            pygame.draw.circle(screen, black, [center[0]+40+50/math.sqrt(2), center[1]-50/math.sqrt(2)], 20, 2)
            pygame.draw.circle(screen, black, [center[0]-50/math.sqrt(2), center[1]-50/math.sqrt(2)], 20, 2)
            pygame.draw.circle(screen, black, [center[0], center[1]-50], 20, 2)
            pygame.draw.circle(screen, black, [center[0]+50/math.sqrt(2), center[1]-50/math.sqrt(2)], 20, 2)
            pygame.draw.circle(screen, black, [center[0]+40, center[1]+50], 20, 2)
            pygame.draw.circle(screen, black, [center[0], center[1]+50], 20, 2)
            
            pygame.draw.circle(screen, gray, [center[0]-50, center[1]], 19)
            pygame.draw.circle(screen, gray, [center[0]+40+50/math.sqrt(2), center[1]-50/math.sqrt(2)], 19)
            pygame.draw.circle(screen, gray, [center[0]-50/math.sqrt(2), center[1]-50/math.sqrt(2)], 19)
            pygame.draw.circle(screen, gray, [center[0], center[1]-50], 19)
            pygame.draw.circle(screen, gray, [center[0]+50/math.sqrt(2), center[1]-50/math.sqrt(2)], 19)
            pygame.draw.circle(screen, gray, [center[0]-50/math.sqrt(2), center[1]+50/math.sqrt(2)], 19)
            pygame.draw.circle(screen, gray, [center[0], center[1]+50], 19)
            pygame.draw.circle(screen, gray, [center[0]+40, center[1]+50], 19)
        elif brk == 1:
            pygame.draw.circle(screen, black, [center[0]-50/math.sqrt(2), center[1]+50/math.sqrt(2)], 20, 2)
            pygame.draw.circle(screen, black, [center[0]-50, center[1]], 20, 2)
            pygame.draw.circle(screen, black, [center[0]+50, center[1]], 20, 2)
            pygame.draw.circle(screen, black, [center[0]-50/math.sqrt(2), center[1]-50/math.sqrt(2)], 20, 2)
            pygame.draw.circle(screen, black, [center[0], center[1]-50], 20, 2)
            pygame.draw.circle(screen, black, [center[0]+50/math.sqrt(2), center[1]-50/math.sqrt(2)], 20, 2)
            pygame.draw.circle(screen, black, [center[0]-50/math.sqrt(2), center[1]+40+50/math.sqrt(2)], 20, 2)
            pygame.draw.circle(screen, black, [center[0]+50, center[1]+40], 20, 2)
            
            pygame.draw.circle(screen, gray, [center[0]-50, center[1]], 19)
            pygame.draw.circle(screen, gray, [center[0]+50, center[1]], 19)
            pygame.draw.circle(screen, gray, [center[0]-50/math.sqrt(2), center[1]-50/math.sqrt(2)], 19)
            pygame.draw.circle(screen, gray, [center[0], center[1]-50], 19)
            pygame.draw.circle(screen, gray, [center[0]+50/math.sqrt(2), center[1]-50/math.sqrt(2)], 19)
            pygame.draw.circle(screen, gray, [center[0]-50/math.sqrt(2), center[1]+50/math.sqrt(2)], 19)
            pygame.draw.circle(screen, gray, [center[0]+50, center[1]+40], 19)
            pygame.draw.circle(screen, gray, [center[0]-50/math.sqrt(2), center[1]+40+50/math.sqrt(2)], 19)
        else:
            pygame.draw.circle(screen, black, [center[0]-50, center[1]], 20, 2)
            pygame.draw.circle(screen, black, [center[0]+50/math.sqrt(2), center[1]+50/math.sqrt(2)], 20, 2)
            pygame.draw.circle(screen, black, [center[0]+50, center[1]], 20, 2)
            pygame.draw.circle(screen, black, [center[0]-50, center[1]-40], 20, 2)
            pygame.draw.circle(screen, black, [center[0]+50/math.sqrt(2), center[1]-40-50/math.sqrt(2)], 20, 2)
            pygame.draw.circle(screen, black, [center[0]+50/math.sqrt(2), center[1]-50/math.sqrt(2)], 20, 2)
            pygame.draw.circle(screen, black, [center[0], center[1]+50], 20, 2)
            pygame.draw.circle(screen, black, [center[0]-50/math.sqrt(2), center[1]+50/math.sqrt(2)], 20, 2)

            pygame.draw.circle(screen, gray, [center[0]-50, center[1]], 19)
            pygame.draw.circle(screen, gray, [center[0]+50/math.sqrt(2), center[1]+50/math.sqrt(2)], 19)
            pygame.draw.circle(screen, gray, [center[0]+50, center[1]], 19)
            pygame.draw.circle(screen, gray, [center[0]-50, center[1]-40], 19)
            pygame.draw.circle(screen, gray, [center[0]+50/math.sqrt(2), center[1]-40-50/math.sqrt(2)], 19)
            pygame.draw.circle(screen, gray, [center[0]+50/math.sqrt(2), center[1]-50/math.sqrt(2)], 19)
            pygame.draw.circle(screen, gray, [center[0], center[1]+50], 19)
            pygame.draw.circle(screen, gray, [center[0]-50/math.sqrt(2), center[1]+50/math.sqrt(2)], 19)

        for z in d1:
            if z[0] != 0:
                if z[2] == []:
                    dx1 = (center[0] - 28.5) + 28.5/z[0]
                    dy1 = (center[1] - 25.5) + 75.5/z[0]
                    z[2].append([dx1, dy1])
                    z[0] = z[0] - 1
                else:
                    dx1 = (z[2][i - (first+1)][0]) + (center[0] - z[2][i - (first+1)][0])/z[0]
                    dy1 = (z[2][i - (first+1)][1]) + (center[0] + 50 - z[2][i - (first+1)][1])/z[0]
                    z[2].append([dx1, dy1])
                    z[0] = z[0] - 1
                pygame.draw.ellipse(screen, black, [[dx1-2, dy1-2], [32, 17]], 2)
                pygame.draw.ellipse(screen, maroon, [[dx1, dy1], [30, 15]])
            elif z[1] != 0 and z[0] == 0:
                dx1 = 640
                dy1 = 360
                if z[3] == False and z[4] == False and z[5] == False:
                    dx1 = (z[2][i - (first+1)][0]) + random.randint(-10, 10)
                    dy1 = (z[2][i - (first+1)][1]) + random.randint(-10, 10)
                if dx1 > 1280:
                    dx1 = dx1 - (dx1 - (1280+random.randint(1, 6)))
                elif dx1 < 0:
                    dx1 = random.randint(1, 6)
                if dy1 > 720:
                    dy1 = dy1 - (dy1 - (720 + random.randint(1, 6)))
                elif dy1 < 0:
                    dy1 = random.randint(1, 6)

                for v in range(nPoints):
                    q = v + 1
                    dr = 1
                    if q >= nPoints:
                        q = 0
                    if v == 0:
                        dr = -1
                    point = checkLine(points[v], points[q], [dx1, dy1], dr)
                    dx1 = point[0]
                    dy1 = point[1]

                    if blocked[v] == True:
                        #point = checkGate(points[v], points[q], midpoints[v], [dx1, dy1])
                        #dx1 = point[0]
                        #dy1 = point[1]
                        z[v+3] = False
                    else:
                        dx1, dy1 = tryBlock(points[v], points[q], midpoints[v], dx1, dy1, z, v, i)
                z[2].append([dx1, dy1])
                if z[1] == 0 and z[3] == True:
                    blocked[0] = True
                if z[1] == 0 and z[4] == True:
                    blocked[1] = True
                if z[1] == 0 and z[5] == True:
                    blocked[2] = True
                pygame.draw.ellipse(screen, black, [[dx1-2, dy1-2], [32, 17]], 2)
                pygame.draw.ellipse(screen, maroon, [[dx1, dy1], [30, 15]])
            else:
                for v in range(nPoints):
                    if z[v+3] == True:
                        pygame.draw.ellipse(screen, black, [[midpoints[v][0]-2, midpoints[v][1]-2], [32, 17]], 2)
                        pygame.draw.ellipse(screen, maroon, [[midpoints[v][0], midpoints[v][1]], [30, 15]])

        for z in d2:
            if z[0] != 0:
                if z[2] == []:
                    dx1 = (center[0] - 1.5) + 1.5/z[0]
                    dy1 = (center[1] + 1.5) + 48.5/z[0]
                    z[2].append([dx1, dy1])
                    z[0] = z[0] - 1
                else:
                    dx1 = (z[2][i - (first+1)][0]) + (center[0] - z[2][i - (first+1)][0])/z[0]
                    dy1 = (z[2][i - (first+1)][1]) + (center[0] + 50 - z[2][i - (first+1)][1])/z[0]
                    z[2].append([dx1, dy1])
                    z[0] = z[0] - 1
                pygame.draw.ellipse(screen, black, [[dx1-2, dy1-2], [32, 17]], 2)
                pygame.draw.ellipse(screen, maroon, [[dx1, dy1], [30, 15]])
            elif z[1] != 0 and z[0] == 0:
                dx1 = 566
                dy1 = 521
                if z[3] == False and z[4] == False and z[5] == False:
                    dx1 = (z[2][i - (first+1)][0]) + random.randint(-10, 10)
                    dy1 = (z[2][i - (first+1)][1]) + random.randint(-10, 10)
                if dx1 > 1280:
                    dx1 = dx1 - (dx1 - (1280+random.randint(1, 6)))
                elif dx1 < 0:
                    dx1 = random.randint(1, 6)
                if dy1 > 720:
                    dy1 = dy1 - (dy1 - (720 + random.randint(1, 6)))
                elif dy1 < 0:
                    dy1 = random.randint(1, 6)

                for v in range(nPoints):
                    q = v + 1
                    dr = 1
                    if q >= nPoints:
                        q = 0
                    if v == 1:
                        dr = -1
                    point = checkLine(points[v], points[q], [dx1, dy1], dr)
                    dx1 = point[0]
                    dy1 = point[1]

                    if blocked[v] == True:
                        point = checkGate(points[v], points[q], midpoints[v], [dx1, dy1])
                        dx1 = point[0]
                        dy1 = point[1]
                        z[v+3] = False
                    else:
                        dx1, dy1 = tryBlock(points[v], points[q], midpoints[v], dx1, dy1, z, v, i)
                z[2].append([dx1, dy1])
                if z[1] == 0 and z[3] == True:
                    blocked[0] = True
                elif z[1] == 0 and z[4] == True:
                    blocked[1] = True
                elif z[1] == 0 and z[5] == True:
                    blocked[2] = True
                pygame.draw.ellipse(screen, black, [[dx1-2, dy1-2], [32, 17]], 2)
                pygame.draw.ellipse(screen, maroon, [[dx1, dy1], [30, 15]])
            else:
                for v in range(nPoints):
                    if z[v+3] == True:
                        pygame.draw.ellipse(screen, black, [[midpoints[v][0]-2, midpoints[v][1]-2], [32, 17]], 2)
                        pygame.draw.ellipse(screen, maroon, [[midpoints[v][0], midpoints[v][1]], [30, 15]])

        for z in d3:
            if z[0] != 0:
                if z[2] == []:
                    dx1 = (center[0] + 1.5) - 1.5/z[0]
                    dy1 = (center[1] - 3) + 53/z[0]
                    z[2].append([dx1, dy1])
                    z[0] = z[0] - 1
                else:
                    dx1 = (z[2][i - (first+1)][0]) + (center[0] - z[2][i - (first+1)][0])/z[0]
                    dy1 = (z[2][i - (first+1)][1]) + (center[0] + 50 - z[2][i - (first+1)][1])/z[0]
                    z[2].append([dx1, dy1])
                    z[0] = z[0] - 1
                pygame.draw.ellipse(screen, black, [[dx1-2, dy1-2], [32, 17]], 2)
                pygame.draw.ellipse(screen, maroon, [[dx1, dy1], [30, 15]])
            elif z[1] != 0 and z[0] == 0:
                dx1 = 566
                dy1 = 521
                if z[3] == False and z[4] == False and z[5] == False:
                    dx1 = (z[2][i - (first+1)][0]) + random.randint(-10, 10)
                    dy1 = (z[2][i - (first+1)][1]) + random.randint(-10, 10)
                if dx1 > 1280:
                    dx1 = dx1 - (dx1 - (1280+random.randint(1, 6)))
                elif dx1 < 0:
                    dx1 = random.randint(1, 6)
                if dy1 > 720:
                    dy1 = dy1 - (dy1 - (720 + random.randint(1, 6)))
                elif dy1 < 0:
                    dy1 = random.randint(1, 6)

                for v in range(nPoints):
                    q = v + 1
                    dr = 1
                    if q >= nPoints:
                        q = 0
                    if v == 1:
                        dr = -1
                    point = checkLine(points[v], points[q], [dx1, dy1], dr)
                    dx1 = point[0]
                    dy1 = point[1]

                    if blocked[v] == True:
                        point = checkGate(points[v], points[q], midpoints[v], [dx1, dy1])
                        dx1 = point[0]
                        dy1 = point[1]
                        z[v+3] = False
                    else:
                        dx1, dy1 = tryBlock(points[v], points[q], midpoints[v], dx1, dy1, z, v, i)
                z[2].append([dx1, dy1])
                if z[1] == 0 and z[3] == True:
                    blocked[0] = True
                elif z[1] == 0 and z[4] == True:
                    blocked[1] = True
                elif z[1] == 0 and z[5] == True:
                    blocked[2] = True
                pygame.draw.ellipse(screen, black, [[dx1-2, dy1-2], [32, 17]], 2)
                pygame.draw.ellipse(screen, maroon, [[dx1, dy1], [30, 15]])
            else:
                for v in range(nPoints):
                    if z[v+3] == True:
                        pygame.draw.ellipse(screen, black, [[midpoints[v][0]-2, midpoints[v][1]-2], [32, 17]], 2)
                        pygame.draw.ellipse(screen, maroon, [[midpoints[v][0], midpoints[v][1]], [30, 15]])

    elif second <= i < third:
        pygame.draw.circle(screen, black, [center[0]-50, center[1]], 20, 2)
        pygame.draw.circle(screen, black, [center[0]+50, center[1]], 20, 2)
        pygame.draw.circle(screen, black, [center[0]-50/math.sqrt(2), center[1]-50/math.sqrt(2)], 20, 2)
        pygame.draw.circle(screen, black, [center[0], center[1]-50], 20, 2)
        pygame.draw.circle(screen, black, [center[0]+50/math.sqrt(2), center[1]-50/math.sqrt(2)], 20, 2)
        pygame.draw.circle(screen, black, [center[0]-50/math.sqrt(2), center[1]+50/math.sqrt(2)], 20, 2)

        pygame.draw.circle(screen, gray, [center[0]-50, center[1]], 19)
        pygame.draw.circle(screen, gray, [center[0]+50, center[1]], 19)
        pygame.draw.circle(screen, gray, [center[0]-50/math.sqrt(2), center[1]-50/math.sqrt(2)], 19)
        pygame.draw.circle(screen, gray, [center[0], center[1]-50], 19)
        pygame.draw.circle(screen, gray, [center[0]+50/math.sqrt(2), center[1]-50/math.sqrt(2)], 19)
        pygame.draw.circle(screen, gray, [center[0]-50/math.sqrt(2), center[1]+50/math.sqrt(2)], 19)

        x1 = pos1[0]["x"][i-second].item()
        y1 = pos1[0]["y"][i-second].item()
        if x1 > 1280:
            x1 = x1 - (x1 - (1280+random.randint(1, 6)))
        elif x1 < 0:
            x1 = random.randint(1, 6)
        if y1 > 720:
            y1 = y1 - (y1 - (720 + random.randint(1, 6)))
        elif y1 < 0:
            y1 = random.randint(1, 6)

        for v in range(nPoints):
            q = v + 1
            dr = 1
            if q >= nPoints:
                q = 0
            if v == 1:
                dr = -1
            point = checkLine(points[v], points[q], [x1, y1], dr)
            x1 = point[0]
            y1 = point[1]

            point = checkGate(points[v], points[q], midpoints[v], [x1, y1])
            x1 = point[0]
            y1 = point[1]

        x = pos2[0]["x"][i-second].item()
        y = pos2[0]["y"][i-second].item()
        if x > 1280:
            x = x - (x - (1280+random.randint(1, 6)))
        elif x < 0:
            x = random.randint(1, 6)
        if y > 720:
            y = y - (y - (720 + random.randint(1, 6)))
        elif y < 0:
            y = random.randint(1, 6)

        for v in range(nPoints):
            q = v + 1
            dr = 1
            if q >= nPoints:
                q = 0
            if v == 1:
                dr = -1
            point = checkLine(points[v], points[q], [x, y], dr)
            x = point[0]
            y = point[1]

            point = checkGate(points[v], points[q], midpoints[v], [x, y])
            x = point[0]
            y = point[1]
        
        pygame.draw.circle(screen, black, [x1, y1], 20, 1)
        pygame.draw.circle(screen, gray, [x1, y1], 19)
        pygame.draw.circle(screen, black, [x, y], 20, 1)
        pygame.draw.circle(screen, gray, [x, y], 19)

        for z in d1:
            if z[0] != 0:
                if z[2] == []:
                    dx1 = (center[0] - 28.5) + 28.5/z[0]
                    dy1 = (center[1] - 25.5) + 75.5/z[0]
                    z[2].append([dx1, dy1])
                    z[0] = z[0] - 1
                else:
                    dx1 = (z[2][i - (first+1)][0]) + (center[0] - z[2][i - (first+1)][0])/z[0]
                    dy1 = (z[2][i - (first+1)][1]) + (center[0] + 50 - z[2][i - (first+1)][1])/z[0]
                    z[2].append([dx1, dy1])
                    z[0] = z[0] - 1
                pygame.draw.ellipse(screen, black, [[dx1-2, dy1-2], [32, 17]], 2)
                pygame.draw.ellipse(screen, maroon, [[dx1, dy1], [30, 15]])
            elif z[1] != 0 and z[0] == 0:
                dx1 = 566
                dy1 = 521
                if z[3] == False and z[4] == False and z[5] == False:
                    dx1 = (z[2][i - (first+1)][0]) + random.randint(-10, 10)
                    dy1 = (z[2][i - (first+1)][1]) + random.randint(-10, 10)
                if dx1 > 1280:
                    dx1 = dx1 - (dx1 - (1280+random.randint(1, 6)))
                elif dx1 < 0:
                    dx1 = random.randint(1, 6)
                if dy1 > 720:
                    dy1 = dy1 - (dy1 - (720 + random.randint(1, 6)))
                elif dy1 < 0:
                    dy1 = random.randint(1, 6)

                for v in range(nPoints):
                    q = v + 1
                    dr = 1
                    if q >= nPoints:
                        q = 0
                    if v == 1:
                        dr = -1
                    point = checkLine(points[v], points[q], [dx1, dy1], dr)
                    dx1 = point[0]
                    dy1 = point[1]

                    if blocked[v] == True:
                        point = checkGate(points[v], points[q], midpoints[v], [dx1, dy1])
                        dx1 = point[0]
                        dy1 = point[1]
                        z[v+3] = False
                    else:
                        dx1, dy1 = tryBlock(points[v], points[q], midpoints[v], dx1, dy1, z, v, i)
                z[2].append([dx1, dy1])
                if z[1] == 0 and z[3] == True:
                    blocked[0] = True
                elif z[1] == 0 and z[4] == True:
                    blocked[1] = True
                elif z[1] == 0 and z[5] == True:
                    blocked[2] = True
                pygame.draw.ellipse(screen, black, [[dx1-2, dy1-2], [32, 17]], 2)
                pygame.draw.ellipse(screen, maroon, [[dx1, dy1], [30, 15]])
            else:
                for v in range(nPoints):
                    if z[v+3] == True:
                        pygame.draw.ellipse(screen, black, [[midpoints[v][0]-2, midpoints[v][1]-2], [32, 17]], 2)
                        pygame.draw.ellipse(screen, maroon, [[midpoints[v][0], midpoints[v][1]], [30, 15]])

        for z in d2:
            if z[0] != 0:
                if z[2] == []:
                    dx1 = (center[0] - 1.5) + 1.5/z[0]
                    dy1 = (center[1] + 1.5) + 48.5/z[0]
                    z[2].append([dx1, dy1])
                    z[0] = z[0] - 1
                else:
                    dx1 = (z[2][i - (first+1)][0]) + (center[0] - z[2][i - (first+1)][0])/z[0]
                    dy1 = (z[2][i - (first+1)][1]) + (center[0] + 50 - z[2][i - (first+1)][1])/z[0]
                    z[2].append([dx1, dy1])
                    z[0] = z[0] - 1
                pygame.draw.ellipse(screen, black, [[dx1-2, dy1-2], [32, 17]], 2)
                pygame.draw.ellipse(screen, maroon, [[dx1, dy1], [30, 15]])
            elif z[1] != 0 and z[0] == 0:
                dx1 = 566
                dy1 = 521
                if z[3] == False and z[4] == False and z[5] == False:
                    dx1 = (z[2][i - (first+1)][0]) + random.randint(-10, 10)
                    dy1 = (z[2][i - (first+1)][1]) + random.randint(-10, 10)
                if dx1 > 1280:
                    dx1 = dx1 - (dx1 - (1280+random.randint(1, 6)))
                elif dx1 < 0:
                    dx1 = random.randint(1, 6)
                if dy1 > 720:
                    dy1 = dy1 - (dy1 - (720 + random.randint(1, 6)))
                elif dy1 < 0:
                    dy1 = random.randint(1, 6)

                for v in range(nPoints):
                    q = v + 1
                    dr = 1
                    if q >= nPoints:
                        q = 0
                    if v == 1:
                        dr = -1
                    point = checkLine(points[v], points[q], [dx1, dy1], dr)
                    dx1 = point[0]
                    dy1 = point[1]

                    if blocked[v] == True:
                        point = checkGate(points[v], points[q], midpoints[v], [dx1, dy1])
                        dx1 = point[0]
                        dy1 = point[1]
                        z[v+3] = False
                    else:
                        dx1, dy1 = tryBlock(points[v], points[q], midpoints[v], dx1, dy1, z, v, i)
                z[2].append([dx1, dy1])
                if z[1] == 0 and z[3] == True:
                    blocked[0] = True
                elif z[1] == 0 and z[4] == True:
                    blocked[1] = True
                elif z[1] == 0 and z[5] == True:
                    blocked[2] = True
                pygame.draw.ellipse(screen, black, [[dx1-2, dy1-2], [32, 17]], 2)
                pygame.draw.ellipse(screen, maroon, [[dx1, dy1], [30, 15]])
            else:
                for v in range(nPoints):
                    if z[v+3] == True:
                        pygame.draw.ellipse(screen, black, [[midpoints[v][0]-2, midpoints[v][1]-2], [32, 17]], 2)
                        pygame.draw.ellipse(screen, maroon, [[midpoints[v][0], midpoints[v][1]], [30, 15]])

        for z in d3:
            if z[0] != 0:
                if z[2] == []:
                    dx1 = (center[0] + 1.5) - 1.5/z[0]
                    dy1 = (center[1] - 3) + 53/z[0]
                    z[2].append([dx1, dy1])
                    z[0] = z[0] - 1
                else:
                    dx1 = (z[2][i - (first+1)][0]) + (center[0] - z[2][i - (first+1)][0])/z[0]
                    dy1 = (z[2][i - (first+1)][1]) + (center[0] + 50 - z[2][i - (first+1)][1])/z[0]
                    z[2].append([dx1, dy1])
                    z[0] = z[0] - 1
                pygame.draw.ellipse(screen, black, [[dx1-2, dy1-2], [32, 17]], 2)
                pygame.draw.ellipse(screen, maroon, [[dx1, dy1], [30, 15]])
            elif z[1] != 0 and z[0] == 0:
                dx1 = 566
                dy1 = 521
                if z[3] == False and z[4] == False and z[5] == False:
                    dx1 = (z[2][i - (first+1)][0]) + random.randint(-10, 10)
                    dy1 = (z[2][i - (first+1)][1]) + random.randint(-10, 10)
                if dx1 > 1280:
                    dx1 = dx1 - (dx1 - (1280+random.randint(1, 6)))
                elif dx1 < 0:
                    dx1 = random.randint(1, 6)
                if dy1 > 720:
                    dy1 = dy1 - (dy1 - (720 + random.randint(1, 6)))
                elif dy1 < 0:
                    dy1 = random.randint(1, 6)

                for v in range(nPoints):
                    q = v + 1
                    dr = 1
                    if q >= nPoints:
                        q = 0
                    if v == 1:
                        dr = -1
                    point = checkLine(points[v], points[q], [dx1, dy1], dr)
                    dx1 = point[0]
                    dy1 = point[1]

                    if blocked[v] == True:
                        point = checkGate(points[v], points[q], midpoints[v], [dx1, dy1])
                        dx1 = point[0]
                        dy1 = point[1]
                        z[v+3] = False
                    else:
                        dx1, dy1 = tryBlock(points[v], points[q], midpoints[v], dx1, dy1, z, v, i)
                z[2].append([dx1, dy1])
                if z[1] == 0 and z[3] == True:
                    blocked[0] = True
                elif z[1] == 0 and z[4] == True:
                    blocked[1] = True
                elif z[1] == 0 and z[5] == True:
                    blocked[2] = True
                pygame.draw.ellipse(screen, black, [[dx1-2, dy1-2], [32, 17]], 2)
                pygame.draw.ellipse(screen, maroon, [[dx1, dy1], [30, 15]])
            else:
                for v in range(nPoints):
                    if z[v+3] == True:
                        pygame.draw.ellipse(screen, black, [[midpoints[v][0]-2, midpoints[v][1]-2], [32, 17]], 2)
                        pygame.draw.ellipse(screen, maroon, [[midpoints[v][0], midpoints[v][1]], [30, 15]])
 
    pygame.display.flip()
    fps.tick(60)

carr()

screen = pygame.display.set_mode(size)
fps = pygame.time.Clock()

i = 0
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    #update()
    render(i)
    if i < 10000:
        i = i+1
    else:
        sys.exit()