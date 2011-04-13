#!/usr/bin/env python
import csv
import sys

"""
Convert a csv to a table in Trac format.
"""

def get_row(row_src, lsep="|=", rsep="=|"):
    row = ""
    for field in row_src:
        row += "%s %s %s" % (lsep, field, rsep)
    return row

def handle_opt():
    from optparse import OptionParser
    parser = OptionParser()
    return parser.parse_args()

if __name__ == "__main__":
    """use the pipe to input
    """
    opts, args = handle_opt()
    if len(args) != 1:
        print "Usage:"
        print
        print "    python csv2trac_table infile"
        print
        sys.exit(0)
    filename = args[0]
    c = csv.reader(open(filename))
    header = c.next()
    out = []
    out.append("|%s|" % get_row(header))
    for row in c:
        out.append("|%s|" % get_row(row, "|", "|"))
    print "\n".join(out)

