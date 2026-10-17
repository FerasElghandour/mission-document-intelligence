# Mission Document Intelligence

**Feras Elghandour** · Technical case study

Answer questions about mission documentation using retrieved source passages and make answer quality inspectable.

## Implementation

A local SQLite FTS5 document index, configurable overlapping chunks, provider-neutral answer composition, and citation-label validation.

```mermaid
flowchart LR
    A[Validated inputs] --> B[Portable implementation]
    B --> C[Evaluation and contract checks]
    C --> D[Inspectable results]
```

## Completed study

The completed study used a six-question evaluation harness and configurable ingestion. The public edition exposes retrieval and citation-checking components. This source release does not claim a new live-provider evaluation; generated responses and document-store state are not distributed.

These historical figures describe the completed study. This refactored standalone implementation has separate validation and has not been used to recertify the historical benchmark. The public release contains the portable core and focused tests.

## Run locally

Python 3.11 or later.

```sh
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python smoke_test.py
python document_intelligence.py /path/to/text_corpus "mission question"
```

Prepare your own inputs as described in [DATA.md](DATA.md). Tests use generated fixtures and do not need credentials or provider calls. [VALIDATION.md](VALIDATION.md) records their scope.

## Practical relevance and limitations

Retrieval can omit relevant evidence and an LLM judge can be wrong. Citations should be checked against the source. Live generation, embeddings, and judging require credentials and may incur provider charges.

This edition makes the core behavior reusable and inspectable. Historical metrics and synthetic contract tests provide different kinds of evidence; neither establishes client deployment or commercial impact.
