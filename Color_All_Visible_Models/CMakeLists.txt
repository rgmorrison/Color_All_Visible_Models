cmake_minimum_required(VERSION 3.5)

project(Color_All_Visible_Models)

#-----------------------------------------------------------------------------
# Extension meta-information
set(EXTENSION_HOMEPAGE "http://slicer.org/slicerWiki/index.php/Documentation/Nightly/Extensions/Color_All_Visible_Models")
set(EXTENSION_CATEGORY "CustomExtensions")
set(EXTENSION_CONTRIBUTORS "Ryan Morrison (RowanSOM)")
set(EXTENSION_DESCRIPTION "This is an example of a simple extension")
set(EXTENSION_ICONURL "http://www.example.com/Slicer/Extensions/Color_All_Visible_Models.png")
set(EXTENSION_SCREENSHOTURLS "http://www.example.com/Slicer/Extensions/Color_All_Visible_Models/Screenshots/1.png")
set(EXTENSION_DEPENDS "NA") # Specified as a space separated string, a list or 'NA' if any

#-----------------------------------------------------------------------------
# Extension dependencies
find_package(Slicer REQUIRED)
include(${Slicer_USE_FILE})

#-----------------------------------------------------------------------------
# Extension modules
add_subdirectory(Color_All_Visible_Models)
## NEXT_MODULE

#-----------------------------------------------------------------------------
include(${Slicer_EXTENSION_GENERATE_CONFIG})
include(${Slicer_EXTENSION_CPACK})
