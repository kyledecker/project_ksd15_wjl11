# BME590 Final Project: Automated Cervical Cancer Diagnosis

## SUMMARY
This package is used to classify cervical cancer automatically using features extracted from POCkeT Colposcope images. The classification relies on a SVM model that is trained on a representative sample of dysplasia and healthy images.

## MODULES
* *main.py* - wrapper script used to either train and evaluate the SVM model or classify an unkown image 
* OTHER FILES HERE

## UNIT TESTING
Unit testing of core functions can performed by running *py.test* from the base directory

## RUN CODE
The automated cervical cancer diagnosis script can be run from the base directory using the following command:
```
python main.py
```

**Be sure to set inputs for the image file you would like to classify, if you would like to perform training, the model filename, etc.** 
For help and description of input arguments:
```
python main.py --help
```