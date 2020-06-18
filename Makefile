LAGUAGE=python
RUN_SRC=protein_interaction_domain.py
RUN_EXE=$(LAGUAGE) $(RUN_SRC)
NET_FILE=9606.protein.links.v11.0.txt

## execute : execute the python
execute : $(RUN_SRC) $(NET_FILE)
	$(RUN_EXE)


## download : download protein interaction 
.PHONY: download
download : $(NET_FILE)
$(NET_FILE) : 
	wget https://stringdb-static.org/download/protein.links.v11.0/9606.protein.links.v11.0.txt.gz 
	gzip -d 9606.protein.links.v11.0.txt.gz
