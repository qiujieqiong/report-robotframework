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
cd /home/$AUTO_LOGIN_USER
pwd
ls -ahl /home/$AUTO_LOGIN_USER
git clone https://github.com/qiujieqiong/testlink-robotframework-integration.git
cd /home/$AUTO_LOGIN_USER/testlink-robotframework-integration/checklist/launcher
echo $PWD
echo ${arr[@]} > casesID.txt
su - $AUTO_LOGIN_USER <<EOF
pybot /home/$AUTO_LOGIN_USER/testlink-robotframework-integration/checklist/launcher/launcher.txt
ls -ahl
EOF
ls -ahl
lava-test-run-attach log.html text/plain
lava-test-run-attach test.result text/plain
fi