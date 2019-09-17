#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import bs4, requests

with open('rosalind_mprt.txt') as f:
	# Generates list of uniprot IDs to get the protein sequence of
	uniprot_id_list = f.read().split()

protein_seq_dict = {}
for uniprot_id in uniprot_id_list:
	# Scrapes protein sequences from uniprot and creates dictionary of
	# Uniprot IDs and protein sequences
	res = requests.get('http://www.uniprot.org/uniprot/' + uniprot_id + '.fasta')
	res.raise_for_status()
	uniprotSoup = bs4.BeautifulSoup(res.text, 'lxml')
	protein_seq = uniprotSoup.select('p')
	protein_seq = protein_seq[0].getText().strip()
	protein_seq = protein_seq.split('\n')
	protein_seq.pop(0)
	protein_seq = ''.join(protein_seq)
	protein_seq_dict[uniprot_id] = protein_seq


for uniprot_id in protein_seq_dict:
	# Searches for and records position of N-glycosylation motifs
	site_list = []
	for i in range(0, len(protein_seq_dict[uniprot_id])):
		if protein_seq_dict[uniprot_id][i] == 'N':
			if i + 3 <= len(protein_seq_dict[uniprot_id]):
				# Checks if near the end of the protein sequence
				if protein_seq_dict[uniprot_id][i + 1] != 'P':
					if protein_seq_dict[uniprot_id][i + 2] == 'S' or protein_seq_dict[uniprot_id][i + 2] == 'T':
						if protein_seq_dict[uniprot_id][i + 3] != 'P':
							site_list.append(i+1)
	if len(site_list) >= 1:
		# if motif is present, prints uniprot ID and every location
		# the motif occurs.
		print(uniprot_id)
		for i in site_list:
			print(i, end=' ')
		print()
		
