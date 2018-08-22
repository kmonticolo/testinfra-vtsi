#!/bin/bash
py.test test_tigo_cim_demo.py --ssh-config=/home/kamil/.ssh/config --hosts root@10.48.77.9 -v
py.test test_tigo_pump_demo.py --ssh-config=/home/kamil/.ssh/config --hosts root@10.48.77.10 -v
py.test test_tigo_vtsi_demo.py --ssh-config=/home/kamil/.ssh/config --hosts root@10.48.77.11 -v

