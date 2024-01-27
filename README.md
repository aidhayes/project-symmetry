# project-symmetry

## About

Software designed for comparing Wikipedia articles in different languages in order to determine what information is missing from one article, but present in another. The goal is for everyone to have the same access to information no matter what language they speak. This is just one small step in eliminating the digital divide. 

The intended use of this software is for comparing Wikipedia articles, however in it's current state, users must copy/paste text into text-boxes. Because of this, it can be used to compare any 2 sets of text to view similarities.

For more information, visit: https://www.grey-box.ca

## Requirements
Python version >=3.7 < 3.11  
https://www.python.org/downloads/  
Git:  
https://git-scm.com/book/en/v2/Getting-Started-Installing-Git

## Installation

```
# Go to your operating system's command line interface
# Go to the folder where you want to clone the project to 
# Clone repo 
  git clone https://github.com/grey-box/Project-Symmetry-Semantic-comparison-Alpha.git
# change directory to Project-Symmetry-Semantic-comparison-Alpha
  cd Project-Symmetry-Semantic-comparison-Alpha
# Install required libraries
  python -m pip install -r requirements.txt
# Install Punkt
  1- python
  2- import nltk
  3- nltk.download('punkt')
# Create a deepl config file
  1- Inside *dev* folder, create a file called *deeplconfig.py*
  2- In the file, add the following line of code: deepl_api_key = "your_api_key"
  3- Replace "your_api_key" by your personal deepl api key
  4- Save the file
# Run program
  python main.py
```

## Getting Started

### Text Entry

<img width="500" alt="Screenshot 2022-11-03 at 10 01 40 PM" src="https://user-images.githubusercontent.com/57809744/200054578-8d54f9d0-94a4-4a07-814a-7a5dae11c7ac.png">

Inside these text-boxes is where you will paste the articles you wish to compare. Please note, at this time text must be in the same language, so use a translation tool such as DeepL to make text the same language. 

### Language Selection

We currently offer support for 45 different languages. Select one from the drop down then hit "Select" to change the on screen display.

<img width="483" alt="Screenshot 2022-11-04 at 2 59 33 PM" src="https://user-images.githubusercontent.com/57809744/200055252-176e444a-b55f-4e73-b771-7b1b72a32b6b.png">

### Comparison

First select a comparison tool (currently, only 2 are supported):  

<img width="459" alt="Screenshot 2022-11-04 at 2 59 15 PM" src="https://user-images.githubusercontent.com/57809744/200055549-d37a470f-f2c5-43fa-8c7e-c46ef7053d58.png">  

Then select a similarity percentage:  

<img width="468" alt="Screenshot 2022-11-04 at 2 59 24 PM" src="https://user-images.githubusercontent.com/57809744/200056502-361d9a5c-e104-44ad-aaf8-f039dc19277d.png">

The program will search for sentences that have a similarity score >= to this number. (Note: The program is unlikely to return results if you select a high percentage due to the nature of comparison tools. A percentage of ~10% for BLEU Score and ~30% for Sentence Bert has returned best results, though feel free to test different values. Click "Select" to change the Comparison Tool and Similarity Percentage.  

Finally, click "Compare", and the program should highlight sentences in both articles than are similar to each other. Matching colors denote maching sentences.  

Ex. English v. French Article on Barack Obama:  

<img width="1258" alt="Screenshot 2022-11-04 at 3 28 43 PM" src="https://user-images.githubusercontent.com/57809744/200059469-af3f18e1-c6af-4504-8e71-6b3d8b826a7c.png">


Note: Some sections highlighted may not be very similar at all, please reference the disclaimer down below. We will try to get better results so less human review is needed.

## Testing

Testing for comparison speed will be done as follows:
- Clean up formatting of articles, if this step is not done the comparison will take much longer than needed (i.e. 1.5 minutes vs 10 minutes)
  - Paste without formatting into word document
  - Remove infobox
    - It's likely these contain roughly the same information, and since text is unformatted, it will be hard to tell where this information is coming from
    - Mostly done to cut down on comparison time
  - Preferably remove image captions
  - Remove references
- Minimal apps open so more RAM is being allocated to comparison (i.e. Tests were run with only VSCode, the comparison app, and Excel open).
- Number iterations based off # sentences in each article (O(m * n))
  - NLTK splits articles into sentences using `sent_tokenizer`, simply got length by using `len()`
- Estimates made based off previous results
  - Comparison speed calculated using time library 
  - Time per comparison = (total time) / (# iterations)
  - Initial estimate of .0005 seconds per iteration
- Articles of varying length used
  - Barack Obama (random selection)
  - Elvis Presley (One of the longest articles according to [this site](https://diff.wikimedia.org/2016/05/12/rock-n-scroll-english-wikipedias-longest-featured-articles/ "diff.wikimedia.org")
  - Boris Johnson (One of largest articles according to Wikipedia)

If you wish to not wait roughly 1-2 minute to compare entire articles, then it is recommended you only compare single sections at a time. Doing so will provide much faster results, though more testing will be needed if doing this section by section will save much time.

The instructions for the executable file:
# Project Symmetry Alpha Setup
Follow these steps to set up Project Symmetry Alpha on your system.
## Prerequisites
1. **Install PyInstaller 6.3.0**
   - Ensure PyInstaller version 6.3.0 is installed on your system.
## Configuration Steps
2. **Copy More Languages File**
   - Copy the file path of "morelanguagesFinal.csv" located under the "supplements" directory.
3. **Update Project Specification**
   - Navigate to the file named "Project-Symmetry-Alpha.specs" containing project specifications.
   - Replace the existing file path in the "datas" section with the copied path for "morelanguagesFinal.csv."
   - Also, copy the file path for the user guide and replace it in the "datas" section.
4. **File Path Adjustment**
   - Add an 'r' before the replaced file paths to ensure correct interpretation.
5. **Save Configuration**
   - Save the changes made to ".specs" file.
6. **Modify gui.py**
   - Open "gui.py" and locate line 48.
   - Replace the 'open' function with the commented line above it.
7. **Update User Guide Path**
   - In the "userguide" section of "gui.py" (line 434), uncomment the 'open' file code line and comment the existing line. This provides a specific path to the files.
8. **Run PyInstaller**
   - Open the command window and run the command:
     ```bash
     pyinstaller Project-Symmetry-Alpha.specs
     ```
9. **Execution**
   - The process will run for a while and generate a folder called "dist" in your directory.
   - Inside "dist," you will find an "exe" file along with a folder named "dict."
Now, you can run the executable file to use Project Symmetry Alpha. If you encounter any issues or have feedback, feel free to report them in the project repository. Happy using!

## Disclaimer

This project utilizes several NLP libraries to compare text. It is important to note that the results may not always be accurate. Most of these libraries do not take into consideration sentence structure and grammar, so it is advised that the user double checks to make sure highlighted sections are *close enough* to each other. The best translations and comparisons will always be made by a real person, however having someone manually do this would be extremely time consuming, which is one of the problems this project aims to solve.
