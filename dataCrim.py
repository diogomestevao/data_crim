import os
import shutil
import concurrent.futures
import requests
from string import Template
import time
import xml.etree.ElementTree as ET
import requests 
from xml.etree import ElementTree
import csv
from datetime import datetime
import pandas as pd
from glob import glob
# np é uma convenção para o numpy, convenção é um acordo 
# estabelecido com o intuito de padronizar e facilitar o entendimento.
import numpy as np  

#http://www.ssp.sp.gov.br/transparenciassp/Consulta.aspx

path_input_file='C:\\Diogo\Devs\\Python\\roubosPy\\in\\'

#Obtem arquivos para serem processados
def checkFilesInputExist(filePath):
    arquivos = glob(filePath + '*.csv')
    #for arq in arquivos:
    #  print(arq)
    return arquivos

def reader_file(file):
    df = pd.read_csv(file,sep=';',delimiter=';', header="infer", encoding='ISO-8859-1')
    #print( df.head() )
    #print( df.describe(include="all") )
    #print( df.info() )

    df.replace("?", np.nan, inplace = True)

    missing_data = df.isnull()
    print(missing_data.head(5))

    for column in missing_data.columns.values.tolist():
        print(column)
        print (missing_data[column].value_counts())
        print("")   




    t=df['MARCA_CELULAR'].value_counts()
    print("total " + str(t))


    X = df["MARCA_CELULAR"] 

    moda = X.mode() 
    print("Moda ", moda[0])


    for index, row in df.iterrows():
        #print(index)
        dataocorrencia=row["DATAOCORRENCIA"]
        print("DATAOCORRENCIA: " + dataocorrencia)

def main():

    filesList = []
    filesList = checkFilesInputExist(path_input_file)
    #print( str(len(filesList)) + ' files to process in: ' + path_input_file)
    if len(filesList) > 0 :
      for file in filesList:
        #print('File in process: ' + file)
        fullNameFile= os.path.basename(file)
        nameFile=os.path.splitext(fullNameFile)[0]
        #print('File:' + nameFile)
        reader_file(file)
    else:
      print('No files to process')
if __name__ == "__main__":
    main()
