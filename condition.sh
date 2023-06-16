#if a condition is true or false.
#!/bin/bash

#whoami = labmero

echo "who are you"
read user

if [["$user" != whoami ]];
then
    echo "you are not registered here"
else
