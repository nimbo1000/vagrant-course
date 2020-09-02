from onpit import Grader
from os.path import join, exists

class LabGrader(Grader):
	@Grader.addStep(name='step1')
	def step1(self, workingDir, inputCommand):
		if inputCommand == "docker -h":
			self.firstCommand1 = True
		if inputCommand == "docker ps":
			self.secondCommand1 = True
		if inputCommand == "docker images":
			self.thirdCommand1 = True
		if hasattr(self, 'firstCommand1') and hasattr(self, 'secondCommand1') and hasattr(self, 'thirdCommand1') and self.firstCommand1 and self.secondCommand1 and self.thirdCommand1:
			return True

	@Grader.addStep(name='step2')
	def step2(self, workingDir, inputCommand):
		if inputCommand == "docker pull docker/whalesay":
			self.firstCommand2 = True
		if inputCommand == "docker images" and hasattr(self, 'firstCommand2') and self.firstCommand2:
			self.secondCommand2 = True
		if hasattr(self, 'secondCommand2') and self.secondCommand2:
			return True

	@Grader.addStep(name='step3')
	def step3(self, workingDir, inputCommand):
		if inputCommand == "docker ps" and hasattr(self, 'thirdCommand1') and self.thirdCommand1:
			self.firstCommand3 = True
		if inputCommand == "docker run docker/whalesay cowsay hello-world":
			self.secondCommand3 = True
		if hasattr(self, 'firstCommand3') and hasattr(self, 'secondCommand3') and self.firstCommand3 and self.secondCommand3:
			return True
