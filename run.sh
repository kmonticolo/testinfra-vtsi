# ssh-copy-id root@10.48.77.29

#py.test test_vtsi.py --ssh-config=/home/kamil/.ssh/config --hosts root@10.48.77.29 -v
py.test test_vtsi.py test_vtsi_serices.py --ssh-config=/home/kamil/.ssh/config --hosts root@10.48.77.31 -v

