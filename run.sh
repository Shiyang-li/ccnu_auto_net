#!/bin/sh
while [ 1 ]
do
	ping -c 1 -q -s 8 baidu.com
	if [ $? -eq 0 ]; then
		sleep 600
	else
	{
	echo "reconnecting..."
	python3 login_ccnu.py
	sleep 30
	}
	fi
	#break
done
