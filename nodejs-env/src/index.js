const express = require('express');
const fs = require('fs');
const path = require('path');
const app = express();

const envAPIKey = process.env.ENV_API_KEY;

// Retrieve key from environment variable and print it
if (!envAPIKey) {
  console.error("ENV_API_KEY environment variable is not set!");
} else {
  console.log("ENV_API_KEY is set : " + envAPIKey);
}

// Retrieve key from mounted file and print it
try {
  const volApiKey = fs.readFileSync('/etc/secrets/apikey', 'utf8').trim();
  console.log('API Key loaded from file');
} catch (error) {
  console.error('Failed to read API key from file:', error.message);
  //process.exit(1);
}

// Health check endpoint
app.get('/health/live',(req,res)=>{
  res.status(200).json({
    status:'alive',
    timestamp:new Date().toISOString()
  });
});

// Start the server
app.listen(3000, () => {
  console.log('Server running on port 3000');
});