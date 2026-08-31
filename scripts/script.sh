# !/bin/bash

Date=$(date +%F)
LogFile='/home/sourabh/work/training/logs/backup.logs'
dest='/home/sourabh/work/training/archives'
backup='/home/sourabh/work/training/projects'

echo "Enter the number of files to be kept"

read n_files

log_message(){

  echo "$(date '+%Y-%m-%d %H:%M:%S') [$1] $2" >> "$LogFile"
}


for f in "$backup"/*;
do 
  name=$(basename $f)
  tar -czvf $dest/"$name-$Date".tar.gz $f
  log_message "INFO" "backup created for $name"
done

total_projects=$(find ""$backup/* -maxdepth 0 -type d | wc -l)

i=0

for f in "$dest"/*;
do
  name=$(basename $f)
  if [ "$i" -lt $((total_projects - n_files)) ]; then
    echo "removing $f from archives"
  log_message "INFO" "removinr $name from archives"
    rm -rf "$f"
    ((i++))
  fi
done

