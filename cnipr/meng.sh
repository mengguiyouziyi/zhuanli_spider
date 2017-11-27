#!/bin/bash
. /etc/profile
. ~/.bash_profile
export PYENV_VIRTUALENV_DISABLE_PROMPT=1
eval "$(pyenv init -)"
pyenv deactivate
pyenv activate env354

ID=`ps -ef | grep "cmd_meng.py" |grep -v "grep"| awk '{print $2}'`
echo "first time $ID"
for id in $ID
do
    kill $id
    echo "killed $id"
done
echo "first sleep 30s..."
sleep 30

while true
do
    IDD=`ps -ef | grep "cmd_meng.py" |grep -v "grep"| awk '{print $2}'`
    echo "other times $IDD"
    if [ ! "$IDD" ]
    then
        break
    fi
    echo "other times sleep 5s..."
    sleep 5
done

echo "into work_package"
cd /data1/spider/menggui/zhuanli_spider/cnipr/
echo "excute main program"
nohup python /data1/spider/menggui/zhuanli_spider/cnipr/cmd_meng.py >> /data1/spider/menggui/zhuanli_spider/cnipr/out_meng.out 2>&1 &