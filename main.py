import pygame as pg
import math,random,time
from ray import *
from wall import *
pg.init()
pg.time.Clock()

rays = []
for degree in range(450):
	degree *= 0.8
	radian = degree/360*2*math.pi
	rays.append(Ray(250,250,radian))
	pass
#print(f'{r.dir}; m = {r.m}; c = {r.c}'for r in rays)

walls = [Wall(0,0,0,500),Wall(0,500,500,500),Wall(0,0,500,0),Wall(500,0,500,500)]

for e in range(random.randint(1,10)):
	walls.append(Wall(random.randint(0,500),random.randint(0,500),random.randint(0,500),random.randint(0,500)))


window = pg.display.set_mode((500,500))

curT = time.time()
while True:
	
	for event in pg.event.get():
		if event.type == pg.QUIT:
			quit()

	window.fill((0,0,0))
	points = []
	for r in rays:
		r.x,r.y = pg.mouse.get_pos()
		record = 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
		point = (r.x,r.y)
		#pg.draw.line(window,(255,255,255),[r.x,r.y] ,[r.x+r.dir[0]*10,r.y+r.dir[1]*10],1)
		for w in walls:
			pg.draw.line(window,(255,255,255),w.pos1,w.pos2,1)
			if r.checkCollision(w): 
				point,record = r.findPoint(record,point)
				#print(point)
		try:
			pg.draw.line(window,(255,255,255,1),[r.x,r.y],point,1)
		except:print(None)
	'''
	for p in points:
		#pg.draw.circle(window,(0,100,0),p,5)
		pg.draw.line(window,(255,255,255),)
	'''
	pg.display.update()

	print(1/(time.time()-curT))
	curT = time.time()
