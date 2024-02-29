#!/bin/bash
#send DELETE request to URL as the first argument, display the body of response
curl -s "$1" -X DELETE
