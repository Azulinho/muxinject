import libtmux
import base64

def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))


server = libtmux.Server()
session = server.find_where({"session_name": "exploit" })
pane = session.attached_pane

with open('payload.tar.gz', 'rb') as f:
    bin = f.read()

encodedBytes = base64.b64encode(bin)
seq = chunker(str(encodedBytes.decode()), 76)

pane.send_keys('mkdir -p /tmp/payload/', enter=True)
pane.send_keys('cd /tmp/payload', enter=True)

pane.send_keys('rm -f payload.tar.gz.b4', enter=True)

for chunk in seq:
    pane.send_keys(f'echo "{chunk}" >> payload.tar.gz.b4', enter=True)

pane.send_keys('base64 -d payload.tar.gz.b4 > payload.tar.gz', enter=True)
pane.send_keys('tar xzf payload.tar.gz', enter=True)
