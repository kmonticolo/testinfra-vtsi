# VTSI infrastructure tests

## installation: 

`$ pip install testinfra`

its also good to install xdist plugin to speedup testing process - (103 vs 51 seconds with "-n8" parameter)
`$ pip install pytest-xdist`


## execution

for PUMP: `$ py.test test_pump.py --ssh-config=/home/kamil/.ssh/config --hosts root@10.48.77.30 -v`

for VTSI: `$ py.test test_pump.py --ssh-config=/home/kamil/.ssh/config --hosts root@10.48.77.31 -v`

where /home/kamil/.ssh/config is configuration which allows you to connect to vtsi site

content of .ssh/config:
`User seachange
 StrictHostKeyChecking no`
