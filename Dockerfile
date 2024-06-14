# Use the official Ubuntu Minimal base image
FROM --platform=linux/amd64  ubuntu:20.04

# Avoid tzdata asking for geographic location
ENV DEBIAN_FRONTEND=noninteractive

# Install build tools
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    cmake \
    make \
    git \
    libcurl4-openssl-dev \
    libssl-dev

# Set the working directory in the Docker container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app
