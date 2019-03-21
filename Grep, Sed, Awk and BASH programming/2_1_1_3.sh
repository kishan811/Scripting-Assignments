cd /usr/share/dict/
cat words | sed -ne '/^[aeiou].*[aeiou]$/p'
