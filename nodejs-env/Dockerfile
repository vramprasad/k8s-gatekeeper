# Use a production-ready Node.js base image
FROM node:20-alpine

# Create a non-root user and group
RUN addgroup -g 1001 -S nodejs && \
    adduser -S nodejsuser -u 1001

# Set the working directory inside the container
WORKDIR /app

# Copy package.json and install dependencies
COPY package*.json ./
RUN npm ci --only=production

# Copy the rest of the application code
COPY . .

RUN chown -R nodejsuser:nodejs /app

# Switch to the non-root user
USER nodejsuser

# Start the application
CMD ["node", "src/index.js"]
# Expose the application port
EXPOSE 3000