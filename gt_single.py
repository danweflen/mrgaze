#!/opt/local/bin/python
"""
Run gaze tracking pipeline on a single subject/session

Example
----
>>> gt_single /Data/Subject_0001

Author
----
Mike Tyszka, Caltech Brain Imaging Center

Dates
----
2014-05-07 JMT From scratch

License
----
This file is part of geetee.

    geetee is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    geetee is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with geetee.  If not, see <http://www.gnu.org/licenses/>.

Copyright
----
2014 California Institute of Technology.
"""

import os
import sys
import datetime as dt

import pipeline

def main():
    
    # Get single session directory from command line
    if len(sys.argv) > 1:
        ss_dir = sys.argv[1]
    else:
        ss_dir = os.getcwd()
        
    # Split subj/session directory path into data_dir and subj/sess name
    data_dir, subj_sess = os.path.split(ss_dir)

    # Text splash
    print('')
    print('--------------------------------------------------')
    print('GeeTee Single Session Gaze Tracking Video Analysis')
    print('--------------------------------------------------')
    print('Version   : %s' % '0.1')
    print('Date      : %s' % dt.datetime.now())
    print('Data dir  : %s' % data_dir)
    print('Subj/Sess : %s' % subj_sess)
    print('')
    
    # Run single-session pipeline
    pipeline.RunSingle(data_dir, subj_sess)


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()