
#!/bin/bash
cd /usr/share/dict/
cat words | sed -ne '/[[:punct:]]/p'
