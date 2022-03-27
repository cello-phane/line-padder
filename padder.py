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
    if len(header_) != len(footer_):
        if len(header_) > len(footer_):
            footer_ = footer_ + filler * (abs(len(header_) - len(footer_)))
        elif len(footer_) > len(header_):
            header_ = header_ + filler * (abs(len(footer_) - len(header_)))
        if len(footer_) % 2 != 0 and len(header_) % 2 == 0:
            footer_ += filler
        if len(footer_) % 2 == 0 and len(header_) % 2 != 0:
            header_ += filler
    return header_, footer_
header = 'columne'
footer = 'this footer'
filler = '-'
corner = '+'
line = 'data data data'
width = int(len(line)/2)+1
head, foot = padder(header = header, footer = '', filler = filler, count = width)
fill_ws = int(abs(len(head) - len(line))/2) or 1
if len(head) % 2 == 0:
    if len(head) > (fill_ws*2) + len(line):
        fill_ws += 1
        if not header:
            right_ = filler + corner
        else:
            right_ = corner
    else:
        if not header and len(line) % 2 != 0:
            right_ = filler + corner
        else:
            if len(line) % 2 != 0:
                right_ = filler + corner
            else:
                right_ = corner
    line = ' ' * (fill_ws) + line + ' ' * (fill_ws)
    left_ = corner
else:
    left_ = corner
    right_ = corner
    if len(line) % 2 == 0:
        if len(line) > len(header):
            head = head[:-1]
            foot = foot[:-1]
        else:
            line += ' '

    line = ' ' * (fill_ws) + line + ' ' * (fill_ws)
print(left_ + head + right_)
print('|' + line + '|')
if footer:
    if int(width/2)-1 % 2 != 0:
        fill_ = (int(width/2)-1)-1
        left_ = corner + (filler * (fill_+1))
    else:
        fill_ = (int(width/2)-1)-1
        left_ = corner + (filler * fill_)
    foot = footer
    right_ = (filler * fill_) + corner
print(left_ + foot + right_)
