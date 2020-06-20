import math
from easy_vector import Vector

def ht(dx,dy):
	return (dx**2+dy**2)**0.5
def cosinus(dx,dy):
	return dx/ht(dx,dy)
def sinus(dx,dy):
	return dy/ht(dx,dy)

class Ray():
	def __init__(self,x,y,angle = (math.pi/4)):
		self.x = x
		self.y = y
		self.dir = Vector(math.cos(angle),math.sin(angle))
		#print(self.dir)
	
	def checkCollision(self,wall):
		self.x3,self.x4,self.x1,self.x2 = self.x, self.x+self.dir[0], wall.pos1[0], wall.pos2[0]
		self.y3,self.y4,self.y1,self.y2 = self.y, self.y+self.dir[1], wall.pos1[1], wall.pos2[1]
		self.denominator = (self.x1-self.x2)*(self.y3-self.y4)-(self.y1-self.y2)*(self.x3-self.x4)
		if self.denominator == 0:return False 
		t = ((self.x1-self.x3)*(self.y3-self.y4)-(self.y1-self.y3)*(self.x3-self.x4))/self.denominator
		u = -((self.x1-self.x2)*(self.y1-self.y3)-(self.y1-self.y2)*(self.x1-self.x3))/self.denominator
		if t>0 and t<1 and u>0: return True
		else:return False

	def findPoint(self,record,prevpoint):
		self.pointX = int(((self.x1*self.y2-self.y1*self.x2)*(self.x3-self.x4) - (self.x1-self.x2)*(self.x3*self.y4-self.y3*self.x4))/((self.x1-self.x2)*(self.y3-self.y4)-(self.y1-self.y2)*(self.x3-self.x4)))
		self.pointY = int(((self.x1*self.y2-self.y1*self.x2)*(self.y3-self.y4) - (self.y1-self.y2)*(self.x3*self.y4-self.y3*self.x4))/((self.x1-self.x2)*(self.y3-self.y4)-(self.y1-self.y2)*(self.x3-self.x4)))
		if record > ht(self.pointX-self.x,self.pointY-self.y):
			record = ht(self.pointX-self.x,self.pointY-self.y)
			return (self.pointX,self.pointY),record
		else:
			return (prevpoint),record

	def lookAt(self,point):
		self.dir = Vector(cosinus(point[0]-self.x,point[1]-self.y),sinus(point[0]-self.x,point[1]-self.y))

if __name__ == '__main__':
	r = Ray(4,6)