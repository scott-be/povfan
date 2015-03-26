i=0; od -An -t x1 ~/message.bin | while read line; do \
                   for c in $line; do \
                       cmd=$(printf "echo -y 1 0x50 0x%x 0x$c b" $i); $cmd; ((i++));
                   done;
               done