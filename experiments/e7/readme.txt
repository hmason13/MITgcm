the input/data has been modified slightly.
instead of using a bin file to initiate the temperature, the list of 50 
temp levels was directly added to the data file at tref.

this was because of issues from python saving the files as .bin and
mitgcm interpreting the bin files. this is true for e7,e8,e9,e10
