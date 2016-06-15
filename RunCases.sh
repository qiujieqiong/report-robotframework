#!/bin/bash
if [[ -z "AUTO_LOGIN_USER" ]]; then
    echo a user name must be given in order to login into destkop >&2
    exit 1    
fi

if [[ 0 != $UID ]]; then
    echo priveledged user is required >&2
    exit 1
fi

echo $CASE_ID

if [[ ! -z "CASE_ID" ]]; then 
	arr=$(echo $CASE_ID|tr "," "\n")
	n=0
	echo "$arr" |while read line
	do
		echo "$n:$line"	
		casesID[$n]=$line
		#count=$[ $count + 1 ]
		#let "count+=1"
		((n++))
	done 
echo ${#arr[@]}
echo ${arr[@]} 

fi

set -e
if [[ "$DEBUG" ]]; then
    PS4="> ${0##*/}: "
    set -x
fi

systemctl is-active lightdm >/dev/null && systemctl stop lightdm || true


systemctl start lightdm
sleep 30
# wait for the launching of desktop till timeout
ps aux |grep dde-dock |grep -v grep
if [[ $? == 0 ]]; then
echo $PWD
su - $AUTO_LOGIN_USER <<EOF
export DISPLAY=:0
env 
cd /home/$AUTO_LOGIN_USER
pwd
ls -ahl /home/$AUTO_LOGIN_USER
git clone https://github.com/qiujieqiong/testlink-robotframework-integration.git
cd /home/$AUTO_LOGIN_USER/testlink-robotframework-integration/checklist/launcher
echo $PWD
pybot -v casesID:${arr[@]}  launcher.txt
ls -ahl
EOF
fi