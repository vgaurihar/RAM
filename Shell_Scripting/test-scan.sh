#!/bin/bash -x
#
date

#ip=`ifconfig  eth1 | head -2 | tail -1 | tr -s ' ' | cut -d' ' -f3 | cut -d':' -f2`
#ip=`ip addr | grep 'state UP' -A2 | tail -n1 | awk '{print $2}' | cut -f1 -d'/'`
ip=`ifconfig | grep -A 8 'eth' | head -2 | tail -1 | tr -s ' ' | cut -d' ' -f3 | cut -d ':' -f2`
nm=`cat /etc/hosts | grep "$ip" | cut -d' ' -f1`
#name=`echo $nm | tr -s ' ' '-'`
LOGFILE="/var/log/clamav/clamav-$(date +'%Y-%m-%d').txt";
EMAIL_MSG="This is test mail for ClamAV Scan Report of $nm";
EMAIL_FROM="`hostname`";
#EMAIL_TO="vgaurihar@gmail.com, mtaylor@proteusdh.com, hmehtalia@proteusdh.com, sseifoddini@proteusdh.com, lchang@proteusdh.com, vgaurihar@proteusdh.com, gchouhan@proteusdh.com";
EMAIL_TO="vgaurihar@gmail.com, vgaurihar@proteusdh.com";
#DIRTOSCAN="/home";
DIRTOSCAN="/";

# Check for mail installation
type mail >/dev/null 2>&1 || { echo >&2 "I require mail but it's not installed. Aborting."; exit 1; };

# Update ClamAV database
echo "Looking for ClamAV database updates...";
freshclam --quiet;

TODAY=$(date +%u);

if [ "$TODAY" == "6" ];then
	echo "Starting a full weekend scan.";
	# be nice to others while scanning the entire root
	nice -n5 clamscan -ri / --exclude-dir=/sys/ &>"$LOGFILE";
else
	DIRSIZE=$(du -sh "$DIRTOSCAN"  2>/dev/null|cut -f1);
	echo -e "Starting a daily scan of "$DIRTOSCAN" directory.\nAmount of data to be scanned is "$DIRSIZE".";
	clamscan -ri "$DIRTOSCAN" &>"$LOGFILE";
#       clamscan -ri "$DIRTOSCAN" --exclude-dir=/sys/  --exclude-dir=/proc/ &>"$LOGFILE";
fi

# get the value of "Infected lines"
MALWARE=$(tail "$LOGFILE"|grep Infected|cut -d" " -f3);

# if the value is not equal to zero, send an email with the log file attached
if [ "$MALWARE" -ne "0" ]; then
	echo "$EMAIL_MSG"|mail -a "$LOGFILE" -s "ClamAV: Malware Found on `echo $nm | tr -s ' ' '-'`" -r "$EMAIL_FROM" "$EMAIL_TO";
fi

echo "The script has finished.";

date
exit 0;
