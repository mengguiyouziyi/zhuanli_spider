#!/bin/bash
. /etc/profile
. ~/.bash_profile
export PYENV_VIRTUALENV_DISABLE_PROMPT=1
eval "$(pyenv init -)"
pyenv activate env354

while true
do
    ID=`ps -ef | grep "cmd_meng.py" |grep -v "grep"| awk '{print $2}'`
    echo "start $ID"
    if [ ! "$ID" ]
    then
        break
    fi
    for id in $ID
    do
        kill $id
        #IDD=`ps -ef | grep "cmd_meng.py" |grep -v "grep"| awk '{print $2}'`
        #echo "programing $IDD"
        echo "killed $id"
    echo "sleep 10s..."
    sleep 10
    done
done

nohup python /data1/spider/menggui/zhuanli_spider/cnipr/cmd_meng.py >> /data1/spider/menggui/zhuanli_spider/cnipr/meng_1.out 2>&1 &