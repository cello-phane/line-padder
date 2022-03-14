def padder(header = "begin", footer = "end", filler = "-", count = 2):
    if not filler:
        filler = ' '
    diff = int(len(header) - len(footer))
    if int(abs(diff)/2) + 1 > count:
        if count < abs(diff):
            count = int(abs(diff) / 2) + 1
    tabs = (filler * count)
    sofline = tabs + header + tabs
    eofline = tabs + footer + tabs
    if len(sofline) > len(eofline):
        offset = int((len(sofline) - len(eofline)) / 2)
        if offset:
            sofline = sofline[offset:-abs(offset + 1)]
    elif len(eofline) > len(sofline):
        offset = int((len(eofline) - len(sofline)) / 2)
        if offset:
            eofline = eofline[offset:-abs(offset)]
        
    if diff != 0:
        if diff % 2 != 0 and diff < 0:
            eofline = eofline[:-1]
        elif diff % 2 != 0 and diff > 0:
            if offset % 2 == 0:
                eofline = eofline + filler
            if offset == 0 or offset % 2 == 0:
                sofline = sofline + filler
            if diff == 1:
                eofline = eofline + filler
        elif diff % 2 == 0 and diff > 0:
            sofline = sofline + filler
    return sofline, eofline
header = 'Header Title'
footer = 'This is a footer'
num_spaces = 10 #required to be >= difference of the strings for a symmetrical formatting
filler = '-'
head, foot = padder(header = header, footer = footer, filler = filler, count = num_spaces)
print(head)
print(foot)
