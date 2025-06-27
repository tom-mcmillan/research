# Intro

I built [Sail MCP](https://sailmcp.com) to help me save the knowledge i created in my chatGPT sessions, and share that knowledge with others. I hope it's of some use to you. 

Sail is based on a few principles:

1. We want to create knowledge 

2. Knowledge is created through a process, which I believe consists of *Eliciting*, *Abstracting*, *Rendering*, and *Exchanging*. 

3. The best thoughts and ideas emerge in the intersubjective field between two subjects. 

4. LLMs are a new subject, and Sail MCP is a tool to help us make and exchange knowledge in that field. 

## Why use Sail MCP

Sail MCP helps you interact with knowledge stores (libraries, notes, code) in real time, with no set up.  Sail MCP provides:

- A growing list of pre-built integrations that your LLM can directly plug into
- The flexibility to switch between LLM providers and vendors
- Best practices for securing your data within your infrastructure

```mermaid

flowchart td


```

Sail MCP is of a set of servers (containing knowledge) and protocols (defining the exchange) that enable you to share your personal knowledge sources (local files, Google Drive, GitHub repositories) with AI assistants like Claude and ChatGPT through the Model Context Protocol (MCP). 
It implements a bidirectional knowledge flow:

- **Get**: Your knowledge flows OUT to others through Sail MCP servers.
- **Post**: Your knowledge flows IN to your personal stores from your AI conversations.


## Features

### Multiple Data Source Support
- **Local Folders**: Share files and documents from your computer
- **Google Drive**: Connect your Google Drive files and folders
- **GitHub Repositories**: Expose code repositories and documentation

### AI Assistant Integration
- **Claude Desktop**: Native MCP integration
- **ChatGPT**: MCP support through HTTP transport
- **Universal Compatibility**: Works with any MCP-compatible AI assistant

### Privacy & Security
- **Private/Public Exchanges**: Control who can access your data
- **OAuth2 Authentication**: Secure authorization flows
- **JWT-based Security**: Protected API endpoints
- **Rate Limiting**: Prevent abuse and ensure fair usage

### Management & Analytics
- **Real-time Dashboard**: Monitor your MCP servers
- **Usage Analytics**: Track requests and performance
- **Exchange Management**: Create, update, and delete MCP servers
- **Health Monitoring**: Automatic health checks and status updates

## Architecture

### System Overview
```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   AI Assistant  │    │   Sail Platform │    │ Knowledge Sources│
│                 │    │                 │    │                 │
│ • Claude        │◄──►│ • MCP Servers   │◄──►│ • Local Files   │
│ • ChatGPT       │    │ • OAuth2 Server │    │ • Google Drive  │
│ • Others        │    │ • Exchange API  │    │ • GitHub Repos  │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```
