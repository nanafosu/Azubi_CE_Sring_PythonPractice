#!/bin/bash

echo "Please enter a number"

read number

if [ $number -gt 0 ];
then
 echo "The number is positive"
elif [ $number -lt 0 ];
then
 echo "The number is negative"
else
 echo "The number is zero"
fi

for ((i=1; i<=$number; i++))
do
  echo "$i"
done
