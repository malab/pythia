'''
Created on 13 Nov 2011

@author: george

Unit tests for the analysis.clustering package.
'''
import unittest
from analysis.text import TextAnalyser
from analysis.clustering.algorithms.algorithms import hierarchical, cosine
from visualizations.dendrogram import Dendrogram

class TestHierarchicalClustering(unittest.TestCase):
    
    def test_hierarchical(self):
        doc0 = 'This is a document related to sports : Football, basketball, tennis, golf etc.' 
        doc1 = 'In this document we will be talking about basketball, football, tennis, golf and sports in general.'
        doc2 = 'I like golf but football is really an amazing sport. I love it. But I love basketball too and tennis'
        doc3 = 'This document is related to programming. More specifically Python and CPP. For more info check my blog.'
        doc4 = 'I wrote a small Python script to run a clustering algorithm. I hope it works well . If not Ill try CPP' 
        doc5 = 'This blog writes about Python and programming in general.'
        
        #=======================================================================
        # doc0 = 'Hello Hello Hello Hello Hello Hello '
        # doc1 = 'Hello Hello Hello Hello Hello Hello '
        # doc2 = 'Hello Hello Hello Hello Hello Hello ' 
        # doc3 = 'Bye Bye Bye Bye Bye '
        # doc4 = 'Bye Bye Bye Bye Bye '
        # doc5 = 'Bye Bye Bye Bye Bye ' 
        #=======================================================================
    
        sample_docs = [doc0, doc1, doc2, doc3, doc4, doc5]

        analyser = TextAnalyser()
        for s in sample_docs:
            analyser.add_document(s)
            
        analyser.save_frequency_matrix("test.txt")
        rownames, colnames, data = analyser.read_frequency_matrix("test.txt")
        
        cluster = hierarchical(data, cosine)
        cluster.print_it(rownames)
        
        dendro = Dendrogram(cluster, rownames, "cluster,jpg", cluster.get_height(), cluster.get_depth())
        dendro.draw_node(10, cluster.get_height()/2)
        
        
if __name__ == "__main__":
    unittest.main()