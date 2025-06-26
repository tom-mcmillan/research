# MCP Integration Guide

This document provides detailed information about Sail's Model Context Protocol (MCP) integration, including implementation details, protocol compliance, and integration examples.


## Overview

Sail implements the Model Context Protocol (MCP) to enable seamless integration between personal knowledge sources and AI assistants. The implementation supports both the standard MCP specification and AI assistant-specific variants.

### Key Features

- **Full MCP Compliance**: Implements MCP specification version 2024-11-05
- **Dual Transport Support**: JSON-RPC over HTTP and Server-Sent Events
- **Multi-Client Support**: Claude Desktop, ChatGPT, and generic MCP clients
- **Dynamic Server Management**: Docker-based MCP server instances
- **Real-time Communication**: WebSocket-like experience via SSE
- **Protocol Extension**: Custom tools and resources for enhanced functionality

## MCP Protocol Implementation

### Supported MCP Features

| Feature | Status | Description |
|---------|---------|-------------|
| **Tools** | ✅ Full | Dynamic tool discovery and execution |
| **Resources** | ✅ Full | File and document resource exposure |
| **Prompts** | ❌ Planned | Template-based prompt management |
| **Sampling** | ❌ Not Planned | LLM text generation |
| **Logging** | ✅ Partial | Request/response logging |
| **Progress** | ✅ Full | Long-running operation progress |

### Protocol Versions

- **Current**: `2024-11-05` (MCP v1.0)
- **Backward Compatibility**: `2024-06-25` (MCP v0.x)
- **Future Support**: Will support upcoming MCP versions

## Architecture

### System Overview

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   AI Assistant  │    │  Sail Platform  │    │ Knowledge Store │
│                 │    │                 │    │                 │
│  ┌───────────┐  │    │  ┌───────────┐  │    │  ┌───────────┐  │
│  │ MCP Client│◄─┼────┼─►│MCP Server │◄─┼────┼─►│Local Files│  │
│  └───────────┘  │    │  └───────────┘  │    │  └───────────┘  │
│                 │    │       │        │    │  ┌───────────┐  │
│                 │    │  ┌────▼────┐   │    │  │Google Drive│  │
│                 │    │  │Transport│   │    │  └───────────┘  │
│                 │    │  │ Layer   │   │    │  ┌───────────┐  │
│                 │    │  └─────────┘   │    │  │GitHub Repo│  │
│                 │    │                │    │  └───────────┘  │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

### Component Architecture

#### MCP Server (`backend/src/services/mcp/server.ts`)
- **Core Logic**: Implements MCP protocol message handling
- **Tool Registration**: Dynamic tool discovery and execution
- **Resource Management**: Exposes documents and files as resources
- **State Management**: Session state and client tracking

#### Transport Layer (`backend/src/services/mcp/transport.ts`)
- **HTTP Transport**: JSON-RPC over HTTP
- **SSE Transport**: Server-Sent Events for real-time communication
- **Session Management**: Client session lifecycle
- **Message Queuing**: Offline message handling

#### Exchange Controller (`backend/src/controllers/mcpController.ts`)
- **Request Routing**: Routes MCP requests to appropriate servers
- **Instance Management**: Creates and manages MCP server instances
- **Protocol Adaptation**: Handles different AI assistant requirements
- **Analytics Tracking**: Request logging and performance metrics

## Transport Layer

### JSON-RPC over HTTP

The primary transport mechanism uses HTTP POST requests with JSON-RPC payloads.

#### Request Format

```http
POST /mcp/{exchangeId}
Content-Type: application/json
Authorization: Bearer <token>

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

#### Response Format

```http
HTTP/1.1 200 OK
Content-Type: application/json

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

### Server-Sent Events (SSE)

For real-time communication and long-running operations, Sail uses Server-Sent Events.

#### Connection Setup

```http
GET /mcp/{exchangeId}
Accept: text/event-stream
Authorization: Bearer <token>
```

#### Event Stream

```
event: session_created
data: {"sessionId": "sess_123", "exchangeId": "exchange_456"}

event: server_ready  
data: {"capabilities": {"tools": ["search", "fetch"], "resources": true}}

event: tool_progress
data: {"toolCallId": "call_789", "progress": 0.5, "message": "Processing..."}

event: heartbeat
data: {"timestamp": "2024-01-01T12:00:00.000Z"}
```

### Session Management

Each MCP connection maintains a session with the following lifecycle:

1. **Initialization**: Client connects and negotiates capabilities
2. **Authentication**: Token validation and user context setup
3. **Operation**: Tool calls and resource access
4. **Heartbeat**: Periodic connectivity checks
5. **Cleanup**: Session termination and resource cleanup

```typescript
interface MCPSession {
  id: string;
  exchangeId: string;
  userId?: string;
  clientInfo: {
    name: string;
    version: string;
  };
  capabilities: MCPCapabilities;
  createdAt: Date;
  lastActivity: Date;
  status: 'initializing' | 'ready' | 'error' | 'closed';
}
```

## Server Implementation

### Core MCP Server Class

```typescript
export class SailMCPServer {
  private server: Server;
  private tools: Map<string, MCPTool>;
  private resources: Map<string, MCPResource>;
  
  constructor(private exchange: Exchange) {
    this.server = new Server({
      name: 'SailMCP Server',
      version: '1.0.0'
    }, {
      capabilities: {
        tools: { listChanged: true },
        resources: { subscribe: true, listChanged: true }
      }
    });
    
    this.setupTools();
    this.setupResources();
  }
}
```

### Tool Implementation

#### Search Tool

```typescript
{
  name: 'search',
  description: 'Search for documents and files within the exchange',
  inputSchema: {
    type: 'object',
    properties: {
      query: {
        type: 'string',
        description: 'Search query string'
      },
      limit: {
        type: 'number',
        description: 'Maximum number of results to return',
        default: 10,
        minimum: 1,
        maximum: 100
      },
      fileTypes: {
        type: 'array',
        items: { type: 'string' },
        description: 'Filter by file types (e.g., ["pdf", "txt"])'
      }
    },
    required: ['query']
  }
}
```

**Implementation:**
```typescript
async function handleSearchTool(args: SearchArgs): Promise<ToolResult> {
  const { query, limit = 10, fileTypes } = args;
  
  try {
    const searchService = new SearchService(exchange);
    const results = await searchService.search({
      query,
      limit,
      fileTypes,
      userId: session.userId
    });
    
    return {
      content: [{
        type: 'text',  
        text: formatSearchResults(results)
      }],
      isError: false
    };
  } catch (error) {
    return {
      content: [{
        type: 'text',
        text: `Search failed: ${error.message}`
      }],
      isError: true
    };
  }
}
```

#### Fetch Tool  

```typescript
{
  name: 'fetch',
  description: 'Fetch the content of a specific document by ID',
  inputSchema: {
    type: 'object',
    properties: {
      id: {
        type: 'string',
        description: 'Document ID from search results'
      },
      format: {
        type: 'string',
        enum: ['text', 'markdown', 'html'],
        description: 'Output format for the document content',
        default: 'text'
      }
    },
    required: ['id']
  }
}
```

**Implementation:**
```typescript
async function handleFetchTool(args: FetchArgs): Promise<ToolResult> {
  const { id, format = 'text' } = args;
  
  try {
    const document = await documentService.getById(id);
    if (!document) {
      throw new Error(`Document not found: ${id}`);
    }
    
    const content = await documentService.getContent(document, format);
    
    return {
      content: [{
        type: 'text',
        text: content
      }],
      isError: false
    };
  } catch (error) {
    return {
      content: [{
        type: 'text', 
        text: `Failed to fetch document: ${error.message}`
      }],
      isError: true
    };
  }
}
```

### Resource Implementation

Resources expose documents and files directly to MCP clients.

```typescript
interface MCPResource {
  uri: string;
  name: string;
  description?: string;
  mimeType?: string;
  annotations?: {
    audience?: string[];
    priority?: number;
  };
}
```

**Example Resource:**
```typescript
{
  uri: "file:///documents/readme.md",
  name: "Project README",
  description: "Main project documentation",
  mimeType: "text/markdown",
  annotations: {
    audience: ["user"],
    priority: 1
  }
}
```

## Client Integration

### Claude Desktop Integration

Claude Desktop requires a specific configuration format:

#### Manual Configuration (`claude_desktop_config.json`)

```json
{
  "mcpServers": {
    "sail-exchange": {
      "command": "node",
      "args": ["/path/to/mcp-client.js"],
      "env": {
        "SAIL_MCP_URL": "http://localhost:3001/mcp/your-exchange-id",
        "SAIL_ACCESS_TOKEN": "your-access-token"
      }
    }
  }
}
```

#### MCP Client Script (`mcp-client.js`)

```javascript
const { Client } = require('@modelcontextprotocol/sdk/client/index.js');
const { SSEClientTransport } = require('@modelcontextprotocol/sdk/client/sse.js');

async function main() {
  const transport = new SSEClientTransport(
    new URL(process.env.SAIL_MCP_URL)
  );
  
  const client = new Client({
    name: "Claude Desktop",
    version: "1.0.0"
  }, {
    capabilities: {
      tools: {},
      resources: {}
    }
  });

  await client.connect(transport);
  
  // The client will now be available to Claude Desktop
  process.stdin.resume();
}

main().catch(console.error);
```

### ChatGPT Integration

ChatGPT uses a different MCP implementation approach:

#### HTTP-Only Transport

```javascript
const express = require('express');
const app = express();

app.use('/mcp', async (req, res) => {
  const response = await fetch(`http://localhost:3001/mcp/${exchangeId}`, {
    method: req.method,
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${accessToken}`
    },
    body: JSON.stringify(req.body)
  });
  
  const data = await response.json();
  res.json(data);
});

app.listen(3002);
```

#### ChatGPT Actions Configuration

```yaml
openapi: 3.0.0
info:
  title: Sail MCP Proxy
  version: 1.0.0
servers:
  - url: http://localhost:3002
paths:
  /mcp:
    post:
      operationId: mcp_request
      summary: Send MCP JSON-RPC request
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
      responses:
        '200':
          description: MCP response
          content:
            application/json:
              schema:
                type: object
```

## AI Assistant Integration

### Supported AI Assistants

| Assistant | Integration Method | Status | Features |
|-----------|-------------------|---------|----------|
| **Claude Desktop** | Native MCP | ✅ Full | Tools, Resources, SSE |
| **ChatGPT** | Actions/HTTP | ✅ Full | Tools via HTTP proxy |
| **Cursor** | MCP Extension | 🔄 Beta | Tools, basic resources |
| **VSCode Copilot** | Extension | 📋 Planned | Tools integration |
| **Generic MCP** | Standard Protocol | ✅ Full | Full MCP compliance |

### Integration Examples

#### Claude Desktop - Advanced Usage

```typescript
// Claude Desktop automatically discovers tools
// Users can directly ask: "Search for project documentation"
// Claude will call the search tool and present results

// Example interaction:
User: "Find all TypeScript files related to authentication"

Claude: [Calls search tool with query="authentication TypeScript files"]
Tool Response: "Found 5 files: authController.ts, authMiddleware.ts, ..."

Claude: "I found 5 TypeScript files related to authentication:
1. authController.ts - Main authentication controller
2. authMiddleware.ts - Authentication middleware
..."

User: "Show me the contents of authController.ts"

Claude: [Calls fetch tool with id="authController.ts"]  
Tool Response: [Full file contents]

Claude: "Here's the content of authController.ts: [formatted code]"
```

#### ChatGPT - Actions Integration

```yaml
# actions.yaml for ChatGPT
actions:
  - name: search_documents
    description: Search through personal documents
    parameters:
      query:
        type: string
        description: Search query
    implementation:
      type: http
      url: http://localhost:3002/mcp
      method: POST
      body:
        jsonrpc: "2.0"
        method: "tools/call"
        params:
          name: "search"
          arguments:
            query: "{{query}}"
```

### Error Handling & Fallbacks

#### Connection Failures
```typescript
class MCPConnectionManager {
  private retryAttempts = 3;
  private retryDelay = 1000;
  
  async connectWithRetry(transport: Transport): Promise<void> {
    for (let attempt = 1; attempt <= this.retryAttempts; attempt++) {
      try {
        await this.client.connect(transport);
        return;
      } catch (error) {
        if (attempt === this.retryAttempts) {
          throw new Error(`Failed to connect after ${this.retryAttempts} attempts`);
        }
        await this.delay(this.retryDelay * attempt);
      }
    }
  }
}
```

#### Tool Call Failures
```typescript
async function safeToolCall(toolName: string, args: any): Promise<ToolResult> {
  try {
    return await this.callTool(toolName, args);
  } catch (error) {
    return {
      content: [{
        type: 'text',
        text: `Tool "${toolName}" failed: ${error.message}. Please try again or use a different approach.`
      }],
      isError: true
    };
  }
}
```

## Security & Authentication

### Authentication Flow

1. **Token Validation**: Every MCP request validates the bearer token
2. **User Context**: Authenticated user context is attached to all operations
3. **Permission Checks**: Exchange access permissions are verified
4. **Rate Limiting**: Per-user and per-exchange rate limits are enforced

### Security Headers

```typescript
const securityHeaders = {
  'X-Content-Type-Options': 'nosniff',
  'X-Frame-Options': 'DENY',
  'X-XSS-Protection': '1; mode=block',
  'Strict-Transport-Security': 'max-age=31536000; includeSubDomains',
  'Content-Security-Policy': "default-src 'self'"
};
```

### Data Privacy

- **Encryption**: All data in transit uses TLS 1.3
- **Isolation**: Each exchange runs in an isolated Docker container
- **Access Control**: Granular permissions per exchange and user
- **Audit Logging**: All MCP requests are logged for security monitoring

## Performance & Scaling

### Optimization Strategies

#### Connection Pooling
```typescript
class MCPConnectionPool {
  private pools: Map<string, ConnectionPool> = new Map();
  
  async getConnection(exchangeId: string): Promise<MCPConnection> {
    const pool = this.getOrCreatePool(exchangeId);
    return await pool.acquire();
  }
  
  private getOrCreatePool(exchangeId: string): ConnectionPool {
    if (!this.pools.has(exchangeId)) {
      this.pools.set(exchangeId, new ConnectionPool({
        min: 1,
        max: 10,
        idleTimeoutMillis: 30000
      }));
    }
    return this.pools.get(exchangeId)!;
  }
}
```

#### Response Caching
```typescript
class MCPResponseCache {
  private cache = new Map<string, CacheEntry>();
  
  async get(key: string): Promise<any> {
    const entry = this.cache.get(key);
    if (entry && entry.expiresAt > Date.now()) {
      return entry.data;
    }
    return null;
  }
  
  set(key: string, data: any, ttlMs: number = 300000): void {
    this.cache.set(key, {
      data,
      expiresAt: Date.now() + ttlMs
    });
  }
}
```

#### Horizontal Scaling

- **Load Balancing**: Multiple Sail instances behind a load balancer
- **Session Affinity**: Sticky sessions for MCP connections
- **Distributed Caching**: Redis for shared cache across instances
- **Database Replication**: Read replicas for improved performance

### Performance Metrics

| Metric | Target | Current | 
|--------|--------|---------|
| MCP Connection Setup | < 100ms | ~50ms |
| Tool Call Latency | < 500ms | ~200ms |
| Search Response Time | < 1000ms | ~300ms |
| Document Fetch Time | < 200ms | ~100ms |
| Concurrent Connections | 1000+ | Tested to 500 |

## Troubleshooting

### Common Issues

#### Connection Problems

**Issue**: "Failed to connect to MCP server"
```bash
# Check server status
curl http://localhost:3001/health

# Check exchange status
curl -H "Authorization: Bearer $TOKEN" \
     http://localhost:3001/api/exchanges/$EXCHANGE_ID

# Check MCP endpoint
curl -H "Authorization: Bearer $TOKEN" \
     http://localhost:3001/mcp/$EXCHANGE_ID
```

**Solution**: Verify server is running and exchange is active

#### Authentication Errors

**Issue**: "Unauthorized MCP request"
```bash
# Verify token
curl -H "Authorization: Bearer $TOKEN" \
     http://localhost:3001/oauth/introspect \
     -d "token=$TOKEN"
```

**Solution**: Refresh access token or check token permissions

#### Tool Call Failures

**Issue**: "Tool 'search' not found"
```bash
# List available tools
curl -X POST http://localhost:3001/mcp/$EXCHANGE_ID \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer $TOKEN" \
     -d '{"jsonrpc":"2.0","id":1,"method":"tools/list"}'
```

**Solution**: Verify tool registration and exchange configuration

### Debug Mode

Enable debug logging for detailed troubleshooting:

```bash
# Environment variable
DEBUG=sail:mcp:* npm start

# Or programmatically
process.env.DEBUG = 'sail:mcp:*';
```

Debug output includes:
- MCP message traces
- Tool call parameters and responses
- Session lifecycle events
- Error stack traces

### Monitoring Dashboard

Access the built-in monitoring dashboard at `/admin/mcp-monitor` to view:

- Active MCP connections
- Tool call statistics
- Error rates and patterns
- Performance metrics
- Session activity logs

## Best Practices

### Client Implementation

1. **Connection Management**: Implement connection pooling and retry logic
2. **Error Handling**: Gracefully handle tool failures and network issues  
3. **Caching**: Cache frequently accessed resources locally
4. **Rate Limiting**: Respect server rate limits and implement backoff
5. **Security**: Always use HTTPS and validate server certificates

### Server Configuration

1. **Resource Limits**: Configure appropriate Docker resource limits
2. **Monitoring**: Set up comprehensive logging and alerting
3. **Backup Strategy**: Regular backups of exchange configurations
4. **Security Updates**: Keep dependencies and base images updated
5. **Load Testing**: Regular performance testing under load

### Development Workflow

1. **Local Testing**: Use local MCP client for development
2. **Integration Testing**: Test with actual AI assistants
3. **Performance Profiling**: Monitor resource usage and response times
4. **Security Scanning**: Regular security audits and vulnerability scans
5. **Documentation**: Keep MCP integration docs updated

---
