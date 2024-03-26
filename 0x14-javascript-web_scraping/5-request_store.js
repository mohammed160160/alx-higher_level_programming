#!/usr/bin/node

const fs = require('fs');
const request = require('request');

const URL = process.argv[2];
const File = process.argv[3];

request.get({ url: URL, encoding: 'utf-8' }, (error, response, body) => {
  if (error) {
    console.error('Error occurred:', error);
  } else {
    if (response.statusCode === 200) {
      fs.writeFile(File, body, 'utf-8', (err) => {
        if (err) {
          console.error('Error occurred:', err);
        }
      });
    } else {
      console.error('Error occurred:', error);
    }
  }
});
