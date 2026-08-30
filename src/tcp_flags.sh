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

echo "tcp_flag decimal list: ${tcp_flag[@]}"
echo "tcp_flag flag list: ${(k)tcp_flag[@]}"

for i in ${(k)tcp_flag[@]}
do
  binary=$(echo "ibase=10;obase=2;$tcp_flag[$i]" | bc | xargs printf "%08d\n")
  hexadecimal=$(echo "ibase=10;obase=16;$tcp_flag[$i]" | bc | xargs printf "%04X\n")
  echo "key: $i => binary:$binary - hexadecimal:$hexadecimal - decimal: $tcp_flag[$i]"
done
