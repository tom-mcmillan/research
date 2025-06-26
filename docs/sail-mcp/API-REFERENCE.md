# Sail MCP API Reference

This document provides a comprehensive reference for the Sail MCP platform API endpoints, including request/response formats, authentication, and examples.

## Base URL

- **Development**: `http://localhost:3001`
- **Production**: `https://api.sailmcp.com`

## Authentication

Sail uses JWT (JSON Web Tokens) for authentication. Include your token in the Authorization header:

```
Authorization: Bearer <your-jwt-token>
```

### Obtaining a Token

```bash
POST /oauth/token
Content-Type: application/x-www-form-urlencoded

grant_type=authorization_code&
code=<authorization_code>&
client_id=<client_id>&
client_secret=<client_secret>&
redirect_uri=<redirect_uri>
```

## Rate Limiting

API requests are rate-limited to prevent abuse:

- **Authenticated users**: 100 requests per minute
- **Unauthenticated users**: 10 requests per minute

Rate limit headers are included in all responses:
```
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 95
X-RateLimit-Reset: 1640995200
```

## Error Handling

All API endpoints return errors in a consistent format:

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid request parameters",
    "details": {
      "field": "name",
      "issue": "Name is required"
    }
  }
}
```

### Common Error Codes

| Code | HTTP Status | Description |
|------|-------------|-------------|
| `VALIDATION_ERROR` | 400 | Invalid request parameters |
| `UNAUTHORIZED` | 401 | Authentication required |
| `FORBIDDEN` | 403 | Insufficient permissions |
| `NOT_FOUND` | 404 | Resource not found |
| `RATE_LIMITED` | 429 | Too many requests |
| `INTERNAL_ERROR` | 500 | Server error |

## Core API Endpoints

### Health Check

Check the API server status.

```
GET /health
```

**Response:**
```json
{
  "status": "healthy",
  "timestamp": "2024-01-01T00:00:00.000Z",
  "version": "1.0.0",
  "services": {
    "database": "connected",
    "redis": "connected",
    "mcp_servers": "operational"
  }
}
```

## Exchange Management

### List Exchanges

Retrieve all exchanges for the authenticated user.

```
GET /api/exchanges
```

**Query Parameters:**
- `limit` (optional): Number of results (default: 50, max: 100)
- `offset` (optional): Pagination offset (default: 0)
- `type` (optional): Filter by exchange type (`local`, `google-drive`, `github`)
- `status` (optional): Filter by status (`active`, `processing`, `error`, `stopped`)

**Response:**
```json
{
  "exchanges": [
    {
      "id": "550e8400-e29b-41d4-a716-446655440000",
      "name": "My Documents",
      "description": "Personal document collection",
      "type": "local",
      "status": "active",
      "privacy": "private",
      "mcpUrl": "http://localhost:3001/mcp/550e8400-e29b-41d4-a716-446655440000",
      "config": {
        "folderPath": "/home/user/documents"
      },
      "analytics": {
        "totalRequests": 42,
        "lastAccessed": "2024-01-01T12:00:00.000Z"
      },
      "createdAt": "2024-01-01T00:00:00.000Z",
      "updatedAt": "2024-01-01T12:00:00.000Z"
    }
  ],
  "pagination": {
    "total": 1,
    "limit": 50,
    "offset": 0,
    "hasMore": false
  }
}
```

### Create Exchange

Create a new MCP exchange.

```
POST /api/exchanges
Content-Type: application/json
```

**Request Body:**
```json
{
  "name": "My GitHub Repos",
  "description": "Access to my GitHub repositories",
  "type": "github",
  "privacy": "public",
  "config": {
    "owner": "username",
    "repos": ["repo1", "repo2"],
    "includeForks": false
  }
}
```

**Response:**
```json
{
  "id": "550e8400-e29b-41d4-a716-446655440001",
  "name": "My GitHub Repos",
  "description": "Access to my GitHub repositories",
  "type": "github",
  "status": "processing",
  "privacy": "public",
  "mcpUrl": "http://localhost:3001/mcp/550e8400-e29b-41d4-a716-446655440001",
  "config": {
    "owner": "username",
    "repos": ["repo1", "repo2"],
    "includeForks": false
  },
  "createdAt": "2024-01-01T00:00:00.000Z",
  "updatedAt": "2024-01-01T00:00:00.000Z"
}
```

### Get Exchange Details

Retrieve details for a specific exchange.

```
GET /api/exchanges/{exchangeId}
```

**Response:**
```json
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "name": "My Documents",
  "description": "Personal document collection",
  "type": "local",
  "status": "active",
  "privacy": "private",
  "mcpUrl": "http://localhost:3001/mcp/550e8400-e29b-41d4-a716-446655440000",
  "config": {
    "folderPath": "/home/user/documents"
  },
  "analytics": {
    "totalRequests": 42,
    "lastAccessed": "2024-01-01T12:00:00.000Z",
    "topQueries": [
      "search project files",
      "find readme"
    ]
  },
  "resources": [
    {
      "id": "doc1.pdf",
      "name": "Project Documentation",
      "type": "document",
      "path": "/documents/project/doc1.pdf",
      "size": 2048,
      "lastModified": "2024-01-01T00:00:00.000Z"
    }
  ],
  "createdAt": "2024-01-01T00:00:00.000Z",
  "updatedAt": "2024-01-01T12:00:00.000Z"
}
```

### Update Exchange

Update an existing exchange.

```
PUT /api/exchanges/{exchangeId}
Content-Type: application/json
```

**Request Body:**
```json
{
  "name": "Updated Name",
  "description": "Updated description",
  "privacy": "public",
  "config": {
    "folderPath": "/home/user/new-documents"
  }
}
```

**Response:**
```json
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "name": "Updated Name",
  "description": "Updated description",
  "privacy": "public",
  "status": "processing",
  "updatedAt": "2024-01-01T12:30:00.000Z"
}
```

### Delete Exchange

Delete an exchange and clean up associated resources.

```
DELETE /api/exchanges/{exchangeId}
```

**Response:**
```json
{
  "message": "Exchange deleted successfully",
  "deletedAt": "2024-01-01T12:00:00.000Z"
}
```

## MCP Protocol Endpoints

### JSON-RPC Requests

Send MCP JSON-RPC requests to an exchange.

```
POST /mcp/{exchangeId}
Content-Type: application/json
```

**Request Body (Initialize):**
```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "initialize",
  "params": {
    "protocolVersion": "2024-11-05",
    "capabilities": {
      "tools": {},
      "resources": {}
    },
    "clientInfo": {
      "name": "Claude Desktop",
      "version": "1.0.0"
    }
  }
}
```

**Response:**
```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "protocolVersion": "2024-11-05",
    "capabilities": {
      "tools": {
        "listChanged": true
      },
      "resources": {
        "subscribe": true,
        "listChanged": true
      }
    },
    "serverInfo": {
      "name": "SailMCP Server",
      "version": "1.0.0"
    }
  }
}
```

### List Available Tools

```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "method": "tools/list"
}
```

**Response:**
```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "result": {
    "tools": [
      {
        "name": "search",
        "description": "Search for documents and files",
        "inputSchema": {
          "type": "object",
          "properties": {
            "query": {
              "type": "string",
              "description": "Search query"
            },
            "limit": {
              "type": "number",
              "description": "Maximum number of results",
              "default": 10
            }
          },
          "required": ["query"]
        }
      },
      {
        "name": "fetch",
        "description": "Fetch content of a specific document",
        "inputSchema": {
          "type": "object",
          "properties": {
            "id": {
              "type": "string",
              "description": "Document ID"
            }
          },
          "required": ["id"]
        }
      }
    ]
  }
}
```

### Search Tool

```json
{
  "jsonrpc": "2.0",
  "id": 3,
  "method": "tools/call",
  "params": {
    "name": "search",
    "arguments": {
      "query": "project documentation",
      "limit": 5
    }
  }
}
```

**Response:**
```json
{
  "jsonrpc": "2.0",
  "id": 3,
  "result": {
    "content": [
      {
        "type": "text",
        "text": "Found 3 documents matching 'project documentation':\n\n1. README.md - Main project documentation\n2. SETUP.md - Setup and installation guide\n3. API.md - API reference documentation"
      }
    ],
    "isError": false
  }
}
```

### Fetch Tool

```json
{
  "jsonrpc": "2.0",
  "id": 4,
  "method": "tools/call",
  "params": {
    "name": "fetch",
    "arguments": {
      "id": "README.md"
    }
  }
}
```

**Response:**
```json
{
  "jsonrpc": "2.0",
  "id": 4,
  "result": {
    "content": [
      {
        "type": "text",
        "text": "# My Project\n\nThis is the main documentation for my project...\n\n## Installation\n\n```bash\nnpm install\n```"
      }
    ],
    "isError": false
  }
}
```

### Server-Sent Events Connection

Establish a persistent connection for real-time updates.

```
GET /mcp/{exchangeId}
Accept: text/event-stream
```

**Response Stream:**
```
event: session_created
data: {"sessionId": "sess_123", "exchangeId": "550e8400-e29b-41d4-a716-446655440000"}

event: server_ready
data: {"status": "ready", "capabilities": {"tools": true, "resources": true}}

event: heartbeat
data: {"timestamp": "2024-01-01T12:00:00.000Z"}
```

## OAuth2 Authorization Server

### Authorization Endpoint

Initiate OAuth2 authorization flow.

```
GET /oauth/authorize?response_type=code&client_id=<client_id>&redirect_uri=<redirect_uri>&scope=<scope>&state=<state>
```

**Query Parameters:**
- `response_type`: Must be `code`
- `client_id`: Your application's client ID
- `redirect_uri`: Callback URL (must be registered)
- `scope`: Requested permissions (e.g., `read write`)
- `state`: CSRF protection token
- `code_challenge` (optional): PKCE code challenge
- `code_challenge_method` (optional): PKCE challenge method

**Response:**
Redirects to `redirect_uri` with authorization code:
```
https://your-app.com/callback?code=<authorization_code>&state=<state>
```

### Token Endpoint

Exchange authorization code for access token.

```
POST /oauth/token
Content-Type: application/x-www-form-urlencoded
```

**Request Body:**
```
grant_type=authorization_code&
code=<authorization_code>&
client_id=<client_id>&
client_secret=<client_secret>&
redirect_uri=<redirect_uri>&
code_verifier=<code_verifier>
```

**Response:**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "Bearer",
  "expires_in": 3600,
  "refresh_token": "refresh_token_here",
  "scope": "read write"
}
```

### Token Introspection

Validate and get information about a token.

```
POST /oauth/introspect
Content-Type: application/x-www-form-urlencoded
Authorization: Basic <base64(client_id:client_secret)>
```

**Request Body:**
```
token=<access_token>
```

**Response:**
```json
{
  "active": true,
  "client_id": "your_client_id",
  "username": "user@example.com",
  "scope": "read write",
  "exp": 1640995200,
  "iat": 1640991600,
  "sub": "550e8400-e29b-41d4-a716-446655440000"
}
```

### Dynamic Client Registration

Register a new OAuth2 client.

```
POST /oauth/register
Content-Type: application/json
```

**Request Body:**
```json
{
  "client_name": "My Application",
  "client_uri": "https://my-app.com",
  "redirect_uris": [
    "https://my-app.com/callback",
    "https://my-app.com/oauth/callback"
  ],
  "scope": "read write",
  "grant_types": ["authorization_code", "refresh_token"],
  "response_types": ["code"],
  "token_endpoint_auth_method": "client_secret_basic"
}
```

**Response:**
```json
{
  "client_id": "generated_client_id",
  "client_secret": "generated_client_secret",
  "client_name": "My Application",
  "client_uri": "https://my-app.com",
  "redirect_uris": [
    "https://my-app.com/callback",
    "https://my-app.com/oauth/callback"
  ],
  "scope": "read write",
  "grant_types": ["authorization_code", "refresh_token"],
  "response_types": ["code"],
  "token_endpoint_auth_method": "client_secret_basic",
  "client_id_issued_at": 1640991600,
  "client_secret_expires_at": 0
}
```

## Exchange Type Configurations

### Local Folder Exchange

```json
{
  "type": "local",
  "config": {
    "folderPath": "/home/user/documents",
    "includeHidden": false,
    "fileTypes": ["pdf", "txt", "md", "docx"],
    "maxFileSize": 10485760,
    "excludePatterns": ["node_modules", ".git", "*.tmp"]
  }
}
```

### Google Drive Exchange

```json
{
  "type": "google-drive",
  "config": {
    "folderId": "1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms",
    "includeShared": true,
    "fileTypes": ["document", "spreadsheet", "presentation"],
    "recursive": true,
    "maxResults": 1000
  }
}
```

### GitHub Repository Exchange

```json
{
  "type": "github",
  "config": {
    "owner": "username",
    "repos": ["repo1", "repo2"],
    "includeForks": false,
    "includePrivate": true,
    "fileTypes": ["md", "txt", "js", "ts", "py"],
    "excludePaths": ["node_modules", "dist", "build"]
  }
}
```

## Webhooks

### Exchange Status Updates

Receive notifications when exchange status changes.

**Webhook URL Configuration:**
```json
{
  "webhookUrl": "https://your-app.com/webhooks/sail",
  "events": ["exchange.created", "exchange.updated", "exchange.deleted", "exchange.error"]
}
```

**Webhook Payload:**
```json
{
  "event": "exchange.updated",
  "timestamp": "2024-01-01T12:00:00.000Z",
  "data": {
    "exchangeId": "550e8400-e29b-41d4-a716-446655440000",
    "status": "active",
    "previousStatus": "processing"
  }
}
```

## SDK Examples

### JavaScript/Node.js

```javascript
const SailMCP = require('@sailmcp/sdk');

const client = new SailMCP({
  apiUrl: 'http://localhost:3001',
  accessToken: 'your_access_token'
});

// Create an exchange
const exchange = await client.exchanges.create({
  name: 'My Documents',
  type: 'local',
  config: {
    folderPath: '/home/user/documents'
  }
});

// Search documents
const results = await client.mcp.search(exchange.id, {
  query: 'project documentation',
  limit: 10
});

console.log('Search results:', results);
```

### Python

```python
from sailmcp import SailMCPClient

client = SailMCPClient(
    api_url='http://localhost:3001',
    access_token='your_access_token'
)

# Create an exchange
exchange = client.exchanges.create({
    'name': 'My Documents',
    'type': 'local',
    'config': {
        'folderPath': '/home/user/documents'
    }
})

# Search documents
results = client.mcp.search(exchange['id'], {
    'query': 'project documentation',
    'limit': 10
})

print('Search results:', results)
```

## Testing

### Postman Collection

A complete Postman collection is available at:
`https://api.sailmcp.com/postman/collection.json`

### cURL Examples

```bash
# Create an exchange
curl -X POST http://localhost:3001/api/exchanges \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your_token" \
  -d '{
    "name": "Test Exchange",
    "type": "local",
    "config": {"folderPath": "/tmp/test"}
  }'

# Search via MCP
curl -X POST http://localhost:3001/mcp/exchange_id \
  -H "Content-Type: application/json" \
  -d '{
    "jsonrpc": "2.0",
    "id": 1,
    "method": "tools/call",
    "params": {
      "name": "search",
      "arguments": {"query": "test"}
    }
  }'
```

## Troubleshooting

### Common Issues

1. **401 Unauthorized**: Check your access token
2. **429 Rate Limited**: Reduce request frequency
3. **500 Internal Error**: Check server logs
4. **MCP Connection Failed**: Verify exchange status

### Debug Headers

Include debug headers for troubleshooting:

```
X-Debug-Mode: true
X-Trace-Id: your-trace-id
```

### Support

For API support, please:
1. Check the [troubleshooting guide](docs/troubleshooting.md)
2. Open an issue on [GitHub](https://github.com/tom-mcmillan/sail/issues)
3. Contact support at support@sailmcp.com