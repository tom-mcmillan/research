# Sail MCP Deployment Guide

This comprehensive guide covers deploying Sail MCP in various environments, from local development to production cloud deployments.

## Table of Contents

- [Overview](#overview)
- [System Requirements](#system-requirements)
- [Local Development Setup](#local-development-setup)
- [Docker Deployment](#docker-deployment)
- [Production Deployment](#production-deployment)
- [Cloud Deployments](#cloud-deployments)
- [Security Configuration](#security-configuration)
- [Monitoring & Logging](#monitoring--logging)
- [Backup & Recovery](#backup--recovery)
- [Troubleshooting](#troubleshooting)

## Overview

Sail MCP can be deployed in multiple configurations:

- **Local Development**: Single-machine setup for development
- **Docker Compose**: Containerized deployment for staging/production
- **Kubernetes**: Scalable cloud deployment
- **Cloud Platforms**: AWS, GCP, Azure managed services

## System Requirements

### Minimum Requirements

| Resource | Development | Production |
|----------|-------------|------------|
| **CPU** | 2 cores | 4+ cores |
| **RAM** | 4 GB | 8+ GB |
| **Storage** | 20 GB | 100+ GB SSD |
| **Network** | 10 Mbps | 100+ Mbps |

### Software Dependencies

- **Operating System**: Linux (Ubuntu 20.04+), macOS 12+, Windows 10+ with WSL2
- **Node.js**: Version 18+ (LTS recommended)
- **Docker**: Version 20.10+ with Docker Compose
- **PostgreSQL**: Version 14+
- **Redis**: Version 6+
- **Nginx**: Version 1.18+ (for reverse proxy)

## Local Development Setup

### Prerequisites Installation

#### macOS
```bash
# Install Homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install dependencies
brew install node@18 postgresql@14 redis docker
brew install --cask docker

# Start services
brew services start postgresql@14
brew services start redis
```

#### Ubuntu/Debian
```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install Node.js 18
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt-get install -y nodejs

# Install PostgreSQL 14
sudo apt-get install -y postgresql-14 postgresql-client-14

# Install Redis
sudo apt-get install -y redis-server

# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker $USER
```

### Project Setup

1. **Clone Repository**
```bash
git clone https://github.com/tom-mcmillan/sail.git
cd sail
```

2. **Backend Setup**
```bash
cd backend

# Install dependencies
npm install

# Copy environment template
cp .env.example .env

# Edit configuration
nano .env
```

**Backend Environment (.env):**
```bash
# Database Configuration
DATABASE_URL=postgresql://sail:sailpassword@localhost:5432/sail
POSTGRES_USER=sail
POSTGRES_PASSWORD=sailpassword
POSTGRES_DB=sail

# Redis Configuration
REDIS_URL=redis://localhost:6379

# Security
JWT_SECRET=your-super-secret-jwt-key-change-this-in-production
SESSION_SECRET=your-session-secret-key-change-this-too

# Application Settings
NODE_ENV=development
PORT=3001
FRONTEND_URL=http://localhost:3000

# File Storage
STORAGE_PATH=/tmp/sail-storage
MAX_FILE_SIZE=50MB

# OAuth2 Configuration (optional)
GOOGLE_CLIENT_ID=your-google-client-id
GOOGLE_CLIENT_SECRET=your-google-client-secret
GITHUB_CLIENT_ID=your-github-client-id
GITHUB_CLIENT_SECRET=your-github-client-secret

# Docker Socket (for MCP servers)
DOCKER_SOCKET_PATH=/var/run/docker.sock
```

3. **Database Setup**
```bash
# Create database and user
sudo -u postgres psql
```

```sql
CREATE USER sail WITH PASSWORD 'sailpassword';
CREATE DATABASE sail OWNER sail;
GRANT ALL PRIVILEGES ON DATABASE sail TO sail;
\q
```

```bash
# Run migrations
npm run migrate

# Run development setup
npm run setup
```

4. **Frontend Setup**
```bash
cd ../frontend

# Install dependencies
npm install

# Copy environment template
cp .env.local.example .env.local

# Edit configuration
nano .env.local
```

**Frontend Environment (.env.local):**
```bash
NEXT_PUBLIC_API_URL=http://localhost:3001/api
NEXT_PUBLIC_APP_URL=http://localhost:3000
NEXT_PUBLIC_OAUTH_CLIENT_ID=your-oauth-client-id
```

5. **Start Development Servers**
```bash
# Terminal 1: Backend
cd backend && npm run dev

# Terminal 2: Frontend  
cd frontend && npm run dev
```

6. **Verify Installation**
```bash
# Check backend health
curl http://localhost:3001/health

# Check frontend
open http://localhost:3000
```

## Docker Deployment

### Single-Server Docker Compose

1. **Prepare Environment**
```bash
# Create deployment directory
mkdir -p /opt/sail
cd /opt/sail

# Clone repository
git clone https://github.com/tom-mcmillan/sail.git .

# Copy production environment
cp docker-compose.prod.yml docker-compose.override.yml
```

2. **Configure Environment**
```bash
# Create environment file
cat > .env << EOF
# Database
POSTGRES_USER=sail
POSTGRES_PASSWORD=$(openssl rand -base64 32)
POSTGRES_DB=sail

# Redis
REDIS_PASSWORD=$(openssl rand -base64 32)

# Security
JWT_SECRET=$(openssl rand -base64 64)
SESSION_SECRET=$(openssl rand -base64 64)

# Application
NODE_ENV=production
DOMAIN=your-domain.com
FRONTEND_URL=https://your-domain.com
BACKEND_URL=https://api.your-domain.com

# SSL Configuration
ACME_EMAIL=admin@your-domain.com
EOF
```

3. **Start Services**
```bash
# Pull images and start
docker-compose up -d

# Check status
docker-compose ps

# View logs
docker-compose logs -f
```

4. **Initialize Database**
```bash
# Run migrations
docker-compose exec backend npm run migrate

# Create admin user
docker-compose exec backend npm run setup
```

### Docker Compose Configuration

**docker-compose.prod.yml:**
```yaml
version: '3.8'

services:
  frontend:
    build:
      context: ./frontend
      dockerfile: Dockerfile
    environment:
      - NODE_ENV=production
      - NEXT_PUBLIC_API_URL=https://api.${DOMAIN}
    labels:
      - traefik.enable=true
      - traefik.http.routers.frontend.rule=Host(`${DOMAIN}`)
      - traefik.http.routers.frontend.tls.certresolver=letsencrypt
    networks:
      - sail-network

  backend:
    build:
      context: ./backend
      dockerfile: Dockerfile
    environment:
      - NODE_ENV=production
      - DATABASE_URL=postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@database:5432/${POSTGRES_DB}
      - REDIS_URL=redis://redis:6379
      - JWT_SECRET=${JWT_SECRET}
      - SESSION_SECRET=${SESSION_SECRET}
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
      - sail-storage:/app/storage
    labels:
      - traefik.enable=true
      - traefik.http.routers.backend.rule=Host(`api.${DOMAIN}`)
      - traefik.http.routers.backend.tls.certresolver=letsencrypt
    depends_on:
      - database
      - redis
    networks:
      - sail-network

  database:
    image: postgres:14-alpine
    environment:
      - POSTGRES_USER=${POSTGRES_USER}
      - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
      - POSTGRES_DB=${POSTGRES_DB}
    volumes:
      - postgres-data:/var/lib/postgresql/data
    networks:
      - sail-network

  redis:
    image: redis:6-alpine
    command: redis-server --requirepass ${REDIS_PASSWORD}
    volumes:
      - redis-data:/data
    networks:
      - sail-network

  traefik:
    image: traefik:v2.10
    command:
      - --api.dashboard=true
      - --providers.docker=true
      - --providers.docker.exposedbydefault=false
      - --entrypoints.web.address=:80
      - --entrypoints.websecure.address=:443
      - --certificatesresolvers.letsencrypt.acme.tlschallenge=true
      - --certificatesresolvers.letsencrypt.acme.email=${ACME_EMAIL}
      - --certificatesresolvers.letsencrypt.acme.storage=/letsencrypt/acme.json
    ports:
      - "80:80"
      - "443:443"
      - "8080:8080"  # Traefik dashboard
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock:ro
      - traefik-certs:/letsencrypt
    networks:
      - sail-network

volumes:
  postgres-data:
  redis-data:
  sail-storage:
  traefik-certs:

networks:
  sail-network:
    driver: bridge
```

## Production Deployment

### Server Preparation

1. **System Updates**
```bash
# Update system packages
sudo apt update && sudo apt upgrade -y

# Install essential packages
sudo apt install -y curl wget git unzip htop ufw fail2ban
```

2. **Firewall Configuration**
```bash
# Configure UFW
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow ssh
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw enable
```

3. **Fail2Ban Configuration**
```bash
# Configure Fail2Ban for SSH protection
sudo cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local

# Edit jail.local to enable SSH protection
sudo nano /etc/fail2ban/jail.local
```

### SSL Certificate Setup

#### Automated SSL with Let's Encrypt (Recommended)

The Docker Compose configuration includes automatic SSL certificate generation via Traefik and Let's Encrypt.

#### Manual SSL Setup

```bash
# Install Certbot
sudo apt install certbot python3-certbot-nginx

# Obtain certificate
sudo certbot --nginx -d your-domain.com -d api.your-domain.com

# Test renewal
sudo certbot renew --dry-run
```

### Nginx Configuration (Alternative to Traefik)

**nginx.conf:**
```nginx
upstream backend {
    server 127.0.0.1:3001;
}

upstream frontend {
    server 127.0.0.1:3000;
}

# Redirect HTTP to HTTPS
server {
    listen 80;
    server_name your-domain.com api.your-domain.com;
    return 301 https://$server_name$request_uri;
}

# Frontend
server {
    listen 443 ssl http2;
    server_name your-domain.com;
    
    ssl_certificate /etc/letsencrypt/live/your-domain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/your-domain.com/privkey.pem;
    
    # Security headers
    add_header X-Frame-Options DENY;
    add_header X-Content-Type-Options nosniff;
    add_header X-XSS-Protection "1; mode=block";
    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" always;
    
    location / {
        proxy_pass http://frontend;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_cache_bypass $http_upgrade;
    }
}

# Backend API
server {
    listen 443 ssl http2;
    server_name api.your-domain.com;
    
    ssl_certificate /etc/letsencrypt/live/your-domain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/your-domain.com/privkey.pem;
    
    # Rate limiting
    limit_req_zone $binary_remote_addr zone=api:10m rate=10r/s;
    
    location / {
        limit_req zone=api burst=20 nodelay;
        
        proxy_pass http://backend;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_cache_bypass $http_upgrade;
        
        # MCP Server-Sent Events support
        proxy_buffering off;
        proxy_cache off;
    }
}
```

### Database Optimization

**PostgreSQL Configuration (`postgresql.conf`):**
```ini
# Memory settings
shared_buffers = 256MB          # 25% of RAM
effective_cache_size = 1GB      # 75% of RAM
work_mem = 4MB
maintenance_work_mem = 64MB

# Connection settings
max_connections = 100
listen_addresses = 'localhost'

# Performance settings
random_page_cost = 1.1
effective_io_concurrency = 200

# Logging
log_min_duration_statement = 1000  # Log slow queries
log_line_prefix = '%t [%p]: user=%u,db=%d,app=%a,client=%h '
```

**Database Backup Script:**
```bash
#!/bin/bash
# backup-db.sh

BACKUP_DIR="/opt/sail/backups"
DB_NAME="sail"
DB_USER="sail"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)

mkdir -p $BACKUP_DIR

# Create backup
pg_dump -U $DB_USER -h localhost $DB_NAME | gzip > $BACKUP_DIR/sail_backup_$TIMESTAMP.sql.gz

# Keep only last 30 backups
find $BACKUP_DIR -name "sail_backup_*.sql.gz" -mtime +30 -delete

echo "Backup completed: sail_backup_$TIMESTAMP.sql.gz"
```

## Cloud Deployments

### AWS Deployment

#### EC2 + RDS + ElastiCache

**Terraform Configuration:**
```hcl
# main.tf
provider "aws" {
  region = var.aws_region
}

# VPC
resource "aws_vpc" "sail_vpc" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_hostnames = true
  enable_dns_support   = true
  
  tags = {
    Name = "sail-vpc"
  }
}

# Subnets
resource "aws_subnet" "public_subnet" {
  count             = 2
  vpc_id            = aws_vpc.sail_vpc.id
  cidr_block        = "10.0.${count.index + 1}.0/24"
  availability_zone = data.aws_availability_zones.available.names[count.index]
  
  map_public_ip_on_launch = true
  
  tags = {
    Name = "sail-public-${count.index + 1}"
  }
}

resource "aws_subnet" "private_subnet" {
  count             = 2
  vpc_id            = aws_vpc.sail_vpc.id
  cidr_block        = "10.0.${count.index + 10}.0/24"
  availability_zone = data.aws_availability_zones.available.names[count.index]
  
  tags = {
    Name = "sail-private-${count.index + 1}"
  }
}

# RDS Instance
resource "aws_db_instance" "sail_db" {
  identifier = "sail-db"
  
  engine         = "postgres"
  engine_version = "14.9"
  instance_class = "db.t3.micro"
  
  allocated_storage     = 20
  max_allocated_storage = 100
  storage_encrypted     = true
  
  db_name  = "sail"
  username = "sail"
  password = var.db_password
  
  vpc_security_group_ids = [aws_security_group.rds_sg.id]
  db_subnet_group_name   = aws_db_subnet_group.sail_db_subnet_group.name
  
  backup_retention_period = 7
  backup_window          = "03:00-04:00"
  maintenance_window     = "sun:04:00-sun:05:00"
  
  skip_final_snapshot = false
  final_snapshot_identifier = "sail-db-final-snapshot"
  
  tags = {
    Name = "sail-database"
  }
}

# ElastiCache Redis
resource "aws_elasticache_subnet_group" "sail_cache_subnet_group" {
  name       = "sail-cache-subnet-group"
  subnet_ids = aws_subnet.private_subnet[*].id
}

resource "aws_elasticache_cluster" "sail_redis" {
  cluster_id           = "sail-redis"
  engine               = "redis"
  node_type            = "cache.t3.micro"
  num_cache_nodes      = 1
  parameter_group_name = "default.redis6.x"
  port                 = 6379
  subnet_group_name    = aws_elasticache_subnet_group.sail_cache_subnet_group.name
  security_group_ids   = [aws_security_group.redis_sg.id]
}

# EC2 Instance
resource "aws_instance" "sail_app" {
  ami           = "ami-0c55b159cbfafe1d0"  # Ubuntu 20.04
  instance_type = "t3.medium"
  
  subnet_id                   = aws_subnet.public_subnet[0].id
  vpc_security_group_ids      = [aws_security_group.app_sg.id]
  associate_public_ip_address = true
  
  key_name = var.key_pair_name
  
  user_data = file("userdata.sh")
  
  tags = {
    Name = "sail-app-server"
  }
}
```

**User Data Script (userdata.sh):**
```bash
#!/bin/bash
set -e

# Update system
apt-get update && apt-get upgrade -y

# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh
usermod -aG docker ubuntu

# Install Docker Compose
curl -L "https://github.com/docker/compose/releases/download/v2.20.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose

# Clone application
cd /opt
git clone https://github.com/tom-mcmillan/sail.git
cd sail

# Set up environment
cat > .env << EOF
DATABASE_URL=postgresql://sail:${db_password}@${rds_endpoint}:5432/sail
REDIS_URL=redis://${redis_endpoint}:6379
JWT_SECRET=${jwt_secret}
SESSION_SECRET=${session_secret}
NODE_ENV=production
DOMAIN=${domain}
EOF

# Start application
docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d
```

#### ECS Fargate Deployment

**ECS Task Definition:**
```json
{
  "family": "sail-app",
  "networkMode": "awsvpc",
  "requiresCompatibilities": ["FARGATE"],
  "cpu": "512",
  "memory": "1024",
  "executionRoleArn": "arn:aws:iam::account:role/ecsTaskExecutionRole",
  "taskRoleArn": "arn:aws:iam::account:role/ecsTaskRole",
  "containerDefinitions": [
    {
      "name": "sail-backend",
      "image": "your-account.dkr.ecr.region.amazonaws.com/sail-backend:latest",
      "portMappings": [
        {
          "containerPort": 3001,
          "protocol": "tcp"
        }
      ],
      "environment": [
        {
          "name": "NODE_ENV",
          "value": "production"
        }
      ],
      "secrets": [
        {
          "name": "DATABASE_URL",
          "valueFrom": "arn:aws:secretsmanager:region:account:secret:sail/database-url"
        },
        {
          "name": "JWT_SECRET",
          "valueFrom": "arn:aws:secretsmanager:region:account:secret:sail/jwt-secret"
        }
      ],
      "logConfiguration": {
        "logDriver": "awslogs",
        "options": {
          "awslogs-group": "/ecs/sail-app",
          "awslogs-region": "us-east-1",
          "awslogs-stream-prefix": "ecs"
        }
      }
    },
    {
      "name": "sail-frontend",
      "image": "your-account.dkr.ecr.region.amazonaws.com/sail-frontend:latest",
      "portMappings": [
        {
          "containerPort": 3000,
          "protocol": "tcp"
        }
      ],
      "environment": [
        {
          "name": "NODE_ENV",
          "value": "production"
        },
        {
          "name": "NEXT_PUBLIC_API_URL",
          "value": "https://api.yourdomain.com"
        }
      ]
    }
  ]
}
```

### Google Cloud Platform

#### GKE Deployment

**Kubernetes Configuration:**
```yaml
# namespace.yaml
apiVersion: v1
kind: Namespace
metadata:
  name: sail

---
# configmap.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: sail-config
  namespace: sail
data:
  NODE_ENV: "production"
  REDIS_URL: "redis://redis-service:6379"

---
# secret.yaml
apiVersion: v1
kind: Secret
metadata:
  name: sail-secrets
  namespace: sail
type: Opaque
data:
  DATABASE_URL: <base64-encoded-database-url>
  JWT_SECRET: <base64-encoded-jwt-secret>
  SESSION_SECRET: <base64-encoded-session-secret>

---
# deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: sail-backend
  namespace: sail
spec:
  replicas: 3
  selector:
    matchLabels:
      app: sail-backend
  template:
    metadata:
      labels:
        app: sail-backend
    spec:
      containers:
      - name: backend
        image: gcr.io/your-project/sail-backend:latest
        ports:
        - containerPort: 3001
        envFrom:
        - configMapRef:
            name: sail-config
        - secretRef:
            name: sail-secrets
        resources:
          requests:
            memory: "256Mi"
            cpu: "200m"
          limits:
            memory: "512Mi"
            cpu: "500m"
        livenessProbe:
          httpGet:
            path: /health
            port: 3001
          initialDelaySeconds: 30
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /health
            port: 3001
          initialDelaySeconds: 5
          periodSeconds: 5

---
# service.yaml
apiVersion: v1
kind: Service
metadata:
  name: sail-backend-service
  namespace: sail
spec:
  selector:
    app: sail-backend
  ports:
  - port: 80
    targetPort: 3001
  type: LoadBalancer

---
# ingress.yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: sail-ingress
  namespace: sail
  annotations:
    kubernetes.io/ingress.class: "gce"
    cert-manager.io/cluster-issuer: "letsencrypt-prod"
spec:
  tls:
  - hosts:
    - api.yourdomain.com
    - yourdomain.com
    secretName: sail-tls
  rules:
  - host: api.yourdomain.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: sail-backend-service
            port:
              number: 80
  - host: yourdomain.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: sail-frontend-service
            port:
              number: 80
```

### Azure Deployment

#### Container Apps

**Azure Container Apps Configuration:**
```yaml
# containerapp.yaml
apiVersion: v1
kind: ContainerApp
metadata:
  name: sail-app
spec:
  configuration:
    activeRevisionsMode: single
    ingress:
      external: true
      targetPort: 3001
      allowInsecure: false
    secrets:
    - name: database-url
      value: "postgresql://user:pass@server:5432/db"
    - name: jwt-secret
      value: "your-jwt-secret"
    dapr:
      enabled: false
  template:
    containers:
    - name: sail-backend
      image: youracr.azurecr.io/sail-backend:latest
      env:
      - name: DATABASE_URL
        secretRef: database-url
      - name: JWT_SECRET
        secretRef: jwt-secret
      - name: NODE_ENV
        value: "production"
      resources:
        cpu: 0.5
        memory: 1Gi
    scale:
      minReplicas: 1
      maxReplicas: 10
```

## Security Configuration

### Environment Security

1. **Secret Management**
```bash
# Use environment-specific secrets
# Development
cp .env.development .env

# Production  
cp .env.production .env

# Never commit .env files
echo ".env*" >> .gitignore
```

2. **File Permissions**
```bash
# Secure configuration files
chmod 600 .env
chmod 600 docker-compose.override.yml

# Secure application directories
chown -R www-data:www-data /opt/sail
chmod -R 755 /opt/sail
```

3. **Network Security**
```bash
# Configure firewall rules
iptables -A INPUT -p tcp --dport 22 -j ACCEPT
iptables -A INPUT -p tcp --dport 80 -j ACCEPT
iptables -A INPUT -p tcp --dport 443 -j ACCEPT
iptables -A INPUT -j DROP
```

### Application Security

1. **JWT Configuration**
```javascript
// Secure JWT settings
const jwtConfig = {
  algorithm: 'HS256',
  expiresIn: '1h',
  issuer: 'sailmcp.com',
  audience: 'sailmcp-clients',
  // Use a strong secret (256-bit minimum)
  secret: process.env.JWT_SECRET
};
```

2. **Rate Limiting**
```javascript
// Redis-based rate limiting
const rateLimitConfig = {
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100, // requests per window
  message: 'Too many requests',
  standardHeaders: true,
  legacyHeaders: false,
  store: new RedisStore({
    client: redisClient
  })
};
```

3. **CORS Configuration**
```javascript
const corsConfig = {
  origin: process.env.NODE_ENV === 'production' 
    ? ['https://sailmcp.com', 'https://api.sailmcp.com']
    : ['http://localhost:3000'],
  credentials: true,
  optionsSuccessStatus: 200
};
```

## Monitoring & Logging

### Application Monitoring

1. **Health Checks**
```javascript
// Health check endpoint
app.get('/health', async (req, res) => {
  const health = {
    status: 'healthy',
    timestamp: new Date().toISOString(),
    services: {
      database: await checkDatabaseHealth(),
      redis: await checkRedisHealth(),
      docker: await checkDockerHealth()
    }
  };
  
  const isHealthy = Object.values(health.services)
    .every(status => status === 'healthy');
    
  res.status(isHealthy ? 200 : 503).json(health);
});
```

2. **Prometheus Metrics**
```javascript
const prometheus = require('prom-client');

// Custom metrics
const httpRequestDuration = new prometheus.Histogram({
  name: 'http_request_duration_seconds',
  help: 'Duration of HTTP requests in seconds',
  labelNames: ['method', 'route', 'status']
});

const mcpRequestsTotal = new prometheus.Counter({
  name: 'mcp_requests_total',
  help: 'Total number of MCP requests',
  labelNames: ['exchange_id', 'tool', 'status']
});
```

3. **Grafana Dashboard**
```json
{
  "dashboard": {
    "title": "Sail MCP Dashboard",
    "panels": [
      {
        "title": "Request Rate",
        "type": "graph",
        "targets": [
          {
            "expr": "rate(http_requests_total[5m])",
            "legendFormat": "{{method}} {{route}}"
          }
        ]
      },
      {
        "title": "Response Time",
        "type": "graph", 
        "targets": [
          {
            "expr": "histogram_quantile(0.95, rate(http_request_duration_seconds_bucket[5m]))",
            "legendFormat": "95th percentile"
          }
        ]
      }
    ]
  }
}
```

### Centralized Logging

1. **Winston Configuration**
```javascript
const winston = require('winston');

const logger = winston.createLogger({
  level: process.env.LOG_LEVEL || 'info',
  format: winston.format.combine(
    winston.format.timestamp(),
    winston.format.errors({ stack: true }),
    winston.format.json()
  ),
  transports: [
    new winston.transports.Console(),
    new winston.transports.File({ 
      filename: 'logs/error.log', 
      level: 'error' 
    }),
    new winston.transports.File({ 
      filename: 'logs/combined.log' 
    })
  ]
});
```

2. **ELK Stack Integration**
```yaml
# docker-compose.logging.yml
version: '3.8'

services:
  elasticsearch:
    image: docker.elastic.co/elasticsearch/elasticsearch:8.8.0
    environment:
      - discovery.type=single-node
      - xpack.security.enabled=false
    volumes:
      - elasticsearch-data:/usr/share/elasticsearch/data

  logstash:
    image: docker.elastic.co/logstash/logstash:8.8.0
    volumes:
      - ./logstash.conf:/usr/share/logstash/pipeline/logstash.conf

  kibana:
    image: docker.elastic.co/kibana/kibana:8.8.0
    ports:
      - "5601:5601"
    environment:
      - ELASTICSEARCH_HOSTS=http://elasticsearch:9200

volumes:
  elasticsearch-data:
```

## Backup & Recovery

### Database Backup

1. **Automated Backup Script**
```bash
#!/bin/bash
# backup-sail.sh

set -e

# Configuration
BACKUP_DIR="/opt/sail/backups"
S3_BUCKET="sail-backups"
RETENTION_DAYS=30

# Create backup directory
mkdir -p $BACKUP_DIR

# Database backup
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
DB_BACKUP="sail_db_$TIMESTAMP.sql.gz"

pg_dump $DATABASE_URL | gzip > $BACKUP_DIR/$DB_BACKUP

# File storage backup
STORAGE_BACKUP="sail_storage_$TIMESTAMP.tar.gz"
tar -czf $BACKUP_DIR/$STORAGE_BACKUP -C /opt/sail storage/

# Upload to S3
aws s3 cp $BACKUP_DIR/$DB_BACKUP s3://$S3_BUCKET/database/
aws s3 cp $BACKUP_DIR/$STORAGE_BACKUP s3://$S3_BUCKET/storage/

# Cleanup old backups
find $BACKUP_DIR -name "sail_*" -mtime +$RETENTION_DAYS -delete

# Log completion
echo "Backup completed: $DB_BACKUP, $STORAGE_BACKUP"
```

2. **Restore Script**
```bash
#!/bin/bash
# restore-sail.sh

set -e

if [ $# -ne 1 ]; then
    echo "Usage: $0 <backup_timestamp>"
    exit 1
fi

TIMESTAMP=$1
BACKUP_DIR="/opt/sail/backups"
S3_BUCKET="sail-backups"

# Download backups from S3
aws s3 cp s3://$S3_BUCKET/database/sail_db_$TIMESTAMP.sql.gz $BACKUP_DIR/
aws s3 cp s3://$S3_BUCKET/storage/sail_storage_$TIMESTAMP.tar.gz $BACKUP_DIR/

# Stop application
docker-compose down

# Restore database
gunzip -c $BACKUP_DIR/sail_db_$TIMESTAMP.sql.gz | psql $DATABASE_URL

# Restore storage
tar -xzf $BACKUP_DIR/sail_storage_$TIMESTAMP.tar.gz -C /opt/sail/

# Start application
docker-compose up -d

echo "Restore completed for timestamp: $TIMESTAMP"
```

### Disaster Recovery Plan

1. **Recovery Time Objectives (RTO)**
   - **Database**: < 15 minutes
   - **Application**: < 5 minutes  
   - **Full Service**: < 30 minutes

2. **Recovery Point Objectives (RPO)**
   - **Database**: < 1 hour
   - **File Storage**: < 4 hours
   - **Configuration**: < 24 hours

3. **Disaster Recovery Procedures**
```bash
# Emergency Recovery Script
#!/bin/bash
# emergency-recovery.sh

# 1. Assess situation
echo "=== Disaster Recovery Started ==="
echo "Timestamp: $(date)"

# 2. Restore from latest backup
LATEST_BACKUP=$(aws s3 ls s3://sail-backups/database/ | tail -1 | awk '{print $4}')
./restore-sail.sh $(echo $LATEST_BACKUP | sed 's/sail_db_\(.*\)\.sql\.gz/\1/')

# 3. Verify service health
sleep 30
curl -f http://localhost:3001/health || exit 1

# 4. Notify stakeholders
echo "=== Recovery Completed Successfully ==="
# Send notification to Slack/email
```

## Troubleshooting

### Common Issues

#### Database Connection Problems

**Issue**: "Connection to database failed"
```bash
# Check database status
docker-compose ps database

# Check database logs
docker-compose logs database

# Test connection
docker-compose exec database psql -U sail -d sail -c "SELECT 1;"

# Restart database
docker-compose restart database
```

#### Docker Socket Permission Issues

**Issue**: "Cannot connect to Docker daemon socket"
```bash
# Add user to docker group
sudo usermod -aG docker $USER

# Set socket permissions
sudo chmod 666 /var/run/docker.sock

# Restart Docker service
sudo systemctl restart docker
```

#### SSL Certificate Issues

**Issue**: "SSL certificate verification failed"
```bash
# Check certificate status
openssl x509 -in /etc/letsencrypt/live/domain.com/cert.pem -text -noout

# Renew certificate
certbot renew --force-renewal

# Test SSL configuration
curl -I https://your-domain.com
```

#### Memory/Performance Issues

**Issue**: "Application running slowly or crashing"
```bash
# Check memory usage
docker stats

# Check disk space
df -h

# Analyze performance
docker-compose exec backend npm run analyze

# Scale resources
docker-compose up --scale backend=3
```

### Debug Mode

Enable debug logging for troubleshooting:

```bash
# Enable debug mode
export DEBUG=sail:*
export NODE_ENV=development
export LOG_LEVEL=debug

# Start with verbose logging
docker-compose up --verbose
```

### Support Resources

1. **Documentation**: [docs.sailmcp.com](https://docs.sailmcp.com)
2. **GitHub Issues**: [github.com/tom-mcmillan/sail/issues](https://github.com/tom-mcmillan/sail/issues)
3. **Discord Community**: [discord.gg/sailmcp](https://discord.gg/sailmcp)
4. **Professional Support**: support@sailmcp.com

---

This deployment guide covers the most common deployment scenarios for Sail MCP. For specific environments or custom requirements, please refer to the platform-specific documentation or contact support.