# RateMyCourses Website (Frontend)

Use the Vue.js framework

## Project Setup for Frontend (Vue.js)

```
npm install -g @vue/cli
vue create ratemycourses-frontend
npm install axios
npm install vue-router
npm install -g serve (to check after yarn build, before put in AWS)
```
- When creating the vue project, choose [Vue 3] babel, eslint and Use Yarn

- To start the development server, type ```yarn serve```, the Local URL is the localhost (machine's internal address), and the Network URL (can be accessible from other devices connected to the same network)

- Install the extension called Vetur for better code visual on VSCode

- It is recommended in Vue.js to use a Single File Component (SFC), which includes the ```<template>```, ```<script>```, and ```<style>``` all in the same component ```.vue``` file.

## Note
- Add VUE_APP_API_URL in the .env file (this is the URL of the backend endpoint)

## Deploy Frontend on AWS Amplify (manually via AWS UI/Console)
- Step 1: Build the frontend with ```yarn build``` (this command will create a dist folder inside frontend folder)
- Step 2: Verify the frontend to see if it works as expected after building with ```serve -s dist```. To use this command we need to install with ```yarn global add serve```
- Step 3: Push the ```dist``` folder that we just created in the git branch that we want to deploy with.
- Step 4: Go to Amplify, create a project, connect with Github repo and use this file (```amplify.yml```) to config:
```
version: 1
frontend:
  phases:
    preBuild:
      commands:
        - cd ratemycourses-frontend
        - yarn install
    build:
      commands:
        - yarn build
  artifacts:
        baseDirectory: ratemycourses-frontend/dist
        files:
        - '**/*'
  cache:
      paths:
      - ratemycourses-frontend/node_modules/**/*
```
- Step 5: Add the environment variable of the frontend to Amplify. Redeploy again if needed to see the changes.