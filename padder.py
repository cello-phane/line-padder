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
    fillc = 0
    if padded_header_size >= padded_footer_size:
        if padded_header_size != (fillc * 2) + len_header:
            fillc = count - offset
        header_ = (filler * (count - offset)) + header + (filler * fillc)
        footer_ = pads + footer + pads
    elif padded_footer_size >= padded_header_size:
        if padded_footer_size != (fillc * 2) + len_footer:
            fillc = count - offset
        footer_ = (filler * (count - offset)) + footer + (filler * fillc)
        header_ = pads + header + pads
    else:
        header_ = pads + header + pads
        footer_ = pads + footer + pads
    len_header_ = len(header_)
    if len_header != len(footer_):
        footer_ = footer_ + filler * (abs(len(header_) - len(footer_)))
        header_ = header_ + filler * (abs(len(footer_) - len(header_)))
    if len(header_) > len(footer_) and count >= len(header_):
        footer_ += filler
    if len(footer_) > len(header_) and count >= len(footer_):
        header_ += filler
    return header_, footer_
header = 'This is a header'
footer = 'Footer'
filler = '-'
head, foot = padder(header = header, footer = footer, filler = filler)
print(head)
print(foot)
