"""
Program: GUI_template.py
Chapter 8 Final Project
1/26/2024

**NOTE: The module breezypythongui.py MUST be in the same directory as this file for the app to run correctly!!!

GUI-based version of the Video Store app that prompts for the number of video rentals in pricing categories. Calculates and displays the grand total. 
"""

from breezypythongui import EasyFrame
from tkinter.font import Font
# Other imports go here

# Variables and Constants
NEW_COST = 3.50
OLD_COST = 2.00
DISCOUNT = 0.10

#Class header (class name will change project to project)
class VideoStore(EasyFrame):

	# Defintion of our classes' constructor method
	def __init__(self):
		# Call to the Easy Frame class constructor
		EasyFrame.__init__(self, title = "Video Store", width = 400, height = 300, resizable = False, background = "azure3")

		# Add various components to the window 
		self.addLabel(text = "Five Star Retro Video", row = 0, column = 0, sticky = "NSEW", columnspan = 2, background = "azure3", foreground = "lightskyblue4", font = Font(family = "elephant", size = 20))

		# Lable and entry field for the input
		self.addLabel(text = "New Rentals", row = 1, column = 0, background = "azure3", foreground = "lightblue4", font = "Georgia")
		self.newField = self.addIntegerField(value = 0, row = 1, column = 1)
		self.addLabel(text = "Old Rentals", row = 2, column = 0, background = "azure3", foreground = "lightblue4", font = "Georgia")
		self.oldField = self.addIntegerField(value = 0, row = 2, column = 1)

		# Label and entry field for the output 
		self.oldField.bind ("<Return>", lambda event: self.compute())

		self.computeButton = self.addButton(text = "Calculate", row = 3, column = 0, columnspan = 2, command = self.compute)
		self.computeButton["background"] = "Darkseagreen4"
		self.computeButton["foreground"] = "honeydew3"
		self.computeButton["width"] = 8
		self.computeButton["height"] = 1
		self.computeButton["font"] = "elephant"

		self.totalLabel = self.addLabel(text = "The total cost for this order is: ", row = 5, column = 0, columnspan = 2, background = "azure3", foreground = "lightskyblue4", font = "elephant")

		# Add discount checkbutton 
		self.discountCB = self.addCheckbutton(text = " Apply Ten Percent Discount", row = 4, column = 0, columnspan = 2)

		self.discountCB["background"] = "azure3"
		self.discountCB["foreground"] = "Darkseagreen4"
		self.discountCB["font"] = "Georgia"


	def compute(self):
		try:
			new_videos = self.newField.getNumber()
			old_videos = self.oldField.getNumber()

		except ValueError: 
			self.messageBox(title = "Error", message = "Please enter an integer.") 
			return

		# Calcultion 
		total = (NEW_COST * new_videos) + (OLD_COST * old_videos)

		# Apply discount if the checkbox is checked 
		if self.discountCB.isChecked():
			total *= (1 - DISCOUNT)

		# Display result in label 
		self.totalLabel["text"] = f"The total cost for this order is: ${total: .2f}"
	
	
# Global definition of the main() method 
def main():
	# Instantiate an object from the class into mainloop()
	VideoStore().mainloop()

# Global call to main() for program entry 
if __name__ == '__main__':
	main()