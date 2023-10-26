"""Word Finder: finds random words from a dictionary."""
from random import choice

class WordFinder:
    """
    Finds random words from a dictionary

    Attributes:
    --------------------
    file: .txt file where the words come from
    words: dictionary where the words from the .txt file is saved

    >>> wf = WordFinder('simple.txt')
    6 words read
    
    >>> wf.random() in ['banana', 'cranberry','kumquat','door','hinge','blackjack']
    True
    >>> wf.random() in ['banana', 'cranberry','kumquat','door','hinge','blackjack']
    True
    >>> wf.random() in ['banana', 'cranberry','kumquat','door','hinge','blackjack']
    True
    >>> wf.random() in ['banana', 'cranberry','kumquat','door','hinge','blackjack']
    True
    >>> wf.random() in ['banana', 'cranberry','kumquat','door','hinge','blackjack']
    True
    >>> wf.random() in ['banana', 'cranberry','kumquat','door','hinge','blackjack']
    True

    """
    
    def __init__(self, file_path):
        self.file_path = file_path
        self.words = list()
        self.words_list = list()
        
        with open(file_path) as f:
            self.words_list = f.readlines()

        self.words = self.parse()
    
        print(f"{len(self.words)} words read")
    
    def parse(self):
        """parse the list read from the text file to get rid of white space and new line"""
        return [word.strip() for word in self.words_list]
    
    def random(self):
        """randomly chooses a word from words"""
        return choice(self.words)
    
    
class SpecialWordFinder(WordFinder):
    """
    Finds random words from a dictionary that may contain 
    comments and blank space

    inherits from class WordFinder

    >>> swf = SpecialWordFinder('complex.txt')
    3 words read

    >>> swf.random() in ['Apple','Banana','Carrot']
    True
    >>> swf.random() in ['Apple','Banana','Carrot']
    True
    >>> swf.random() in ['Apple','Banana','Carrot']
    True
    
    """
    def parse(self):
        """in addition to white space and new lines, parses out comments and empty spaces between lines"""
        return [word.strip() for word in self.words_list if word.strip() and not word[0] == '#']
