[![Dev Build Status](https://travis-ci.com/drforse/aiogram_oop_framework.svg?branch=master)](https://travis-ci.com/drforse/aiogram_oop_framework)  

# aiogram_oop_framework
An extender for aiogram to make it more OOP

docs: https://aiogram-oop-framework.readthedocs.io/en/latest


## [Live Templates](https://www.jetbrains.com/help/pycharm/using-live-templates.html) for PyCharm
You can find live templates in "misc/idea/live templates"  
To just install them all import all.zip through File | Manage IDE Settings | Import  
To install some of them you should follow these instructions:
1) copy the content of file with template which you want to add
2) go to File | Settings | Editor | Live Templates
3) add Template Group with any name you want (not required)
4) add Live Template to the group you created (or Python group)
5) Paste content to the created Live Template
6) Click edit variables
7) Edit variables as showed below:
    Name|Expression|Default value|Skip if defined   
    ---|---|---|---
    CLASS_NAME|capitalize(fileNameWithoutExtension())|   |as you wish
