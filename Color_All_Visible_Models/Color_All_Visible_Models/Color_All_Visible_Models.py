import os
import unittest
import vtk, qt, ctk, slicer
from slicer.ScriptedLoadableModule import *
import logging
import numpy as np

#
# Color_All_Visible_Models
#

class Color_All_Visible_Models(ScriptedLoadableModule):
  """Uses ScriptedLoadableModule base class, available at:
  https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
  """

  def __init__(self, parent):
    ScriptedLoadableModule.__init__(self, parent)
    self.parent.title = "Color_All_Visible_Models" # TODO make this more human readable by adding spaces
    self.parent.categories = ["CustomExtensions"]
    self.parent.dependencies = []
    self.parent.contributors = ["Ryan Morrison"] # replace with "Firstname Lastname (Organization)"
    self.parent.helpText = """
This is an example of scripted loadable module bundled in an extension.
It performs a simple thresholding on the input volume and optionally captures a screenshot.
"""
    self.parent.helpText += self.getDefaultModuleDocumentationLink()
    self.parent.acknowledgementText = """
This file was originally developed by Jean-Christophe Fillion-Robin, Kitware Inc.
and Steve Pieper, Isomics, Inc. and was partially funded by NIH grant 3P41RR013218-12S1.
""" # replace with organization, grant and thanks.

#
# Color_All_Visible_ModelsWidget
#

class Color_All_Visible_ModelsWidget(ScriptedLoadableModuleWidget):
  """Uses ScriptedLoadableModuleWidget base class, available at:
  https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
  """

  def setup(self):
    ScriptedLoadableModuleWidget.setup(self)

    # Instantiate and connect widgets ...

    #
    # Parameters Area
    #
    parametersCollapsibleButton = ctk.ctkCollapsibleButton()
    parametersCollapsibleButton.text = "Update"
    self.layout.addWidget(parametersCollapsibleButton)
    # Layout within the dummy collapsible button
    parametersFormLayout = qt.QFormLayout(parametersCollapsibleButton)

    #
    # Red value
    #
    self.imageThresholdSliderWidget_Red = ctk.ctkSliderWidget()
    self.imageThresholdSliderWidget_Red.singleStep = 1
    self.imageThresholdSliderWidget_Red.minimum = 0
    self.imageThresholdSliderWidget_Red.maximum = 255
    self.imageThresholdSliderWidget_Red.value = 0
    parametersFormLayout.addRow("Red", self.imageThresholdSliderWidget_Red)

    #
    # Green value
    #
    self.imageThresholdSliderWidget_Green = ctk.ctkSliderWidget()
    self.imageThresholdSliderWidget_Green.singleStep = 1
    self.imageThresholdSliderWidget_Green.minimum = 0
    self.imageThresholdSliderWidget_Green.maximum = 255
    self.imageThresholdSliderWidget_Green.value = 0
    parametersFormLayout.addRow("Green", self.imageThresholdSliderWidget_Green)

    #
    # Blue value
    #
    self.imageThresholdSliderWidget_Blue = ctk.ctkSliderWidget()
    self.imageThresholdSliderWidget_Blue.singleStep = 1
    self.imageThresholdSliderWidget_Blue.minimum = 0
    self.imageThresholdSliderWidget_Blue.maximum = 255
    self.imageThresholdSliderWidget_Blue.value = 0
    parametersFormLayout.addRow("Blue", self.imageThresholdSliderWidget_Blue)

    #
    # Opacity value
    #
    self.imageThresholdSliderWidget_Opacity = ctk.ctkSliderWidget()
    self.imageThresholdSliderWidget_Opacity.singleStep = 0.01
    self.imageThresholdSliderWidget_Opacity.minimum = 0
    self.imageThresholdSliderWidget_Opacity.maximum = 1
    self.imageThresholdSliderWidget_Opacity.value = 0
    parametersFormLayout.addRow("Opacity", self.imageThresholdSliderWidget_Opacity)
    
    #
    # Apply Button
    #
    self.startButton = qt.QPushButton("Apply Color")
    self.startButton.toolTip = "Run the algorithm."
    self.startButton.enabled = True
    parametersFormLayout.addRow(self.startButton)
    # connections
    self.startButton.connect('clicked(bool)', self.onstartButton)

    
    # Add vertical spacer
    self.layout.addStretch(1)

    self.logic = Color_All_Visible_ModelsLogic()

  def cleanup(self):
    pass

  def onstartButton(self):
    red = int(self.imageThresholdSliderWidget_Red.value)
    green = int(self.imageThresholdSliderWidget_Green.value)
    blue = int(self.imageThresholdSliderWidget_Blue.value)
    opacity = int(self.imageThresholdSliderWidget_Blue.value)
    self.logic.applyColor(red,green,blue,opacity)

#
# Color_All_Visible_ModelsLogic
#

class Color_All_Visible_ModelsLogic(ScriptedLoadableModuleLogic):
  """This class should implement all the actual
  computation done by your module.  The interface
  should be such that other python code can import
  this class and make use of the functionality without
  requiring an instance of the Widget.
  Uses ScriptedLoadableModuleLogic base class, available at:
  https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
  """

  #
  # Code executed when button pressed
  #
  def applyColor(self,red,green,blue,opacity):
    print("Color applied: " + str(red) + "," + str(green) + "," + str(blue) + ", with opacity:" + str(opacity))

    modelDisplayableManager = None
    threeDViewWidget = slicer.app.layoutManager().threeDWidget(0)
    managers = vtk.vtkCollection()
    threeDViewWidget.getDisplayableManagers(managers)
    for i in range(managers.GetNumberOfItems()):
      obj = managers.GetItemAsObject(i)
      if obj.IsA('vtkMRMLModelDisplayableManager'):
        modelDisplayableManager = obj
        break
    if modelDisplayableManager is None:
      logging.error('Failed to find the model displayable manager')


    #TODO set color and opacity to all visible models      


class Color_All_Visible_ModelsTest(ScriptedLoadableModuleTest):
  """
  This is the test case for your scripted module.
  Uses ScriptedLoadableModuleTest base class, available at:
  https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
  """

  def setUp(self):
    """ Do whatever is needed to reset the state - typically a scene clear will be enough.
    """
    slicer.mrmlScene.Clear(0)

  def runTest(self):
    """Run as few or as many tests as needed here.
    """
    self.setUp()
    self.test_Color_All_Visible_Models1()

  def test_Color_All_Visible_Models1(self):
    """ Ideally you should have several levels of tests.  At the lowest level
    tests should exercise the functionality of the logic with different inputs
    (both valid and invalid).  At higher levels your tests should emulate the
    way the user would interact with your code and confirm that it still works
    the way you intended.
    One of the most important features of the tests is that it should alert other
    developers when their changes will have an impact on the behavior of your
    module.  For example, if a developer removes a feature that you depend on,
    your test should break so they know that the feature is needed.
    """

    self.delayDisplay("Starting the test")
    #
    # first, get some data
    #
    pass
