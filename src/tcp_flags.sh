#!/bin/zsh
# Desc: enumerate TCP flag options in decimal format

unset tcp_flag
declare -A tcp_flag
tcp_flag[FIN]=1
tcp_flag[SYN]=2
tcp_flag[RST]=4
tcp_flag[PSH]=8
tcp_flag[ACK]=16
tcp_flag[URG]=32

echo "tcp_flag values: ${tcp_flag[@]}"
echo "tcp_flag values: ${(k)tcp_flag[@]}"
echo "tcp_flag values: ${tcp_flag[PSH]}"

for i in ${(k)tcp_flag[@]}
do
  echo "tcp_flag[$i]:$tcp_flag[$i] -  key: $i => value: $tcp_flag[$i]"
done
