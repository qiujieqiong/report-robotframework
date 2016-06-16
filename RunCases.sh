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
	arr=($(echo $CASE_ID|tr "," "\n"))
	length=${#arr[@]}
	echo $length
	for ((i=0; i<$length; i++))
	do
		echo ${arr[$i]}	
	done 

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

export DISPLAY=:0
env 
ls -ahl /home/$AUTO_LOGIN_USER
ls -ahl
#cd /home/$AUTO_LOGIN_USER/testlink-robotframework-integration/checklist/launcher
su - $AUTO_LOGIN_USER <<EOF
export DISPLAY=:0
echo $CASE_ID > casesID.txt
git clone https://github.com/qiujieqiong/testlink-robotframework-integration.git
pybot launcher.txt
EOF
fi
set +x