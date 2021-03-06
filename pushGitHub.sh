#!/bin/bash

# 当前时间 格式: 2021-05-19 10:46:37
echo -e "\033[2J "

name=$(date "+%Y-%m-%d %H:%M:%S")

if [ "$*" ];then
    name=`echo $*`
    echo  ${name}
#else
#    echo "没有带参数 "
fi

commit1="执行命令 git add . "
commit2="执行命令 git commit -m '${name}' "
commit3="执行命令 git push github main "

echo "本次git提交注释为: ${name}";

echo -e "\033[1m\033[33m ${commit1}  \033[0m"  #
git add .

echo -e "\033[1m\033[32m ${commit2} \033[0m"  # 绿色字体
git commit -m "${name}"

echo -e "\033[35m ${commit3} \033[0m"  # 紫色字体
git push github main  # push 到GitHub

