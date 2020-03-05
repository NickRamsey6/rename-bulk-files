import pandas as pd
import os, os.path
import itertools

# Read list of new names
names = pd.read_excel('Put excel list HERE')
# Select the directory of files to be renamed and load them in alphabetical order
files = "Path to directory of files to rename goes HERE"
list=os.listdir(files)
pdfs = []
for filename in os.listdir(files):
    if filename.endswith('.pdf'):
        pdfs.append(filename)
pdfs.sort(key=str.lower)


path="Same path HERE"
#Function for renaming
def rename(src, dst, extension):
    os.rename(b,a+'.'+extension)
os.chdir(path)

# Zip to iterate through two lists at the same time
for (a, b) in zip(names['Partner'], pdfs):
    rename(b, a, 'pdf')
