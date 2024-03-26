#!/usr/bin/node

const request = require('request');

const URL = process.argv[2];

request.get(URL, (error, response, body) => {
  if (error) {
    console.error('Error occurred:', error);
  } else {
    if (response.statusCode === 200) {
      const TodoList = JSON.parse(body);
      const completedTasks = {};
      TodoList.forEach(todo => {
        if (todo.completed) {
          if (completedTasks[todo.userId]) {
            completedTasks[todo.userId]++;
          } else {
            completedTasks[todo.userId] = 1;
          }
        }
      });
      console.log(completedTasks);
    } else {
      console.error('Error occurred:', error);
    }
  }
});
