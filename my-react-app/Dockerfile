# Step 1: Use an official Node.js runtime as a parent image
FROM node:latest

# Step 2: Set the working directory in the container
WORKDIR /app

# Step 3: Copy the package.json files and install dependencies
COPY package*.json ./
RUN npm install

# Step 4: Copy the rest of your app's source code
COPY . .

# Step 5: Build your app
RUN npm run build

# Step 6: Install serve and serve the production build
RUN npm install -g serve
CMD ["serve", "-s", "build", "-l", "3000"]

# Step 7: Expose port 3000
EXPOSE 3000
