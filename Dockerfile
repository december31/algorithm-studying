# ==========================================
# Multi-stage Dockerfile for Algo-Dungeon
# ==========================================

# 1. Base Development Stage
FROM node:22-alpine AS development

WORKDIR /app

# Install dependencies with caching
COPY package.json package-lock.json ./
RUN npm ci

# Copy source code
COPY . .

EXPOSE 5173

# Run Vite dev server with host accessible outside container
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]

# 2. Build Stage
FROM node:22-alpine AS build

WORKDIR /app

COPY package.json package-lock.json ./
RUN npm ci

COPY . .
RUN npm run build

# 3. Production Stage
FROM nginx:alpine AS production

COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=build /app/dist /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
