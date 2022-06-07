import requests
from fretboardgtr import ChordGtr

class Chord():

	def __init__(self):
		self.tuning = ['E','A','D','G','B','E']
		self.name = "C"
		self.displayName = "C major"
		self.quality = "major"
		self.tones = ["C", "E", "G"]
		self.colour = None
		self.position = ["x", "3", "2", "0", "1", "0",]
		self.fingering = [0,3,2,0,1,0]
		self.caged = "C"
		self.open = True
		self.json = None

	def userinput(self):
		self.tuning = input("Tuning [Default: Standard (EADGBe)]:") or self.tuning
		self.name = input("Chord name [Default: C]: ") or self.name

	def api_request(self):
		response = requests.get(f'https://api.uberchord.com/v1/chords?names={self.name}')
		self.json = response.json()[0]
		self.data_entry()

	def data_entry(self):
		self.displayName = self.name
		self.position = [int(i) for i in list(self.json["strings"].replace("X", "0").split(" "))]
		self.fingering = [int(i) for i in list(self.json["fingering"].replace("X", "0").split(" "))]
		self.tones = list(self.json["tones"].split(","))

	def print(self):
		print("\nResult:")
		print(f"{self.displayName}\n{self.fingering}\n{self.tones}")


def draw(chord):
	F=ChordGtr(fingering=chord.position,root=chord.name[0])
	F.customtuning(chord.tuning)
	F.draw()
	F.save()


if __name__ == "__main__":

	print("-----------------------------------------------------")
	print("Welcome to Guitar Chord Visualizer\n")
	print("Enter information below to initiate a chord search.")
	print("-----------------------------------------------------\n")

	chord = Chord()

	chord.userinput()
	chord.api_request()
	chord.print()

	draw(chord)