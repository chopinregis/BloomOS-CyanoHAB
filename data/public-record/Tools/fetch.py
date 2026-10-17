"""Download public reference files; preserve originals and an acquisition manifest."""
from pathlib import Path
import sys, json, urllib.request, hashlib, datetime
ROOT = Path(__file__).resolve().parents[1]
def fetch(url, relative):
    dest = (ROOT / relative).resolve()
    if not dest.is_relative_to(ROOT.resolve()):
        raise ValueError('Destination outside data package')
    req = urllib.request.Request(url, headers={'User-Agent': 'BloomOS research data acquisition (public educational prototype)'})
    with urllib.request.urlopen(req, timeout=90) as response:
        body = response.read()
        resolved = response.url
        mime = response.headers.get('Content-Type')
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(body)
    record = {'file': str(dest.relative_to(ROOT)), 'source_url': url, 'resolved_url': resolved,
              'retrieved_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
              'bytes': len(body), 'content_type': mime, 'sha256': hashlib.sha256(body).hexdigest()}
    with (ROOT / 'acquisition.jsonl').open('a', encoding='utf-8') as f:
        f.write(json.dumps(record) + '\n')
    print(json.dumps(record), flush=True)
    return dest
if __name__ == '__main__':
    if sys.argv[1] == '--batch':
        for url, relative in json.loads(Path(sys.argv[2]).read_text(encoding='utf-8-sig')):
            try:
                fetch(url, relative)
            except Exception as e:
                print(json.dumps({'failed_url': url, 'error': str(e)}), flush=True)
    else:
        fetch(sys.argv[1], sys.argv[2])
