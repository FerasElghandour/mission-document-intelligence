from document_intelligence import chunks,DocumentIndex,answer
assert chunks('abcdef',4,1)==['abcd','def']
index=DocumentIndex();index.add('demo.txt','A fictional mission tests an oxygen supply system.')
hits=index.search('oxygen');assert len(hits)==1 and hits[0].source=='demo.txt'
good=answer('What is tested?',hits,lambda prompt:'An oxygen supply system [S1].')
assert good['citation_present'] and len(good['sources'])==1
try:answer('question',hits,lambda prompt:'Unknown claim [S99].')
except ValueError:pass
else:raise AssertionError('Invalid citation accepted')
index.add('demo.txt','Replacement document.');assert not index.search('oxygen')
assert answer('question',[],lambda prompt:1)['sources']==[]
index.close();print('Chunk overlap, retrieval, source replacement, missing evidence, and citation validation passed.')
