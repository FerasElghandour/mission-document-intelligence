# Input contract

Provide your own authorized .txt corpus. The CLI builds a temporary in-memory SQLite FTS5 index and returns passages with source labels. DocumentIndex also accepts a persistent SQLite path. answer accepts retrieved passages and a caller-supplied generation callback; no API credentials are needed for retrieval or tests. No original mission document collection, Chroma database, model output, or provider trace is included.
