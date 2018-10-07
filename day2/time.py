import os
import sys 

class Time():
	def __init__(self, h, m, s):
		self._hours = h
		self._minutes = m
		self._seconds = s
		self._adjust()

	def set_hours(self, h):
		self._hours = h

	def set_minutes( self, m ):
		self._minutes = m
		
	def set_seconds( self, s ):
		self._seconds = s

	def display_time(self):
		print "time : %s %s %s" % (self._hours, self._minutes, self._seconds)

	def addtime(self, h, m, s):
		self.set_hours(h)
		self.set_minutes(m)
		self.set_seconds(s)
		self._adjust()

	def _adjust(self):
		while(self._seconds > 60):
			self._seconds -= 60
			self._minutes += 1
		while(self._minutes > 60):
			self._minutes -= 60
			self._hours += 1
		while(self._hours > 24):
			self._hours -= 24
			#days here

def main():
	t = Time(3, 7, 3);
	t.display_time()
	t.addtime( 4, 3, 2);
	t.display_time()

main()

