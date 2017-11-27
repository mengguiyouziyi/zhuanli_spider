#!/bin/bash
. /etc/profile
. ~/.bash_profile
export PYENV_VIRTUALENV_DISABLE_PROMPT=1
eval "$(pyenv init -)"
pyenv activate env354
nohup python /data1/spider/menggui/zhuanli_spider/cnipr/cmd_wlglzx.py >> /data1/spider/menggui/zhuanli_spider/cnipr/wlglzx.out 2>&1 &