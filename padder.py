def padder(header = "begin", footer = "end", filler = "-", count = 2):
    if not filler:
        filler = ' '
    pads = filler * count
    len_pads = len(pads)
    len_header = len(header)
    len_footer = len(footer)
    padded_header_size = len_header + len_pads
    padded_footer_size = len_footer + len_pads
    offset = int(abs(len_header - len_footer) / 2)
    if padded_header_size > padded_footer_size:
        if (offset % 2 != 0 and padded_footer_size % 2 != 0):
            fillc = count - offset - 1
        elif offset % 2 == 0 and padded_footer_size % 2 != 0:
            fillc = count - offset - 1
        elif offset % 2 != 0 and padded_footer_size % 2 != 0:
            fillc = count - offset - 1
        else:
            fillc = count - offset
        header_ = (filler * (count - offset)) + header + (filler * fillc)
        footer_ = pads + footer + pads
    elif padded_footer_size > padded_header_size:
        print(offset)
        print(padded_header_size)
        if offset % 2 != 0 and padded_header_size % 2 == 0:
            fillc = count - offset - 1
        elif offset % 2 == 0 and padded_header_size % 2 != 0:
            fillc = count - offset - 1
        elif offset % 2 != 0 and padded_header_size % 2 != 0:
            fillc = count - offset - 1
        else:
            fillc = count - offset
        footer_ = (filler * (count - offset)) + footer + (filler * fillc)
        header_ = pads + header + pads
    else:
        header_ = pads + header + pads
        footer_ = pads + footer + pads
    return header_, footer_
header = 'Header Title'
footer = 'This is a footer___'
num_spaces = 9 #required to be >= difference of the strings for a symmetrical formatting
filler = '-'
head, foot = padder(header = header, footer = footer, filler = filler, count = num_spaces)
print(head)
print(foot)
