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
def columnize(max_line_len, head, foot):
    fill_ws = int(abs(len(head) - max_line_len)/2) or 1
    corner = '*'
    filler = "-"
    if len(head) % 2 == 0:
        if len(head) > (fill_ws*2) + max_line_len:
            if not head:
                hright_ = filler + corner
            else:
                hright_ = corner
        else:
            if not head and max_line_len % 2 != 0:
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
            if max_line_len > len(head):
                head = head[:-1]
                foot = foot[:-1]
    fleft_ = hleft_
    fright_ = hright_
    #return formatted header and footer
    return fleft_, fright_, hright_, hleft_, head, foot
def print_padded(strings_, header_, footer_):
    maxlinelen = len(max(strings_, key = len))
    minlinelen = len(min(strings_, key = len))
    (head,foot) = padder(header = header_, footer = footer_, filler = "-", count = 0)
    fleft_, fright_, hright_, hleft_, head, foot = columnize(maxlinelen, head, foot)
    len_of = len(hleft_ + head + hright_)
    expand_len_t = int((maxlinelen - len_of) // 2)+1
    expand_len_b = int((maxlinelen - len_of) // 2)+1
    print(hleft_ + (expand_len_t * '-') + head + (expand_len_t * '-') + hright_)
    for l in strings_:
        print(" " + l)
    print(hleft_ + (expand_len_b * '-') + foot + (expand_len_b * '-') + hright_)      
lines = ['all code and no compile makes jack nullboy',
		'all code and no compile makesjack a null boy',
		'all code and compile makes jack a null',
		'all code and no compile makes jack a null boyyy',
		'all code and no compile makes jack a null byy',
		'all code and no compile makes jack a null bo']
#print out column 1
print_padded(lines, header_="begin", footer_="end")
