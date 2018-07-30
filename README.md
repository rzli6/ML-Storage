# ML-Storage

This is the summer research I did in my senior year's the summer holiday. I rebuilt three paper's algorithms, which aim at improving accuracy of disk failure prediction. The three papers are: 
1. Prediction Disk Replacement towards Reliable Data Centers (ADF)
2. Improving Storage System Reliability with Proactive Error Prediction (ATC17)
3. Improving Service Availability of Cloud Systems by Prediction Disk Error (ATC18)

## Prerequisites & Installing

### Machine Learning Packages

In this project, we mainly built several machine learning models for disk prediction. Thus, in order to run the scritps in the repository, you have to install **python** on your computer with following python packages:
  1. pandas
  
    CSV file pre-processing
    
  2. numpy
  
    CSV file pre-processing
    
  3. sklearn
  
    Machine learning models
    
  4. matplotlib
  
    Machine presenting & data diagram constructing 
    
*Anaconda is recommended for handling python packages* 

### Dataset

The datasets are different in the three papers. However, only Backblaze dataset is used when algorithms are rebuilt in the project. You can get a copy of dataset according to the following link:

https://www.backblaze.com/b2/hard-drive-test-data.html

## Documents Description

### data

This folder contains all the Backblaze data pre-downloaded from the website. It is empty because data is too large and meaningless to be included here. **Nevertheless, before running any python scripts, please make sure all data has been downloaded from Backblaze Hard Drive website and put in the proper places in this folder.**

  1. atc18
    
    Containing the data of 2017 fouth quarter (from 2017-10-01 to 2017-12-31) 
    
  2. data-2014 
    
    Containing data of 2014
  
  3. data-2015 
    
    Containing data of 2015
  
  4. data-2016 
    
    Containing data of 2016
  
  2. data-2017 
    
    Containing data of 2017
  
  2. data-2018 
    
    Containing data of 2018
   

### ADF/

  1. SgtA.ipynb

    This file contains the main implementation of ADF's paper. It should be run in "jupyter notebook" environment. 

  2. find_cpt.ipynb
    
    This file is an API used in the main file SgtA.ipynb. It takes reference of the link below:
    
    https://medium.com/bigdatarepublic/contextual-changepoint-detection-with-python-and-r-using-rpy2-fa7d86259ba9
    
  3. preprocess/
  
    This folder contains the pre-processed data. It exists because data pre-processing usually requires a huge amount of time compared with the time used to do training.

### ATC17/
   1. SgtA.ipynb

    This file contains the main implementation of ADF's paper. It should be run in "jupyter notebook" environment. 

  2. For Report.ipynb
    
    This file gives out the images and data used to build a report. You can verify my result here. Make sure this file runs only after running the SgtA.ipynb
    
  3. preprocess/
  
    This folder contains the pre-processed data. It exists because data pre-processing usually requires a huge amount of time compared with the time used to do training.

### ATC18/
  1. SgtA.ipynb

    This file contains the main implementation of ADF's paper. It should be run in "jupyter notebook" environment. 

  2. preprocess/
  
    This folder contains the pre-processed data. It exists because data pre-processing usually requires a huge amount of time compared with the time used to do training.

## Paper/

This folder contains the three paper I rebuilt in PDF format.

## Report/

This folder contains the weekly reports in PDF format for convenient to be shown on github.

## Acknowledgments

* Find CPT

  https://medium.com/bigdatarepublic/contextual-changepoint-detection-with-python-and-r-using-rpy2-fa7d86259ba9

* Thanks for the help of my instructive Professor Patrick P. C. Lee and his PhD student Shujie Han.
