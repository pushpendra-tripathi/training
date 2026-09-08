# !/bin/bash
set -euo pipefail

function help ()
{
 echo "
 Name: Backup_script.sh

 DESCRIPTION:
      
    - Archives a given directory to './archives/<name>-YYYY-MM-DD.tar.gz'.
    - Keeps only the last N archives (argument), deletes older ones.
    - Prints a summary of created and deleted archives.

  USECASE:
    - chmod +x Backup_script.sh
    - sh Backup_script.sh [destination_path] [projects_folder path]
    
  OPTIONS:
    --help or -h: show help section
    --logs : shows the logs
 " 
}

LogFile='logs/app.log'

if [[ "$1" == '--help' || "$1" == '-h' ]]; then
  help
  exit 0
fi

if [[ "$1" == '--logs' || "$1" == '-h' ]]; then
  cat $LogFile
  exit 0
fi



Date=$(date +%F)
dest="$1"
backup="$2" 


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

