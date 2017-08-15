#!/bin/bash

DIRECTORY="your/directory"
OUTFILE="output.txt"

echo "Base directory is $DIRECTORY"
echo "Saving structure at $OUTFILE"

FILES=$(find $DIRECTORY -type f -name '*.js')
COUNT=0

for file in $FILES
do
  ((COUNT++))
  RESULTS=`grep 'require(' $file`
  echo "$file :: $RESULTS @@" >> $OUTFILE
done

echo "Processed $COUNT files"
