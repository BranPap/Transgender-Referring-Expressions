#!/usr/local/bin/python

from collections import defaultdict
import math
import argparse

def myswap(inlist):
    return [inlist[1],int(inlist[0])]

parser = argparse.ArgumentParser(description='Computes the weighted log-odds-ratio, informative dirichlet prior algorithm')
parser.add_argument('-f','--first', help='Description for first counts file ', default='allBigramsBreitbart.txt')
parser.add_argument('-s','--second', help='Description for second counts file', default='allBigramsPinkNews.txt')
parser.add_argument('-p','--prior', help='Description for prior counts file', default='allBigramsInclusive.txt')
args = vars(parser.parse_args())

counts1 = defaultdict(int,[myswap(line.strip().split('_')) for line in open(args['first'])])
counts2 = defaultdict(int,[myswap(line.strip().split('_')) for line in open(args['second'])])
prior = defaultdict(int,[myswap(line.strip().split('_')) for line in open(args['prior'])])
sigmasquared = defaultdict(float)
sigma = defaultdict(float)
delta = defaultdict(float)

for bigram in prior.keys():
    prior[bigram] = int(prior[bigram] + 0.5)

for bigram in counts2.keys():
    counts1[bigram] = int(counts1[bigram] + 0.5)
    if prior[bigram] == 0:
        prior[bigram] = 1

for bigram in counts1.keys():
    counts2[bigram] = int(counts2[bigram] + 0.5)
    if prior[bigram] == 0:
        prior[bigram] = 1

n1  = sum(counts1.values())
n2  = sum(counts2.values())
nprior = sum(prior.values())

for bigram in prior.keys():
    if prior[bigram] > 0:
        l1 = float(counts1[bigram] + prior[bigram]) / (( n1 + nprior ) - (counts1[bigram] + prior[bigram]))
        l2 = float(counts2[bigram] + prior[bigram]) / (( n2 + nprior ) - (counts2[bigram] + prior[bigram]))
        sigmasquared[bigram] =  1/(float(counts1[bigram]) + float(prior[bigram])) + 1/(float(counts2[bigram]) + float(prior[bigram]))
        sigma[bigram] =  math.sqrt(sigmasquared[bigram])
        delta[bigram] = ( math.log(l1) - math.log(l2) ) / sigma[bigram]

with open("FightingOutput.txt", "w") as outputFile:
    for bigram in sorted(delta, key=delta.get):
        outputFile.write(bigram + " " + "%.3f" % delta[bigram])
        outputFile.write("\n")
