#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt 
from numpy import *
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


train_df = pd.read_csv("Training.csv")
test_df = pd.read_csv("Testing.csv")


# In[3]:


train_df.shape , test_df.shape


# In[4]:


df1= train_df.sample(frac=1 , random_state = 0)


# In[5]:


len(df1["prognosis"].unique())


# In[6]:


disease_dict = { #dictionary for diseases
       'AIDS': 0,
       'Jaundice' : 1,
       'Paralysis (brain hemorrhage)' : 2,
       'Hepatitis D' : 3,
       'Urinary tract infection' : 4,
       'Hypertension ' : 5,
       'Hepatitis B' : 6,
       'hepatitis A': 7,
       'Dimorphic hemmorhoids(piles)' : 8,
       'Common Cold' : 9,
       'Impetigo' : 10,
       'Peptic ulcer diseae' : 11,
       'Gastroenteritis': 12,
       'Psoriasis' : 13,
       'Fungal infection' : 14,
       'Hyperthyroidism' : 15,
       'Heart attack' : 16,
       'Chronic cholestasis' : 17,
       'Bronchial Asthma' : 18,
       'GERD' : 19,
       'Allergy' : 20,
       'Pneumonia': 21,
       'Acne': 22,
       'Arthritis': 23,
       'Chicken pox': 24,
       'Alcoholic hepatitis' : 25,
       'Hypothyroidism' : 26,
       'Diabetes ': 27,
       'Varicose veins': 28,
       '(vertigo) Paroymsal  Positional Vertigo' : 29,
       'Drug Reaction': 30,
       'Malaria': 31,
       'Hepatitis E': 32,
       'Migraine': 33,
       'Osteoarthristis': 34,
       'Hypoglycemia': 35,
       'Tuberculosis': 36,
       'Typhoid': 37,
       'Hepatitis C' : 38,
       'Dengue': 39,
       'Cervical spondylosis': 40
}

symptoms_dict={'abdominal_pain': 39,
 'abnormal_menstruation': 101,
 'acidity': 8,
 'acute_liver_failure': 44,
 'altered_sensorium': 98,
 'anxiety': 16,
 'back_pain': 37,
 'belly_pain': 100,
 'blackheads': 123,
 'bladder_discomfort': 89,
 'blister': 129,
 'blood_in_sputum': 118,
 'bloody_stool': 61,
 'blurred_and_distorted_vision': 49,
 'breathlessness': 27,
 'brittle_nails': 72,
 'bruising': 66,
 'burning_micturition': 12,
 'chest_pain': 56,
 'chills': 5,
 'cold_hands_and_feets': 17,
 'coma': 113,
 'congestion': 55,
 'constipation': 38,
 'continuous_feel_of_urine': 91,
 'continuous_sneezing': 3,
 'cough': 24,
 'cramps': 65,
 'dark_urine': 33,
 'dehydration': 29,
 'depression': 95,
 'diarrhoea': 40,
 'dischromic _patches': 102,
 'distention_of_abdomen': 115,
 'dizziness': 64,
 'drying_and_tingling_lips': 76,
 'enlarged_thyroid': 71,
 'excessive_hunger': 74,
 'extra_marital_contacts': 75,
 'family_history': 106,
 'fast_heart_rate': 58,
 'fatigue': 14,
 'fluid_overload': 45,
 'fluid_overload.1': 117,
 'foul_smell_of urine': 90,
 'headache': 31,
 'high_fever': 25,
 'hip_joint_pain': 79,
 'history_of_alcohol_consumption': 116,
 'increased_appetite': 104,
 'indigestion': 30,
 'inflammatory_nails': 128,
 'internal_itching': 93,
 'irregular_sugar_level': 23,
 'irritability': 96,
 'irritation_in_anus': 62,
 'itching': 0,
 'joint_pain': 6,
 'knee_pain': 78,
 'lack_of_concentration': 109,
 'lethargy': 21,
 'loss_of_appetite': 35,
 'loss_of_balance': 85,
 'loss_of_smell': 88,
 'malaise': 48,
 'mild_fever': 41,
 'mood_swings': 18,
 'movement_stiffness': 83,
 'mucoid_sputum': 107,
 'muscle_pain': 97,
 'muscle_wasting': 10,
 'muscle_weakness': 80,
 'nausea': 34,
 'neck_pain': 63,
 'nodal_skin_eruptions': 2,
 'obesity': 67,
 'pain_behind_the_eyes': 36,
 'pain_during_bowel_movements': 59,
 'pain_in_anal_region': 60,
 'painful_walking': 121,
 'palpitations': 120,
 'passage_of_gases': 92,
 'patches_in_throat': 22,
 'phlegm': 50,
 'polyuria': 105,
 'prominent_veins_on_calf': 119,
 'puffy_face_and_eyes': 70,
 'pus_filled_pimples': 122,
 'receiving_blood_transfusion': 111,
 'receiving_unsterile_injections': 112,
 'red_sore_around_nose': 130,
 'red_spots_over_body': 99,
 'redness_of_eyes': 52,
 'restlessness': 20,
 'runny_nose': 54,
 'rusty_sputum': 108,
 'scurring': 124,
 'shivering': 4,
 'silver_like_dusting': 126,
 'sinus_pressure': 53,
 'skin_peeling': 125,
 'skin_rash': 1,
 'slurred_speech': 77,
 'small_dents_in_nails': 127,
 'spinning_movements': 84,
 'spotting_ urination': 13,
 'stiff_neck': 81,
 'stomach_bleeding': 114,
 'stomach_pain': 7,
 'sunken_eyes': 26,
 'sweating': 28,
 'swelled_lymph_nodes': 47,
 'swelling_joints': 82,
 'swelling_of_stomach': 46,
 'swollen_blood_vessels': 69,
 'swollen_extremeties': 73,
 'swollen_legs': 68,
 'throat_irritation': 51,
 'toxic_look_(typhos)': 94,
 'ulcers_on_tongue': 9,
 'unsteadiness': 86,
 'visual_disturbances': 110,
 'vomiting': 11,
 'watering_from_eyes': 103,
 'weakness_in_limbs': 57,
 'weakness_of_one_body_side': 87,
 'weight_gain': 15,
 'weight_loss': 19,
 'yellow_crust_ooze': 131,
 'yellow_urine': 42,
 'yellowing_of_eyes': 43,
 'yellowish_skin': 32}  #dictionary for symptoms

disease = list(disease_dict.keys())
index = list(disease_dict.values())


# In[7]:


df1["prognosis_class"] = train_df["prognosis"].map(disease_dict)


# In[8]:


X = df1.drop(["prognosis" , "prognosis_class"] , axis = 1)
y = array(df1.prognosis_class)

X.shape , y.shape


# In[9]:


from sklearn.model_selection import train_test_split
x_train , x_test , y_train , y_test = train_test_split(X , y , test_size = 0.2 , shuffle = True , random_state = 0)


# In[10]:


from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators = 100)
model.fit(x_train , y_train)
model.score (x_test , y_test)  #using Random Forest Classifier ML model to predict


# In[41]:


#def predict_disease(x):
  #  z = zeros((1,132))
   # for i in  x:
      #  t = 0
        #for j in x_train.columns : 
          #  if i == j: 
           #     z[0][t] = 1 
           # else : 
             #   pass 
          #  t = t + 1
   # return model.predict(x)


# In[12]:


import pickle 
with open("symptom_to_disease_model" , "wb") as f: 
    pickle.dump(model,f)


# In[13]:


import json
columns = {
    "data_columns" : [col for col in X.columns]
}

with open("columns.json","w") as f :
    f.write(json.dumps(columns))


# In[ ]:
input_vector = zeros(len(symptoms_dict))
input_vector[[symptoms_dict['itching'], symptoms_dict['skin_rash']]] = 1  #giving sample symptoms to the model to predict a disease
#rf_clf.predict_proba([input_vector])
ans=model.predict([input_vector])   #predicting disease finally
for key,value in disease_dict.items():
    if value==int(ans[0]):            #extracting disease from dictionary
        print(key)
    else:
        continue

