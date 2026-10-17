"""Offline example using the public implementation; see README for evidence scope."""
import sys
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "src"))
os.chdir(ROOT)

from document_intelligence import DocumentIndex, answer
# Fictional document and deterministic callback; no provider call.
index = DocumentIndex()
index.add('demo.txt', 'A fictional mission tests an oxygen supply system.')
hits = index.search('oxygen')
result = answer('What is tested?', hits, lambda prompt: 'An oxygen supply system [S1].')
index.close()

import json
print(json.dumps(result, indent=2))

