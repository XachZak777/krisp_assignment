# Recommendation System

## Overview
This project is a microservices-based recommendation system. It includes:
- A `GENERATOR` service that generates recommendations.
- An `INVOKER` service that retrieves and caches recommendations.

## Getting Started

### Prerequisites
- Docker and Docker Compose installed on your machine.

### Running the Project
1. Clone the repository.
2. Build and start the services using Docker Compose:
   ```bash
   docker-compose up --build