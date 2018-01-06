#!/bin/sh
BASE=$(dirname $(realpath $0))
cat << EOF > ~/.gdbinit
source ${BASE}/pwndbg/gdbinit.py
source ${BASE}/gdb_functions.py
source ${BASE}/pwndbg-theme
EOF
