#!/usr/bin/env python3
#lib/testing/debug.py

from __init__ import CONN, CURSOR
from department import Department

import ipdb

Department.drop_table()
Department.create_table()

payroll = Department("Payroll", "Building A, 5th Floor")
payroll.save()

hr = Department("Human Resources", "Building C, East Wing")
hr.save()

Department.create('Engineering', 'Building B, 2nd Floor')

ipdb.set_trace()
