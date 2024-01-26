# Scrabble-trainer
This project is intended to help eccentric Scrabble players enhance their vocabulary and word recognition skills. The Python program takes a sentence as an input and replaces each word in the sentence with another word starting with the same letter that is the same length. If a particular word isn't found, the original word is returned.

## Resources 
The word list contains 370,000 words used to help prepare for Scrabble matches and is found here: https://github.com/dwyl/english-words/blob/master/words_alpha.txt. Note I do not own this list, I only made use of it to help train eccentric Scrabble players using this project.

## Getting Started
This program is compiled using Python. Please ensure that you have Python installed on your machine. If not, you can download it here: https://www.python.org/downloads. During the installation process, ensure that you check the option 'Add Python to PATH' or else the program will not be able to run.

Clone the Repository into a folder in your workspace. Either use the command line shown below or download it as a Zip file in GitHub directly and unzip the folder.
- git clone https://github.com/Craigels07/scrabble-trainer.git
  
### Running the Program
Open a command terminal and ensure the directory is in your scrabble-trainer folder, read the Note below to change directories. Then to execute the program:
- python scrabble_trainer.py

**NOTE**: Ensure your terminal is in the correct working directory. If not, then in your terminal run the following line and replace 'your_file_path' with the path to your scrabble-trainer folder - assuming your folder name is scrabble-trainer:
- cd 'your_file_path'\scrabble-trainer

Once the file has been executed the user is prompted with a message 'Enter a sentence:'. 
## Result of Running the Program
For example, given the sentence **'Happy dog plays in the sun'**, the program may return **'havel dea pipal ir sky'**. If you run the program again the output will be different.

### Additional Examples

-



