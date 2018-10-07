# !/bin/sh
ls -ilrt *.scel  | awk '{print $1}' | awk '{for(i=1;i<NF;i++);system("find ./ -inum " $i " -delete")}'
