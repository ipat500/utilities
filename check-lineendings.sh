#!/bin/bash
# Adapted from https://simon.aldrich.cc/blog/2016/04/git-pre-commit-dos-line-endings-crlf/

function isDOSFile
{
  local FILENAME="$1"
  file "$FILENAME" | grep -q "with CRLF"
}

# Find files with DOS line endings
FOUND=0
for FILE in $(exec git ls-files) ; do
    isDOSFile "$FILE"
    if (( $? == 0 ))
    then
      echo "\"$FILE\" has DOS line endings" >&2
      FOUND=1
    fi
done

exit $FOUND

