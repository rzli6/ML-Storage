"""
@author: Claudio Bellei
"""

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from scipy.stats import bernoulli, norm, poisson
import sys

matplotlib.rc('font', size=20)
matplotlib.rc('font', family='Arial')

class cpt:
    def __init__(self, data = [], type = 'normal-mean'):
        # data (np array) as input 
        self.data = data
        self.labels = {"xlabel":"Days","ylabel":"Visits"}
        self.type = type

    def plot_data(self,type="ts",p=None):
        fig = plt.figure(figsize=(10,6))
        n = len(self.data)

        marker = ''
        linestyle = '-'

        plt.plot(np.arange(1,n+1),self.data,ls=linestyle,marker=marker)
        plt.xlabel(self.labels["xlabel"])
        plt.ylabel(self.labels["ylabel"])
        plt.ylim([0.9*np.min(self.data),1.1*np.max(self.data)])
        fig.set_tight_layout(True)
        if type=="cpt":
            tau = p[0]
            m1 = p[1]
            m2 = p[2]
            plt.plot([0,tau-1],[m1,m1],'r',lw=2)
            plt.plot([tau,n],[m2,m2],'r',lw=2)
            plt.plot([tau,tau],[0.9*np.min(self.data),1.1*np.max(self.data)],'r--',lw=2)
            filename = self.type + "-cpt.png"
            plt.savefig(filename,format="png")
        filename = self.type + ".png"
        plt.savefig(filename,format="png")
        plt.show()

    def plot_score(self):
        fig = plt.figure(figsize=(10,6))
        plt.plot(self.score)
        plt.xlabel(self.labels["xlabel"])
        plt.ylabel("Score")
        fig.set_tight_layout(True)
        filename = self.type + "-score.png"
        plt.ylim([0.,1.1*np.max(self.score)])
        plt.savefig(filename,format="png")
        plt.show()

    def find_changepoint(self):
        data = self.data
        n = len(data)
        tau = np.arange(1,n)
        lmbd = 2*np.log(n) #Bayesian Information Criterion
        eps = 1.e-8 #to avoid zeros in denominator
        if self.type=="normal-mean":
            mu0 = np.mean(data)
            s0 = np.sum((data-mu0)**2)
            s1 = np.asarray([np.sum((data[0:i]-np.mean(data[0:i]))**2) for i in range(1,n)])
            s2 = np.asarray([np.sum((data[i:]-np.mean(data[i:]))**2) for i in range(1,n)])
            R  = s0-s1-s2
            try: 
                G  = np.max(R)
            except ValueError:  #raised if `R` is empty.
                return -1
            taustar = int(np.where(R==G)[0][0]) + 1
            sd1 = np.std(data[0:taustar-1])
            sd2 = np.std(data[taustar-1:])
            #use pooled standard deviation
            var = ( taustar*sd1**2 + (n-taustar)*sd2**2 ) / n
            result = self.test_decision(2*G,var*lmbd,data,taustar)
        elif self.type=="normal-var":
            std0 = np.std(data)
            std1 = np.asarray([np.std(data[0:i]) for i in range(1,n)],dtype=float) + eps
            std2 = np.asarray([np.std(data[i:]) for i in range(1,n)],dtype=float) + eps
            R = n*np.log(std0) - tau*np.log(std1) - (n-tau)*np.log(std2)
            G  = np.max(R)
            taustar = int(np.where(R==G)[0]) + 1
            result = self.test_decision(2*G,lmbd,data,taustar)
        self.score = R
        return result

    def test_decision(self,teststat,criterion,data,tau):
        # print("---------------------")
        # print("2G = %e"%(teststat))
        # print("sigma**2*lambda = %e"%(criterion))
        if teststat > criterion:
            # print("-->H0 rejected")
            # print("Changepoint detected at position: %d"%tau)
            # m1 = np.mean(data[0:tau])
            # std1 = np.std(data[0:tau])
            # m2 = np.mean(data[tau:])
            # std2 = np.std(data[tau:])
            # if "mean" in self.type:
            #     print("m1 = %f"%m1)
            #     print("m2 = %f"%m2)
            # else:
            #     print("std1 = %f"%std1)
            #     print("std2 = %f"%std2)
            return tau
            # self.plot_data(type="cpt",p=[tau,m1,m2])
        else:
            return -1
        #     print("-->H0 not rejected")
        # print("---------------------")

if __name__ == "__main__":
    print(cpt(np.ones((60,)), 'normal-mean').find_changepoint())
    