
 awk '!NF {print} !($0 in file) { file[$0]; print }' Random.txt