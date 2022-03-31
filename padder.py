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
    fleft_ = hleft_
    fright_ = hright_
    #return formatted header and footer
    return fleft_, fright_, hright_, hleft_, head, foot
header = 'The Shining Column of Data'
footer = 'The red typewriter is typing by itself'
filler = '-'
corner = '*'
lines = ['all code and no compile makes jack nullboy',
		'all code and no compile makesjack a null boy',
		'all code and compile makes jack a null',
		'all code and no compile makes jack a null boyyy',
		'all code and no compile makes jack a null b',
		'all code and no compile makes jack a null bo']
maxlinelen = len(max(lines, key = len))
if len(header) > maxlinelen:
    maxlinelen = len(header)+1
    width = int(maxlinelen/2)+1
    print(width)
elif len(footer) > maxlinelen:
	maxlinelen = len(footer)+1
	width = int(maxlinelen/2)+1
	print(width)
else:
  diff = int((maxlinelen - len(max(header, footer)))/2)
  if diff % 2 == 0:
  	width = int(maxlinelen/diff) + (divmod(diff, 2)[0] - divmod(diff, 2)[1]) 
  else:
  	width = int(maxlinelen/diff)+1 + divmod(diff, 2)[0]  + divmod(diff, 2)[1]
head_, foot_ = padder(header = header, footer = footer, filler = filler, count = width)
fleft, fright, hright, hleft, head, foot = columnize(max_line_len = maxlinelen, width=int(maxlinelen/2)+1, head = head_, foot = foot_)
#print out column 1
for idx, line in enumerate(lines):
	if idx == 0:
		print(hleft + head + hright)
		print('| ' + line.ljust(maxlinelen,' ') + ' |')
	elif idx == len(lines)-1:
		print('| ' + line.ljust(maxlinelen,' ') +' |')
		print(fleft + foot + fright)
	else:
		print('| ' + line.ljust(maxlinelen,' ') + ' |')
#print(fleft + foot + fright)
