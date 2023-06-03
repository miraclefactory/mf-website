# ///////////////////////////////////////////////////////////////////////////
# Dockerfile for containerized devops
# Build: docker build --tag official-website:latest .
# Run: docker run -p 9000:9000 official-website:latest
# ///////////////////////////////////////////////////////////////////////////

# base python image
FROM python:3.11.2-alpine3.17

# flask working directory
WORKDIR /application

# copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# copy the rest of the files
COPY . .

# expose port 9000
ARG PORT=9000
EXPOSE $PORT

# run the application
CMD ["sh", "run.sh"]
