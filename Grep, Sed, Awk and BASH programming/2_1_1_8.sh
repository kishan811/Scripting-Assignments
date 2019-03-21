 #!/bin/bash
cd /usr/share/dict/
sed -n -E "/[a-z]/p" words | sed -n -E '/^.....$|^..........$/p'