### Final project - Analysis of Body Performance Data

Content:
* data shape : (13393, 12)

* age : 20 ~64
* gender : F,M
* height_cm : (If you want to convert to feet, divide by 30.48)
* weight_kg
* body fat_%
* diastolic : diastolic blood pressure (min)
* systolic : systolic blood pressure (min)
* gripForce
* sit and bend forward_cm
* sit-ups counts
* broad jump_cm
* class : A,B,C,D ( A: best) / stratified
* 
Source
link (Korea Sports Promotion Foundation)
Some post-processing and filtering has done from the raw data.

* Saving the selected data set to the SQLite database 
(including "data cleaning"),
* preliminary / exploratory analysis (indicators of position, 
dispersion, including diagrams, e.g. point, histograms),
* development of a simple statistical model 
(including: execution of several selected statistical tests, 
analysis of the dependence of variables, 
verification of selections

Python libraries used: Pandas, Scipy, Seaborn, Matplotlib