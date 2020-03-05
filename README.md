# _Simple Python Script for Bulk File Renaming_

#### _Script takes names from an excel file and renames all files in a given directory with names from excel file. v1.0.0, March 4, 2020._

#### By _**Nick Ramsey**_

## Description

_Our internal dashboard automatically names downloads based on account, project, filters, etc. One client was hoping we could rename the files to something more simple to identify. They had 200+ files needing to be renamed. To avoid errors and tedious work, I wrote a python script to automate this._

## Setup/Installation Requirements

* _$ brew install python_
* _$ git clone https://github.com/NickRamsey6/rename-bulk-files_
* _$ cd rename-bulk-files_
* _$ atom ._
* _$ pip install pandas_
* _$ pip install os_
* _$ pip install itertools_
* _create an .xlsx file with a list of the new names_
* _get the path to the directory of the files you want to rename_
* _enter the name of the .xlsx file (made above) to line 6, in the quotes_
* _enter the path to the directory in line 8 and again in 17_
* _$ python 3 renamer.py_


## Specs
| Behavior | Input | Output |
| ------------- |:-------------:| -----:|
| b1 | i1 | o1 |
| b2 | i2 | o2 |
| b3 | i3 | o3 |
| b4 | i4 | o4 |





## Known Bugs

_Not yet thoroughly tested. Should work for any file type, may adapt for flexibility._

## Support and contact details

_Contact email nramseysc@gmail.com for any comments, suggestions._

## Technologies Used

_Python3, pandas, os and itertools._

### License

*This software is licensed under the MIT license*

Copyright (c) 2020 **_Nick Ramsey, ClearlyRated_**
