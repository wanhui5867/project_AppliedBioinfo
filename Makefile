LAGUAGE=python
RUN_SRC=protein_interaction_domain.py
RUN_EXE=$(LAGUAGE) $(RUN_SRC)

## download : download protein interaction 
download : 9606.protein.links.v11.0.txt
	wget https://stringdb-static.org/download/protein.links.v11.0/9606.protein.links.v11.0.txt.gz 
	gzip -d 9606.protein.links.v11.0.txt.gz

## execute : execute the python
execute : $(RUN_SRC)
	$(RUN_EXE)
