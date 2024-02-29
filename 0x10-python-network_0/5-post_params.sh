#!/bin/bash
#takes a URL, sends POST request to URL, and displays body of response
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
