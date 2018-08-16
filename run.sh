# ssh-copy-id root@10.48.77.29

#py.test test_vtsi.py --ssh-config=/home/kamil/.ssh/config --hosts root@10.48.77.29 -v
py.test test_vtsi.py --ssh-config=/home/kamil/.ssh/config --hosts root@10.48.77.31 -v

py.test test_pump.py --ssh-config=/home/kamil/.ssh/config --hosts root@10.48.77.30 -v

py.test test_cim.py --ssh-config=/home/kamil/.ssh/config --hosts root@10.48.77.29 -v

