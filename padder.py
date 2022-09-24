def padder(header = "", footer = "", filler = "", count = 0):
    if not count or count == 0:
        count = int((max(len(header), len(footer)) - min(len(header), len(footer))) // 2) + 2
    pads = filler * count
    len_pads = len(pads)
    len_header = len(header)
    len_footer = len(footer)
    padded_header_size = len_header + len_pads
    padded_footer_size = len_footer + len_pads
    offset = int(abs(len_header - len_footer) // 2)
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
def columnize(max_line_len, head, foot, corner='', filler=''):
    fill_ws = int(abs(len(head) - max_line_len) // 2)
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
                head = head + filler
                foot = foot + filler
    fleft_ = hleft_
    fright_ = hright_
    #return formatted header and footer
    return fleft_, fright_, hright_, hleft_, head, foot
def print_padded(strings_, header_, footer_):
    filler_ = '-'
    corner_ = '~'
    sidel_ = '| '
    sider_ = ' |'
    count_ = 0 #this 0 says to auto-resize the column
    (head,foot) = padder(header = header_, footer = footer_, filler = filler_, count = count_)
    maxlinelen = len(max(strings_, key = len))
    if len(head) > maxlinelen:
        maxlinelen = len(head)
    minlinelen = len(min(strings_, key = len))
    fleft_, fright_, hright_, hleft_, head, foot = columnize(maxlinelen, head, foot, corner_, filler_)
    len_of = len(hleft_ + head + hright_)
    if sidel_ or sider_:
        side_lens = int(int((len(sider_) + len(sidel_) // 2) + 1) if int(len(sider_) + len(sidel_) // 2) % 2 != 0 else int((len(sider_) + len(sidel_) // 2)) + 2) // 2
    else:
        side_lens = 0
    expand_len_t = int((maxlinelen - len_of) // 2) + side_lens
    expand_len_b = int((maxlinelen - len_of) // 2) + side_lens
    print(hleft_ + (expand_len_t * filler_) + head + (expand_len_t * filler_) + hright_)
    for l in strings_:
        if l:
            if len(l) < maxlinelen:
                ws_ = " " * int((maxlinelen - len(l)))
                print(sidel_ + l + ws_ + sider_)
            else:
                print(sidel_ + l + sider_)
        else:
            print('')
    print(fleft_ + (expand_len_b * filler_) + foot + (expand_len_b * filler_) + fright_)
lines = ['This is sample text:',
        'Column text auto-resizes',
        'according to any cell\'s',
        'maximum length']
#print out column 1
print_padded(lines, header_="Symmetrical padding", footer_="footer")
