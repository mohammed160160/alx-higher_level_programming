#!/bin/bash
#takes a URL as argument, sends a GET request, and display body of the response
curl -s "$1" -X GET -H "X-School-User-Id:98"
