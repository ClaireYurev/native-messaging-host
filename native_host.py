import sys
import json
import struct
import subprocess
import os

def main():
    while True:
        # Read message length (first 4 bytes)
        length_bytes = sys.stdin.buffer.read(4)
        if not length_bytes:
            return
        
        # Unpack message length
        length = struct.unpack('i', length_bytes)[0]
        
        # Read message
        message_bytes = sys.stdin.buffer.read(length)
        message = json.loads(message_bytes.decode('utf-8'))
        
        # Execute command
        try:
            result = subprocess.run(
                message['command'],
                shell=True,
                capture_output=True,
                text=True
            )
            response = {'success': True, 'output': result.stdout}
        except Exception as e:
            response = {'success': False, 'error': str(e)}
        
        # Send response
        response_bytes = json.dumps(response).encode('utf-8')
        sys.stdout.buffer.write(struct.pack('i', len(response_bytes)))
        sys.stdout.buffer.write(response_bytes)
        sys.stdout.buffer.flush()

if __name__ == '__main__':
    main()