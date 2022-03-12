def padder(header = "begin", footer = "end", filler = "-", count = 2):
    diff = int(len(header) - len(footer))
    if count < abs(diff):
        count = int(abs(diff) / 2) + 1
    tabs = ('\t' * count)
    tabs = tabs.replace('\t', filler)
    sofline = tabs + header + tabs
    eofline = tabs + footer + tabs
    if len(sofline) > len(eofline):
        offset = int((len(sofline) - len(eofline)) / 2)
        if offset:
            sofline = sofline[offset:-abs(offset + 1)]
    if count < len(header) / 2:
        head = header
    else:
        head = sofline
    if count < len(footer) / 2:
        end = footer
    if len(eofline) > len(sofline):
        offset = int((len(eofline) - len(sofline)) / 2)
        if offset:
            eofline = eofline[offset:-abs(offset)]
    if diff != 0:
        if diff % 2 != 0 and diff < 0:
            eofline = eofline[:-1]
        elif diff % 2 != 0 and diff > 0:
            if offset % 2 == 0:
                eofline = eofline + filler
            if diff % 2 != 0:
                if offset == 0 or offset % 2 == 0:
                    sofline = sofline + filler
                if diff % 2 != 0 and diff <= 1:
                    eofline = eofline + filler
            else:
                eofline = eofline[:-1]
        elif diff % 2 == 0 and diff > 0:
            sofline = sofline + filler
    return sofline, eofline
header = 'Starting this header'
footer = 'Ending this footer'
num_spaces = 6 #required to be >= difference of the strings(if they aren't equal size)
filler = '-'
head, foot = padder(header = header, footer = footer, filler = filler, count = num_spaces)
print(head)
print(foot)
