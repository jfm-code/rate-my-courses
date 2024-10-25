# RateMyCourses Website (Frontend)

## Overview

This project is a web-based application for reviewing and rating courses, similar to RateMyProfessors. It uses **Vue.js** for the frontend, **Flask** for the backend, and **PostgreSQL** for the database. The application is hosted on **AWS** with a CI/CD pipeline for automated build and deployment, using AWS services like **EC2**, **S3**, **RDS**, **CloudFormation**, and **CodePipeline**.

## Project Setup for Frontend (Vue.js)

```
npm install -g @vue/cli
vue create ratemycourses-frontend
npm install axios
```
When creating the vue project, choose [Vue 3] babel, eslint and Use Yarn

- To start the development server, type ```yarn serve```, the Local URL is the localhost (machine's internal address), and the Network URL (can be accessible from other devices connected to the same network)
