#!/bin/bash
# 9. Catch me if you can!
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
