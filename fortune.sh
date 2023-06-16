#!/bin/bash
fortunes=("You will get great success in the near future"
         "Your hardwork at Azubi Africa will pay off by landing cloud engineering role at europe to 100 companies"
         "Beware of unexpected opportunity in disguise")
random_index=$((RANDOM % ${#fortunes[@]}))

echo "Welcome to the fortune teller!"

echo "Your fortune for today is:"

echo "${fortunes[random_index]}"
