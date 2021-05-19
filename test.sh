#!/bin/bash

#--------------------------------------------
# 这是一个注释

#--------------------------------------------
# 当前时间 格式: 2021-05-19T10:46:37
name=$(date "+%Y-%m-%dT%H:%M:%S")

if [ "$*" ];then
    name=`echo $*`
    echo  ${name}
#else
#    echo "没有带参数 "
fi

echo "本次git提交注释为: ${name}";

git add .
git commit -m ${name}
git push