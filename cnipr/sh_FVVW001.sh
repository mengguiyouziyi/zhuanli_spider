#!/bin/bash
. /etc/profile
. ~/.bash_profile
export PYENV_VIRTUALENV_DISABLE_PROMPT=1
eval "$(pyenv init -)"
pyenv deactivate
pyenv activate env354

ID=`ps -ef | grep "cmd_FVVW001.py" |grep -v "grep"| awk '{print $2}'`
echo "first time $ID"
if [ "$ID" ]
then
    # 如果有这个id，说明在运行这个程序，就要杀死并等待30s，并执行后续判断的循环
    for id in $ID
    do
        kill $id
        echo "killed $id"
    done
    echo "first sleep 30s..."
    sleep 30
    while true
    do
        IDD=`ps -ef | grep "cmd_FVVW001.py" |grep -v "grep"| awk '{print $2}'`
        echo "other times $IDD"
        if [ ! "$IDD" ]
        then
            break
        fi
        echo "other times sleep 5s..."
        sleep 5
    done
fi

echo "into work_package"
cd /data1/spider/menggui/zhuanli_spider/cnipr/
echo "excute main program"
nohup python cmd_FVVW001.py >> out_FVVW001.out 2>&1 &