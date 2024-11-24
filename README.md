
# RateMyCourses Website

## Overview

- This project is a web-based application for reviewing and rating courses, similar to RateMyProfessors. It uses **Vue.js** for the frontend, **Flask** for the backend, and **PostgreSQL** for the database. 
- The application is hosted on **AWS** with a CI/CD pipeline for automated build and deployment, using AWS services like **EC2**, **S3**, **RDS**, **CloudFormation**, and **CodePipeline**.

## Project Setup
Go to each folder (frontend or backend and see the readme file for more info)

## Integrate with AWS
- Initially, host frontend in Amplify and backend in EC2, and use local database first
- Then, transit to S3 bucket + CloudFront for frontend if we need more control
- Then, use RDS database to replace PostgreSQL local database
- In the future, we'll host both frontend and backend on 1 virtual machine, with the help of web server nginx