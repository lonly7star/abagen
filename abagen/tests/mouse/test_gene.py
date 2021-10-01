# -*- coding: utf-8 -*-

import random
import pytest
from abagen.mouse import io, gene

# number of tests to make
RANDOM = random.Random(1234)
GENES = io.fetch_allenref_genes()

19829, 17943
def test_get_gene_info():

    # list = RANDOM.sample(range(len(GENES)), 10)
    # 36
    list_36 = [6437, 19829, 4635, 16444, 4341, 8346, 1622, 15336, 19656, 17943]
    list_36 = [17943]
    samples = GENES.loc[list_36]

    acronyms = gene.get_gene_info(id=samples['id'], attributes='acronym')
    assert sorted(acronyms['acronym']) == sorted(samples['acronym'])

    # url
    # https://api.brain-map.org/api/v2/data/Gene/query.json?criteria=%5Bacronym%24in%27Fam184b%27%2C%27F830225E14Rik%2A%27%2C%279130019P16Rik%27%2C%27Vrk1%27%2C%27Olfr1026%27%2C%27Thbs1%27%2C%27Klhdc9%27%2C%27Gjd2%27%2C%27A230044A09Rik%2A%27%2C%27Palb2%27%5D%2Cproducts%5Bid%24eq1%5D&only=name%2Cacronym&
    # https://api.brain-map.org/api/v2/data/Gene/query.json?criteria=%5Bacronym%24in%27Fam184b%27%2C%27F830225E14Rik%2A%27%2C%27Vrk1%27%2C%27Olfr1026%27%2C%27Thbs1%27%2C%27Klhdc9%27%2C%27Gjd2%27%2C%27A230044A09Rik%2A%27%2C%27Palb2%27%5D%2Cproducts%5Bid%24eq1%5D&only=name%2Cacronym&
    # https://api.brain-map.org/api/v2/data/Gene/query.json?criteria=%5Bacronym%24in%279130019P16Rik%27%5D%2Cproducts%5Bid%24eq1%5D&only=name%2Cacronym&

    # {"success": true, "id": 0, "start_row": 0, "num_rows": 11, "total_rows": 11,
    #  "msg": [{"acronym": "Thbs1", "name": "thrombospondin 1"},
    #          {"acronym": "Palb2", "name": "partner and localizer of BRCA2"},
    #          {"acronym": "A230044A09Rik*", "name": "RIKEN cDNA A230044A09 gene (non-RefSeq)"},
    #          {"acronym": "Klhdc9", "name": "kelch domain containing 9"},
    #          {"acronym": "Fam184b", "name": "family with sequence similarity 184, member B"},
    #          {"acronym": "F830225E14Rik*", "name": "RIKEN cDNA F830225E14 gene (non-RefSeq)"},
    #          {"acronym": "Vrk1", "name": "vaccinia related kinase 1"},
    #          {"acronym": "Olfr1026", "name": "olfactory receptor 1026"},
    #          {"acronym": "9130019P16Rik", "name": "RIKEN cDNA 9130019P16 gene"},
    #          {"acronym": "Gjd2", "name": "gap junction protein, delta 2"},
    #          {"acronym": "9130019P16Rik", "name": "RIKEN cDNA 9130019P16 gene"}]}

    # ["[acronym$in'Fam184b','F830225E14Rik*','9130019P16Rik','Vrk1','Olfr1026','Thbs1','Klhdc9','Gjd2','A230044A09Rik*','Palb2']", 'products[id$eq1]']
    names = gene.get_gene_info(acronym=samples['acronym'], attributes='name')
    a = sorted(names['name'])
    b = sorted(samples['name'])
    assert a == b
    # assert sorted(names['name']) == sorted(samples['name'])

    with pytest.raises(ValueError):
        gene.get_gene_info(acronym=samples['acronym'], attributes='invalid')

    # multiple attributes
    info = gene.get_gene_info(id=samples['id'], attributes=['name', 'acronym'])
    # assert sorted(acronyms['acronym']) == sorted(samples['acronym'])
    assert sorted(info['name']) == sorted(samples['name'])

    # all attributes
    info = gene.get_gene_info(acronym=samples['acronym'])
    assert len(info.columns) == 15

    # exception: invalid gene identifiers
    with pytest.raises(ValueError):
        gene.get_gene_info(id=-100000)
    with pytest.raises(ValueError):
        gene.get_gene_info(acronym='notagene')
