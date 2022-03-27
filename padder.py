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
def columnize(max_line_len, width, head, foot):
    fill_ws = int(abs(len(head) - max_line_len)/2) or 1
    if len(head) % 2 == 0:
        if len(head) > (fill_ws*2) + max_line_len:
            if not header:
                hright_ = filler + corner
            else:
                hright_ = corner
        else:
            if not header and max_line_len % 2 != 0:
                hright_ = filler + corner
            else:
                if max_line_len % 2 != 0:
                    hright_ = filler + corner
                else:
                    hright_ = corner
        hleft_ = corner
    else:
        hleft_ = corner
        hright_ = corner
        if max_line_len % 2 == 0:
            if max_line_len > len(header):
                head = head[:-1]
                foot = foot[:-1]
    if footer:
        fill_ = abs(int(len(head) / 2) - int(len(footer)/2))
        if fill_ % 2 != 0 and len(footer) % 2 != 0:
            if len(head) % 2 != 0:
                fleft_ = corner + (filler * (fill_+1))
            else:
                fleft_ = corner + (filler * (fill_-1))
        elif fill_ % 2 == 0 and len(footer) % 2 != 0:
            if len(head) % 2 != 0:
                fleft_ = corner + (filler * (fill_))
            else:
                fleft_ = corner + (filler * (fill_-1))
        elif fill_ % 2 != 0 and len(footer) % 2 == 0:
            if len(head) % 2 != 0:
                fleft_ = corner + (filler * (fill_+1))
            else:
                fleft_ = corner + (filler * (fill_))
        else:
            if len(head) % 2 != 0:
                fleft_ = corner + (filler * (fill_+1))
            else:
                fleft_ = corner + (filler * (fill_))
        fright_ = (filler * (fill_)) + corner
        foot = footer
    else:
        fleft_ = hleft_
        fright_ = hright_
    #return formatted header and footer
    return fleft_, fright_, hright_, hleft_, head, foot
header = 'Column 1'
footer = 'End Column 1'
filler = '-'
corner = '+'
lines = ['data is here','more data on this second row','even more']
maxlinelen = len(max(lines, key = len))
if len(header) > maxlinelen:
    maxlinelen = len(header)
width = int(maxlinelen/2)+1
head_, foot_ = padder(header = header, footer = '', filler = filler, count = width)
fleft, fright, hright, hleft, head, foot = columnize(max_line_len = maxlinelen, width=int(maxlinelen/2)+1, head = head_, foot = foot_)
#print out column 1
print(hleft + head + hright)
for line in lines:
    print('| ' + line.ljust(maxlinelen,' ') + ' |')
print(fleft + foot + fright)
