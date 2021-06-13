# Filename: thaiAlphaMCApp.py

"""thaiAlphaMCApp.py is simple app displaying Thai Characters using Python and PyQt5"""



# This simple app will display an audio clip along with five character images.
#  The user will play the audio clip and select the correct character.
# 
#  Audio is from thai-language.org, and the character images are 'handwritten'
#
#  The buttons will now require a while loop with an exit button

__version__ = '0.1'
__author__ = 'Sean Nomoto'

#################################################################
# import needed libraries, classes, functions
############################################################

from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QLabel
from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QHBoxLayout, QCheckBox
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtGui import QIcon, QPalette
from PyQt5.QtCore import Qt, QSize, QUrl 
from PyQt5.Qt import QPixmap, QFont, QCloseEvent, QPalette
from PyQt5 import QtCore
import os, sys, random 
from random import choice


#################################################################################
#    image png files
###################################################################################
# read in the png files of the alphabet
pics = os.listdir('AlphaPng/')

# attach 'AlphaPng' file names
for q in range(len(pics)):
	pics[q] = 'AlphaPng/' + pics[q]



#############################################################################
#  audio mp3 files
#############################################################################

# read in the mp3 files
clips = os.listdir('mp3Files/')

# attach 'mp3Files' file names
for i in range(len(clips)):
	clips[i] = 'mp3Files/' + clips[i]

# print list to console to be sure list has files
print(clips)


#############################################################
#  Main Application
#############################################################


class MainWindow(QMainWindow):
	def __init__(self):

		super().__init__()

########################################
# add media files to self
#########################################

		# include pics in self
		self.pics = pics
		self.clips = clips
		
		# print list of pngs in console
		print(self.pics)
		print(self.clips)

########################################
# window parameters and image display, create, media player
#########################################
		
		self.setWindowTitle("Thai Alphabet App")
		self.move(100,100)
		# self.setFixedSize(QSize(500,500))

		##### title for the app
		self.label_title = QLabel("ภาษาไทย: ฝึกหัด (Practice)")
		font = self.label_title.font()
		font.setPointSize(30)
		self.label_title.setFont(font)
		self.label_title.setAlignment(Qt.AlignCenter)

		##### view for the five characters 

		size = 250 # size of character images

		self.label1 = QLabel()
		self.q = list(range(len(clips)))
		print(self.q)
		pixmap1 = QPixmap(self.pics[self.q[0]])
		pixmap1 = pixmap1.scaled(size,size,QtCore.Qt.KeepAspectRatio)
		self.label1.setPixmap(pixmap1)

		self.label2 = QLabel()
		pixmap2 = QPixmap(self.pics[self.q[1]])
		pixmap2 = pixmap2.scaled(size,size,QtCore.Qt.KeepAspectRatio)
		self.label2.setPixmap(pixmap2)

		self.label3 = QLabel()
		pixmap3 = QPixmap(self.pics[self.q[2]])
		pixmap3 = pixmap3.scaled(size,size,QtCore.Qt.KeepAspectRatio)
		self.label3.setPixmap(pixmap3)
		
		self.label4 = QLabel()
		pixmap4 = QPixmap(self.pics[self.q[3]])
		pixmap4 = pixmap4.scaled(size,size,QtCore.Qt.KeepAspectRatio)
		self.label4.setPixmap(pixmap4)
		
		self.label5 = QLabel()
		pixmap5 = QPixmap(self.pics[self.q[4]])
		pixmap5 = pixmap5.scaled(size,size,QtCore.Qt.KeepAspectRatio)
		self.label5.setPixmap(pixmap5)
		

		##### create media player object
		self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.StreamPlayback)


		##### MC section instruction 
		self.MC = QLabel('Instructions: Press Play Audio and Select the Correct character (a, b, c, d, or e). SELECT ONLY ONE.')

		##### Checkbox widgets for user to select answer
		self.ansA = QCheckBox('(a)')
		self.ansB = QCheckBox('(b)')
		self.ansC = QCheckBox('(c)')
		self.ansD = QCheckBox('(d)')
		self.ansE = QCheckBox('(e)')




		##### simple Qlabels for labeling each image
		self.labela = QLabel('(a)')
		self.labela.setAlignment(Qt.AlignCenter)
		self.labelb = QLabel('(b)')
		self.labelb.setAlignment(Qt.AlignCenter)
		self.labelc = QLabel('(c)')
		self.labelc.setAlignment(Qt.AlignCenter)
		self.labeld = QLabel('(d)')
		self.labeld.setAlignment(Qt.AlignCenter)
		self.labele = QLabel('(e)')
		self.labele.setAlignment(Qt.AlignCenter)

		
########################################
# buttons
#########################################
		
		# font size for Buttons
		self.setFont(QFont('Times', 15))

		# Exit Button
		self.button_exit = QPushButton("แล้ว (Exit)")

		# # Previous Button
		# self.button_prev = QPushButton("แล้ว (Previous)")
				
		# Next Button
		self.button_next = QPushButton("หน้า (Next)")
		
		#Play audio button
		self.button_play = QPushButton("เล่น (Play Audio)")
		self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(clips[0])))
		self.button_play.setEnabled(True)

		# Submit Answer Button
		self.button_submit = QPushButton('Submit Answer')

########################################
# signals
#########################################

		# self.ansA.isChecked.connect(self.a_checked)
		# self.ansB.isChecked.connect(self.b_checked)
		# self.ansC.isChecked.connect(self.c_checked)
		# self.ansD.isChecked.connect(self.d_checked)
		# self.ansE.isChecked.connect(self.e_checked)
		self.button_exit.clicked.connect(self.button_clicked_exit)
		# self.button_prev.clicked.connect(self.button_clicked_prev)
		self.button_next.clicked.connect(self.button_clicked_next)
		self.button_play.clicked.connect(self.play_video)
		self.button_submit.clicked.connect(self.button_clicked_submit)

########################################
# layouts for widgets
#########################################
		

		# vertical layout for pics and button below
		self.layout_1 = QVBoxLayout()

		# add the label_title to the widget in  layout1 Vbox
		self.layout_1.addWidget(self.label_title)

		# horizontal layout for buttons, goes into VBoxLayout
		self.layout_2 = QHBoxLayout()
		# self.layout_2.addWidget(self.button_prev)
		self.layout_2.addWidget(self.button_next)

		# we add the label images widget to layout 3 in HBox
		self.layout_3 = QHBoxLayout()
		self.layout_3.addWidget(self.label1)
		self.layout_3.addWidget(self.label2)
		self.layout_3.addWidget(self.label3)
		self.layout_3.addWidget(self.label4)
		self.layout_3.addWidget(self.label5)

		
		# put the MC labels a,b,c,d,e into a horizontal layout
		
		self.layout_4 = QHBoxLayout()
		self.layout_4.addWidget(self.labela)
		self.layout_4.addWidget(self.labelb)
		self.layout_4.addWidget(self.labelc)
		self.layout_4.addWidget(self.labeld)
		self.layout_4.addWidget(self.labele)

		# vertical layout for the checkboxes
		self.layout_5 = QVBoxLayout()
		self.layout_5.addWidget(self.ansA)
		self.layout_5.addWidget(self.ansB)
		self.layout_5.addWidget(self.ansC)
		self.layout_5.addWidget(self.ansD)
		self.layout_5.addWidget(self.ansE)

		# add the images to the main layout
		self.layout_1.addLayout(self.layout_3)

		# add the label for the images to the main layout
		self.layout_1.addLayout(self.layout_4)

		# we add the layout 2 for the buttons to VBox
		self.layout_1.addLayout(self.layout_2)

		# we add the play button widget to the Vbox layout 1
		self.layout_1.addWidget(self.button_play)

		# we add the play button widget to the Vbox layout 1
		self.layout_1.addWidget(self.MC)

		# add the checkbox widget layout here
		self.layout_1.addLayout(self.layout_5)

		# add the submit button here
		self.layout_1.addWidget(self.button_submit)

		# we add the play button widget to the Vbox layout 1
		self.layout_1.addWidget(self.button_exit)

		# set up the mainwindow widget
		widget = QWidget()
		# now set the layout1 VBox for the main widget
		widget.setLayout(self.layout_1)

		self.setCentralWidget(widget)

########################################
# slots
#########################################

		# slots (functions) that connect buttons' signals	
	#################### Exit Button
	def button_clicked_exit(self):
		self.close()

	#######################  Prev Button
	# def button_clicked_prev(self):
	# 	self.q = (self.q - 1) % 44
	# 	new_pic = self.pics[self.q]  
	# 	self.label1.setPixmap(QPixmap(new_pic))
	# 	new_clip = self.clips[self.q]
	# 	self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(new_clip)))
	# 	print(self.q)

	########################### Next Button
	def button_clicked_next(self,q):
		newq = random.sample(self.q, 5)
		size = 250
		new_pic0 = QPixmap(self.pics[newq[0]])  
		new_pic0 = new_pic0.scaled(size,size,QtCore.Qt.KeepAspectRatio)
		self.label1.setPixmap(new_pic0)
		# new_clip0 = self.clips[newq[0]]
		# self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(new_clip0)))

		new_pic1 = QPixmap(self.pics[newq[1]])  
		new_pic1 = new_pic1.scaled(size,size,QtCore.Qt.KeepAspectRatio)
		self.label2.setPixmap(new_pic1)
		# new_clip1 = self.clips[newq[1]]
		# self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(new_clip1)))

		new_pic2 = QPixmap(self.pics[newq[2]])  
		new_pic2 = new_pic2.scaled(size,size,QtCore.Qt.KeepAspectRatio)
		self.label3.setPixmap(new_pic2)
		# new_clip2 = self.clips[newq[2]]
		# self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(new_clip2)))

		new_pic3 = QPixmap(self.pics[newq[3]])  
		new_pic3 = new_pic3.scaled(size,size,QtCore.Qt.KeepAspectRatio)
		self.label4.setPixmap(new_pic3)
		# new_clip3 = self.clips[newq[3]]
		# self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(new_clip3)))


		new_pic4 = QPixmap(self.pics[newq[4]])  
		new_pic4 = new_pic4.scaled(size,size,QtCore.Qt.KeepAspectRatio)
		self.label5.setPixmap(new_pic4)
		# new_clip4 = self.clips[newq[4]]
		# self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(new_clip4)))

		qclip = choice(newq)
		new_clip = self.clips[qclip]
		self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(new_clip)))
		
		index = newq.index(qclip)
		self.ANS = index

		self.ansA.setCheckState(False)
		self.ansB.setCheckState(False)
		self.ansC.setCheckState(False)
		self.ansD.setCheckState(False)
		self.ansE.setCheckState(False)

		
		print(newq)
		print(qclip)
		print(index)

	# ###################### Check Boxes
	# def a_checked(self):

	def button_clicked_submit(self, index):
		pos = 1
		index = self.ANS
		self.a = self.ansA.checkState()
		self.b = self.ansB.checkState()
		self.c = self.ansC.checkState()
		self.d = self.ansD.checkState()
		self.e = self.ansE.checkState()
		ans = [self.a, self.b, self.c, self.d, self.e]
		for i in range(len(ans)):
			if self.a == 2:
				pos = ans.index(self.a)
			elif self.b == 2:
				pos = ans.index(self.b)
			elif self.c == 2:
				pos = ans.index(self.c)
			elif self.d == 2:
				pos = ans.index(self.d)
			elif self.e == 2:
				pos = ans.index(self.e)
		if pos == index:
			print('Correct!')
		else:
			print('Error or Incorrect!')
		print(index)
		print(ans)

	#######################  Play Audio Button
	def play_video(self):
		if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
			self.mediaPlayer.pause()

		else:
			self.mediaPlayer.play()

########################################
# Main application controls
#########################################

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()