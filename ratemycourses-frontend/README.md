# RateMyCourses Website (Frontend)

Use the Vue.js framework

## Project Setup for Frontend (Vue.js)

```
npm install -g @vue/cli
vue create ratemycourses-frontend
npm install axios
npm install vue-router
```
- When creating the vue project, choose [Vue 3] babel, eslint and Use Yarn

- To start the development server, type ```yarn serve```, the Local URL is the localhost (machine's internal address), and the Network URL (can be accessible from other devices connected to the same network)

- Install the extension called Vetur for better code visual on VSCode

- It is recommended in Vue.js to use a Single File Component (SFC), which includes the ```<template>```, ```<script>```, and ```<style>``` all in the same component ```.vue``` file.

## Note
- Add VUE_APP_API_URL in the .env file
