# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 14:30:38 2022

@author: yonau
"""
import json
import sqlite3
import time 

# conn = sqlite3.connect('covid.db')
# print ("Base de données ouverte avec succès")

# conn.execute('CREATE TABLE covid (code_iso, continent,location,last_updated_date,total_cases,new_cases,new_cases_smoothed,total_deaths,new_deaths,new_deaths_smoothed,total_cases_per_million,new_cases_per_million,new_cases_smoothed_per_million,total_deaths_per_million,new_deaths_per_million,new_deaths_smoothed_per_million,reproduction_rate,icu_patients,icu_patients_per_million,hosp_patients,hosp_patients_per_million,weekly_icu_admissions,weekly_icu_admissions_per_million,weekly_hosp_admissions,weekly_hosp_admissions_per_million,new_tests,total_tests,total_tests_per_thousand,new_tests_per_thousand,new_tests_smoothed,new_tests_smoothed_per_thousand,positive_rate,tests_per_case,tests_units,total_vaccinations,people_vaccinated,people_fully_vaccinated,total_boosters,new_vaccinations,new_vaccinations_smoothed,total_vaccinations_per_hundred,people_vaccinated_per_hundred,people_fully_vaccinated_per_hundred,total_boosters_per_hundred,new_vaccinations_smoothed_per_million,stringency_index,population,population_density,median_age,aged_65_older,aged_70_older,gdp_per_capita,extreme_poverty,cardiovasc_death_rate,diabetes_prevalence,female_smokers,male_smokers,handwashing_facilities,hospital_beds_per_thousand,life_expectancy,human_development_index,excess_mortality_cumulative_absolute,excess_mortality_cumulative,excess_mortality,excess_mortality_cumulative_per_million)' )
# print ("Table créée avec succès")
# conn.close ()

f = open('covid.json')
data = json.load(f)


for msg in data: 
    valeur=[]
    #print(msg)
    for col in data[msg]:
        # print(col)
        # print(type(col))
        # print(data[msg][col])
        valeur.append(data[msg][col])
    # print(valeur)
    # print(len(valeur))
    # time.sleep(10)
    with sqlite3.connect("covid.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO covid(code_iso, continent,location,last_updated_date,total_cases,new_cases,new_cases_smoothed,total_deaths,new_deaths,new_deaths_smoothed,total_cases_per_million,new_cases_per_million,new_cases_smoothed_per_million,total_deaths_per_million,new_deaths_per_million,new_deaths_smoothed_per_million,reproduction_rate,icu_patients,icu_patients_per_million,hosp_patients,hosp_patients_per_million,weekly_icu_admissions,weekly_icu_admissions_per_million,weekly_hosp_admissions,weekly_hosp_admissions_per_million,new_tests,total_tests,total_tests_per_thousand,new_tests_per_thousand,new_tests_smoothed,new_tests_smoothed_per_thousand,positive_rate,tests_per_case,tests_units,total_vaccinations,people_vaccinated,people_fully_vaccinated,total_boosters,new_vaccinations,new_vaccinations_smoothed,total_vaccinations_per_hundred,people_vaccinated_per_hundred,people_fully_vaccinated_per_hundred,total_boosters_per_hundred,new_vaccinations_smoothed_per_million,stringency_index,population,population_density,median_age,aged_65_older,aged_70_older,gdp_per_capita,extreme_poverty,cardiovasc_death_rate,diabetes_prevalence,female_smokers,male_smokers,handwashing_facilities,hospital_beds_per_thousand,life_expectancy,human_development_index,excess_mortality_cumulative_absolute,excess_mortality_cumulative,excess_mortality,excess_mortality_cumulative_per_million) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (msg,valeur[0],valeur[1],valeur[2],valeur[3],valeur[4],valeur[5],valeur[6],valeur[7],valeur[8],valeur[9],valeur[10],valeur[11],valeur[12],valeur[13],valeur[14],valeur[15],valeur[16],valeur[17],valeur[18],valeur[19],valeur[20],valeur[21],valeur[22],valeur[23],valeur[24],valeur[25],valeur[26],valeur[27],valeur[28],valeur[29],valeur[30],valeur[31],valeur[32],valeur[33],valeur[34],valeur[35],valeur[36],valeur[37],valeur[38],valeur[39],valeur[40],valeur[41],valeur[42],valeur[43],valeur[44],valeur[45],valeur[46],valeur[47],valeur[48],valeur[49],valeur[50],valeur[51],valeur[52],valeur[53],valeur[54],valeur[55],valeur[56],valeur[57],valeur[58],valeur[59],valeur[60],valeur[61],valeur[62],valeur[63]))

        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    