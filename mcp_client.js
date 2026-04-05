
import { spawn } from 'child_process';

const server = spawn(process.platform === 'win32' ? 'npx.cmd' : 'npx', ['-y', 'notebooklm-mcp@latest'], {
  stdio: ['pipe', 'pipe', 'inherit']
});

let responseData = '';
server.stdout.on('data', (data) => {
  const line = data.toString();
  console.log('SERVER:', line);
  // Khi server sẵn sàng, gửi request JSON-RPC
  if (line.includes('Ready to receive requests')) {
    const request = {
      jsonrpc: '2.0',
      id: 1,
      method: 'tools/call',
      params: {
        name: 'ask_question',
        arguments: {
          question: 'Hãy tóm tắt chi tiết video YouTube này bằng tiếng Việt: https://www.youtube.com/watch?v=zlRRzhZw2Vc'
        }
      }
    };
    server.stdin.write(JSON.stringify(request) + '\n');
  }
  
  if (line.includes('"result":')) {
    console.log('SUCCESS:', line);
    process.exit(0);
  }
});

setTimeout(() => {
  console.log('Timeout waiting for MCP response.');
  server.kill();
  process.exit(1);
}, 120000);
