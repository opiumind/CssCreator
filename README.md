# CssCreator
Creates CSS file with class declaration skeleton, based on formatted html file, for Sublime Text 2 and Sublime Text 3.
It can help you to save time when you develop brandnew page or block.

# How to use
When you complete html file, you can create CSS file, based on it, automatically, which will contain class declarations skeleton.

###You can do it by:
* hot key `ctrl+shift+c` for Linux/Windows or `super+shift+c` for OS X
* main menu: `File --> Create CSS File`

**It creates CSS file, based on the file which is in the active window**

#Installation
### Package Control
Installation through [package control](http://wbond.net/sublime_packages/package_control) is recommended. It will handle updating your packages as they become available. To install, do the following:

* In the Command Palette, enter `Package Control: Install Package`
* Search for `CssCreator`

### Manually
Clone or copy this repository into the packages directory. By default, the packages directory is located at:

* OS X: ~/Library/Application Support/Sublime Text 2/Packages/
* Windows: %APPDATA%/Roaming/Sublime Text 2/Packages/
* Linux: ~/.config/sublime-text-2/Packages/

``For Sublime Text 3 use "3" instead of "2"``

#Rules of the plugin

* if you write two class attributes for one element, the plugin will ignore the second one
* if you write more than one class for one element, like `class="main-container__article _highlighted"`, you will get the following declaration in CSS file: 
`.main-container__article._highlighted {}`
* the plugin likes order, it will make indentation in CSS rules like in formated html in accordance to nesting