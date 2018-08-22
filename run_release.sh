#!/bin/bash
py.test test_tigo_cim_release.py --ssh-config=/home/kamil/.ssh/config --hosts root@10.48.77.29 -v
py.test test_tigo_pump_release.py --ssh-config=/home/kamil/.ssh/config --hosts root@10.48.77.30 -v
py.test test_tigo_vtsi_release.py --ssh-config=/home/kamil/.ssh/config --hosts root@10.48.77.31 -v

