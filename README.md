
# RateMyCourses Website

## Overview

- This project is a web-based application for reviewing and rating courses, similar to RateMyProfessors. 
- Tech stack:
    -  **Vue.js** for the frontend
    -  **Flask (Python)** for the backend
    - **PostgreSQL** for the database. 
- The application is hosted on **AWS** and implemented CI/CD for automated build and deployment, using AWS services such as **Amplify** to host the frontend, **EC2** to host the backend, **RDS** to host database, and **CDK** to automate the CI/CD via CLI (there's no need to use the UI/Console of AWS at all).
- Demo video: https://www.youtube.com/watch?v=1qdlbfD80E0

## Project Setup
- ```ratemycourses-frontend/```: folder that stores all files related to the frontend, contains the ```dist``` that will be used for Amplify.
- ```ratemycourses-backend/```: folder that stores all files related to the backend, including the database setup. This folder will be using in EC2 instance to run the backend in the background.
- ```CDK/```: folder that stores the files to use AWS CDK. In short, CDK is used to create all necessary AWS resources that are needed for this full-stack web app (Amplify, EC2, RDS, Security Groups, IAM policies and IAM roles).
- ```amplify.yml```: this file is used to override the default build setup in Amplify. It needs to be located here so that Amplify can detect it when cloning the whole repo. The reason we need this file is because we are combining the frontend & backend folder into 1 repo, so we need to go to the correct folder (in this case the frontend) to start Amplify.

## Notes
- This project is quite small so we decide to put everything in a repo. However in the future if the project grow, we will definitely separate the frontend and backend into different repos.
- At first, we plan to use S3 bucket + CloudFront for frontend, but then we realize that this project is quite small, we don't need too much control so Amplify will simplify a lot of our tasks.
- We use RDS database to replace PostgreSQL local database. It is more expensive and took much longer to create/delete the stack than MongoDB, but it is beneficial when it comes to the relationship between tables.
- In the future, we might host both frontend and backend on 1 virtual machine, with the help of web server nginx to save cost.

## How to run this web app
Go to the frontend and backend folder, read the README.md there first, then go to the CDK folder and also read its README.md. You can choose to manually deploy via AWS UI/Console or automatically deploy via AWS CLI.
