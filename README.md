# line-padder
Adds padded characters to 2 lines(`header` and `footer`).
The header and footer should equal in size, because the wider string out of the 2 should force the other to change its size.

For the columnize function, add the len of the widest line/row, and make it display with auto-sizing as well.
The example in the code would print this:

+-----------Column 1-----------+
| data is here                 |
| more data on this second row |
| even more                    |
+---------End Column 1---------+
