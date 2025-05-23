---
title: Install and Configure MCP Server
deprecated: false
hidden: true
metadata:
  title: Install and Configure - PayU MCP Server
  keywords:
    - MCP Server
    - Model Context Protocol Server
    - PayU MCP Server
  robots: index
---
This section provides detailed instructions for installing and configuring the PayU MCP Server using either standard installation or Docker.

## Standard Installation

### 1. Clone the Repository

```bash
git clone https://github.com/payu-intrepos/payu-mcp-server.git
cd payu-mcp-server
```

### 2. Install Dependencies

PayU recommends you to use `uv` for Python dependency management.

> **Note**: Using `uv` provides faster dependency resolution and more reliable package management.

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh

# Create virtual environment and activate it
uv venv
source .venv/bin/activate

# Install dependencies
uv add "mcp[cli]" httpx python-dotenv
```

Alternatively, you can use pip:

```bash
pip install -r requirements.txt
```

> **Important**: Make sure your Python version is 3.10 or higher before proceeding with the installation.

## Docker Installation

### 1. Clone the Repository

```bash
git clone https://github.com/payu-intrepos/payu-mcp-server.git
cd payu-mcp-server
```

### 2. Build Docker Image

```bash
docker build -t payu-mcp-server .
```

> 📘 Note:
>
> This step requires Docker to be installed on your system. If you don't have Docker installed, refer to the [Docker installation guide](https://docs.docker.com/get-docker/).

### 3. Run Docker Container

Run the container with your PayU credentials:

```bash
docker run -p 8888:8888 \
  -e CLIENT_ID="YOUR_CLIENT_ID" \
  -e CLIENT_SECRET="YOUR_CLIENT_SECRET" \
  -e MERCHANT_ID="YOUR_MERCHANT_ID" \
  -e PORT=8888 \
  payu-mcp-server python server.py --sse --port 8888
```

> 📘 Note:
>
> Replace `YOUR_CLIENT_ID`, `YOUR_CLIENT_SECRET`, and `YOUR_MERCHANT_ID` with your actual PayU credentials. Never share these credentials in public repositories or insecure environments.

## Connecting to MCP Client

### Add Server to MCP Client Configuration

**Example for Claude AI Desktop Client:**

Location of configuration file:

* macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
* Windows: `%APPDATA%\Claude\claude_desktop_config.json`

#### For Standard Installation:

Add the following to your configuration:

```json
{
  "mcpServers": {
    "payu-mcp-server": {
      "command": "uv",
      "args": [
        "--directory",
        "/path/to/payu-mcp-server",
        "run",
        "server.py"
      ],
      "env": {
        "CLIENT_ID": "YOUR_CLIENT_ID",
        "CLIENT_SECRET": "YOUR_CLIENT_SECRET",
        "MERCHANT_ID": "YOUR_MERCHANT_ID"
      }
    }
  }
}
```

> 📘 Note:
>
> Replace `/path/to/payu-mcp-server` with the actual path where you cloned the repository. The path should be absolute to ensure the MCP client can locate the server files correctly.

#### For Docker Installation:

Configure your MCP client to connect to the Docker container:

```json
{
  "mcpServers": {
    "payu-mcp-server": {
      "url": "http://localhost:8888"
    }
  }
}
```

> 📘 Note:
>
> If you've configured Docker to use a different port, make sure to update the URL accordingly. The port in the URL should match the port mapping specified in your Docker run command.

## Verify Installtion

After completing the installation and configuration, you can verify that everything is working correctly by:

1. Start your MCP server (either via standard installation or Docker)
2. Open your MCP-compatible client (like Claude AI Desktop)
3. Attempt a simple query such as "Create a payment link for ₹100 for testing"

> 📘 Note:
>
> If you encounter any issues during verification, check the server logs for error messages that might help identify the problem.