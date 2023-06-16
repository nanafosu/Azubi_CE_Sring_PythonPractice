#!/bin/bash

echo "Enter the first number:"
read num1
echo "Enter the second number:"
read num2

#Perform arithmetic operation
sum=$(expr $num1 + $num2)
difference=$(expr $num1 - $num2)
product=$(expr $num1 \* $num2)
quotient=$(expr $num1 / $num2)

echo "sum:$sum"
echo "difference:$difference"
echo "product:$product"
echo "quotient:$quotient"
