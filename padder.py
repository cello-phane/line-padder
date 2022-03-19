def padder(header = "begin", footer = "end", filler = "-", count = 0):
    if count == 0:
        count = int((max(len(header), len(footer)) - min(len(header), len(footer))) /2) + 4
    if not filler:
        filler = ' '
    pads = filler * count
    len_pads = len(pads)
    len_header = len(header)
    len_footer = len(footer)
    padded_header_size = len_header + len_pads
    padded_footer_size = len_footer + len_pads
    offset = int(abs(len_header - len_footer) / 2)
    fillc = abs(count - offset)
    if padded_header_size > padded_footer_size:    
        header_ = filler * fillc + header + filler * fillc
        footer_ = pads + footer + pads
    elif padded_footer_size > padded_header_size:
        footer_ = filler * fillc + footer + filler * fillc
        header_ = pads + header + pads
    else:
        header_ = pads + header + pads
        footer_ = pads + footer + pads
    if len(header_) != len(footer_):
        if len(header_) > len(footer_):
            footer_ = footer_ + filler * (abs(len(header_) - len(footer_)))
        elif len(footer_) > len(header_):
            header_ = header_ + filler * (abs(len(footer_) - len(header_)))
    return header_, footer_
header = 'Header'
footer = 'Footer'
filler = '-'
head, foot = padder(header = header, footer = footer, filler = filler)
print(head)
print(foot)
