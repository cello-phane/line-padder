# line-padder
Makes a grid of text from a python list:

```
#In function 'print_padded':
# filler_ = '-'
# corner_ = '~'
# sidel_ = '| '
# sider_ = ' |'
# count_ = 0 #0 means auto-resize, 
             #otherwise it's the # of filler chars at left and right
lines = ['This is sample text:',
        'Column text auto-resizes',
        'according to any cell\'s',
        'maximum length']
#print out column 1
print_padded(lines, header_="Symmetrical padding", footer_="footer")
#Output:
~---Symmetrical padding----~
| This is sample text:     |
| Column text auto-resizes |
| according to any cell's  |
| maximum length           |
~---------footer-----------~
```
