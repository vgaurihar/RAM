#!/bin/bash
export PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:$PATH

# sleep for random value to give upstream a bit of headroom
sleep $(echo $RANDOM | cut -c1-3) >> /dev/null 2>&1

# clear quarantine/session/tmp data every 14 days
/usr/sbin/tmpwatch 336 /usr/local/maldetect/tmp >> /dev/null 2>&1
/usr/sbin/tmpwatch 336 /usr/local/maldetect/sess >> /dev/null 2>&1
/usr/sbin/tmpwatch 336 /usr/local/maldetect/quarantine >> /dev/null 2>&1
/usr/sbin/tmpwatch 336 /usr/local/maldetect/pub/*/ >> /dev/null 2>&1


# check for new release version
/usr/local/maldetect/maldet -d >> /dev/null 2>&1


# check for new definition set
/usr/local/maldetect/maldet -u >> /dev/null 2>&1


# if were running inotify monitoring, send daily hit summary
if [ "$(ps -A --user root -o "comm" | grep inotifywait)" ]; then
        /usr/local/maldetect/maldet --alert-daily >> /dev/null 2>&1
	else
		# scan whole system
		/usr/local/maldetect/maldet -b -a / >> /dev/null 2>&1
fi

