#Copyright 2014 Andrew "HER0 01" Conrad
#
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.

from direct.showbase.ShowBase import ShowBase
from pandac.PandaModules import TextNode
from pandac.PandaModules import WindowProperties

class AntigoMe(ShowBase):
	
	def __init__(self):
		ShowBase.__init__(self)
		
		self.decisions = []
		self.isReady = False
		self.red = 0
		self.messageNode = TextNode("Message")
		self.choiceOneNode = TextNode("ChoiceOne")
		self.choiceTwoNode = TextNode("ChoiceTwo")
		self.instructionsNode = TextNode("Instructions")
		
		self.messageNode.setText('"Antigone, stop screaming!"')
		self.choiceOneNode.setText("[stop]")
		self.choiceTwoNode.setText("[scream louder]")
		self.instructionsNode.setText("Use the arrow keys to make a choice.")
		
		base.setBackgroundColor(self.red, 0, 0)
		base.disableMouse()
		props = WindowProperties()
		props.setTitle("Antigo Me")
		base.win.requestProperties(props)
		
		self.textDisplay()
		self.showText()
		
		self.isReady = True
		
		self.accept("arrow_left", self.decision, [0])
		self.accept("arrow_right", self.decision, [1])

	def decision(self, choice):
		if self.isReady:
			self.decisions.append(choice)
			color = base.getBackgroundColor()
			self.red += color.getW() + .045
			self.showText()
		
	def showText(self, elipse=False):
		self.isReady = False
		base.setBackgroundColor(self.red, 0, 0)
		self.messageNode.setTextColor(1, 1, 1, 1)	
		self.choiceOneNode.setTextColor(.88, .88, .88, 1)
		self.choiceTwoNode.setTextColor(.88, .88, .88, 1)
		self.instructionsNode.setTextColor(1, 1, 1, .5)
		
		last = len(self.decisions) - 1
		if last > -1:
			isRight = self.decisions[last]
		
		if last == 0:
			if isRight:
				self.messageNode.setText("You hear your sister, Ismene, sigh. " + '"Whatever."')
			else:
				self.messageNode.setText("You open your eyes to see your \nsister, Ismene, attempting a smile.")
			self.choiceOneNode.setText("My brothers dying in battle against \n each other is happiness compared to \n one, Polynices, being left unburried.")
			self.choiceTwoNode.setText("[continue screaming]")
			self.isReady = True
			
		if last == 1:
			if self.decisions == [0, 0]:
				self.messageNode.setText('"We will get throught this. I promise."' + "\nIsmene leaves.")
			else:
				self.messageNode.setText('"Just try to be strong. It is what' + "\nPolynices would want." + '"' + "\nIsmene leaves.")
			self.choiceOneNode.setText("[try to sleep]")
			self.choiceTwoNode.setText("[stay awake]")
			self.isReady = True
			
		if last == 2:
			self.choiceOneNode.setText("")
			self.choiceTwoNode.setText("")
			if self.decisions == [1, 1, 1]:
				scream = "You scream into your pillow. \n"
			else:
				scream = ""
			if isRight:
				self.messageNode.setText(scream + "You are unable to think of a word\nto describe your anguish. Fuming under\nyour covers, sleep grabs hold of you...")
			else:
				self.messageNode.setText("You roll over in your bed, happy\nto be alone. You bury yourself in the\nsheets and drift to sleep...")
			self.instructionsNode.setTextColor(1, 1, 1, 0)
			taskMgr.doMethodLater(6.5, self.showText, 'showText', [True])
			if elipse == True:
				self.messageNode.setText("A dark, horned figure approaches. Suddenly, \nit lurches towards you.")
				self.choiceOneNode.setText("[run]")
				self.choiceTwoNode.setText("[attack]")
				self.instructionsNode.setTextColor(1, 1, 1, .5)
				self.isReady = True
		
		if last == 3:
			self.choiceOneNode.setText("")
			self.choiceTwoNode.setText("")
			if isRight:
				self.messageNode.setText("You realize that your arms are like a baby's...")
			else:
				self.messageNode.setText("Your legs feel unusually weak...")
			self.instructionsNode.setTextColor(1, 1, 1, .0)
			taskMgr.doMethodLater(4, self.showText, 'showText', [True])
			if elipse == True:
				self.messageNode.setText("Just before it grabs you, you wake up \nin a cold sweat. You hear the murmur of the \ncrier outside in the agorn. " + '"Remember the words \nof our king, Kreon! The traitor is to be \nleft unburried, punishable by death."')
				self.choiceOneNode.setText("[close the door to your home]")
				self.choiceTwoNode.setText("[run outside and scream]")
				self.instructionsNode.setTextColor(1, 1, 1, .5)
				self.isReady = True
		
		if last == 4:
			night = '\nShe pulls you close, speaking quickly\nand quietly. "I know what you did last night. You\nburried Polynices! Why, Antigone?"'
			if isRight:
				self.messageNode.setText("Everyone turns and stares at you, silent.\nIsmene bursts out of the house and rushes you in." + night)
			else:
				self.messageNode.setText("As you shut the door, Ismene rushes in the room." + night)
			if self.decisions[3] == 0:
				self.choiceOneNode.setText('"I told you I would do it."')
				self.choiceTwoNode.setText('[lie] "What are you talking about?"')
			else:
				self.choiceOneNode.setText('"You refused to help me!"')
				self.choiceTwoNode.setText('"Get away from me."')
			self.instructionsNode.setTextColor(1, 1, 1, .5)
			self.isReady = True
		
		if last == 5:
			self.messageNode.setText('Isemene looks grave. "You are going to die."')
			self.choiceOneNode.setText("")
			self.choiceTwoNode.setText("")
			self.instructionsNode.setTextColor(1, 1, 1, 0)
			taskMgr.doMethodLater(4, self.showText, 'showText', [True])
			if elipse == True:
				self.messageNode.setText("The End")
		
	def textDisplay(self):
		messagePath = aspect2d.attachNewNode(self.messageNode)
		messagePath.setScale(0.1)
		messagePath.setPos(-1.1, 0, 0.8)
		
		choiceOnePath = aspect2d.attachNewNode(self.choiceOneNode)
		choiceOnePath.setScale(0.065)
		choiceOnePath.setPos(-1.3, 0, -0.2)
		
		choiceTwoPath = aspect2d.attachNewNode(self.choiceTwoNode)
		choiceTwoPath.setScale(0.065)
		choiceTwoPath.setPos(.1, 0, -0.2)
		
		instructionsPath = aspect2d.attachNewNode(self.instructionsNode)
		instructionsPath.setScale(0.05)
		instructionsPath.setPos(-.8, 0, -.8)

game = AntigoMe()
game.run()
