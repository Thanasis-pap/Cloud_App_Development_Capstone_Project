# Car Dealer Review Application

This project is a cloud-based web application that allows users to browse car dealerships, view reviews, and submit their own reviews for dealerships. The application integrates IBM Watson's Natural Language Understanding (NLU) service to analyze customer sentiment and provides a seamless user experience through dynamic pages, user authentication, and cloud deployment. **This project was developed as a part of IBM Full Stack Software Developer Specialization.**

## Project Overview

This web application was developed as part of a comprehensive final project that showcases the integration of cloud services with a modern web framework. The project includes several key components:

- User authentication and management
- Backend services for managing car dealers and customer reviews
- Sentiment analysis using Watson NLU
- Dynamic web pages using Django templates
- Containerized deployment for scalable and reproducible development

The app is fully deployed on IBM Cloud and utilizes a CI/CD pipeline to automate deployments.

## Key Features

- **Dealer Listings**: View a list of car dealerships from various locations.
- **Dealer Reviews**: Browse customer reviews for each dealership, along with sentiment analysis to gauge overall feedback.
- **Submit Reviews**: Authenticated users can submit their own reviews and ratings for any dealership.
- **Sentiment Analysis**: Reviews are analyzed using IBM Watson NLU to provide a sentiment score (positive, neutral, or negative) for each review.
- **User Authentication**: Users can sign up, log in, and manage their accounts using Django’s built-in user management system.
- **Cloud Deployment**: The application is deployed on IBM Cloud with a fully automated CI/CD pipeline, ensuring smooth updates and deployments.

## Technologies Used

- **IBM Watson NLU**: Provides natural language processing and sentiment analysis for reviews.
- **Django**: A high-level Python web framework used for backend logic and templating.
- **IBM Cloud Functions**: Used to manage car dealer and review data via serverless cloud functions.
- **PostgreSQL**: Used as the database to store dealer and review data.
- **Docker**: For containerizing the application to ensure consistency across different environments.
- **CI/CD**: Implemented with IBM Cloud Continuous Delivery pipelines for automated testing and deployment.

## ## How the Application Works

### 1. Dealer Listings

The main page of the application lists all car dealerships. Each dealer entry includes their location and a "View Reviews" button, which leads to the dealer's review page.

### 2. Dealer Reviews & Sentiment Analysis

On each dealer’s review page, customers can see reviews along with a sentiment analysis (positive, neutral, or negative) provided by IBM Watson NLU. This adds an extra layer of insight into customer feedback.

### 3. Adding a Review

Users can log in and submit reviews for a dealer. The review form allows users to provide text feedback, select a rating, and submit the review. Watson NLU automatically analyzes the sentiment of the review once submitted.

### 4. Cloud Functions Backend

The application’s backend is powered by IBM Cloud Functions. These serverless functions are used to fetch dealer data and manage user-submitted reviews.

## 5. License

This project is licensed under the Apache License 2.0, which allows you to use, modify, and distribute the code under certain conditions. You must include a copy of the license and provide proper attribution if you make any changes.

You can read the full text of the Apache 2.0 License in the [LICENSE](LICENSE) file provided in this repository.
