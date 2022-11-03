# project-symmetry
## About
Software designed for comparing Wikipedia articles in different languages in order to determine what information is missing from one article, but present in another. The goal is for everyone to have the same access to information no matter what language they speak. This is just one small step in eliminating the digital divide. 
The intended use of this software is for comparing Wikipedia articles, however in it's current state, users must copy/paste text into text-boxes. Because of this, it can be used to compare any 2 sets of text to view similarities.
For more information, visit: https://www.grey-box.ca
## Requirements
Python 3+:  
https://www.python.org/downloads/  
Git:  
https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
## Installation
```
# go to your operating system's command line interface
# clone repo 
git clone https://github.com/aidhayes/project-symmetry
# change directory to project-symmetry
cd project-symmetry
# install required libraries
python3 -m pip install -r requirements.txt
# run program
python3 main.py
```
## Disclaimer
This project utilizes several NLP libraries to compare text. It is important to note that the results may not always be accurate. Most of these libraries do not take into consideration sentence structure and grammar, so it is advised that the user double checks to make sure highlighted sections are *close enough* to each other. The best translations and comparisons will always be made by a real person, however having someone manually do this would be extremely time consuming, which is one of the problems this project aims to solve.
