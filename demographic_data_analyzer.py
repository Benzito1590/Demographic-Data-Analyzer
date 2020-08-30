#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#########################################
# Created by: Joao Pedro Peters Barbosa #
#                                       #
# github: https://github.com/Jppbrbs    #
# email: jpptrs@gmail.com               #
#                                       #
# Date: Jul/2020                        #
#########################################


"""
freeCodeCamp Project2 - Data Analysis with Python Course
"""



import pandas as pd
import sys


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult_data.csv')
    df.info()

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()
    # print(race_count)

    # What is the average age of men?
    average_age_men = round(df.loc[df['sex'] == 'Male', 'age'].mean(), 1)
    # print(average_age_men)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round(
        (df.loc[df['education'] == 'Bachelors'].shape[0] / df.shape[0]) * 100,
        1)
    # print(percentage_bachelors)

    # What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
    higher_education_rich = round(
        (df.loc[(
            (df['education'] == 'Bachelors') | (df['education'] == 'Masters') |
            (df['education'] == 'Doctorate')) &
                (df['salary'] == '>50K')].shape[0] * 100) /
        df.loc[(df['education'] == 'Bachelors') |
               (df['education'] == 'Masters') |
               (df['education'] == 'Doctorate')].shape[0], 1)
    # print(higher_education_rich)

    # What percentage of people without advanced education make more than 50K?
    lower_education_rich = round((df.loc[
        ((df['education'] != 'Bachelors') & (df['education'] != 'Masters') &
         (df['education'] != 'Doctorate')) &
        (df['salary'] == '>50K')].shape[0] * 100) / df.loc[
            (df['education'] != 'Bachelors') & (df['education'] != 'Masters') &
            (df['education'] != 'Doctorate')].shape[0], 1)
    # print(lower_education_rich)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()
    # print(min_work_hours)

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    rich_percentage = round(
        (df.loc[(df['hours-per-week'] == min_work_hours) &
                (df['salary'] == '>50K')].shape[0] /
         df.loc[df['hours-per-week'] == min_work_hours].shape[0]) * 100)
    # print(rich_percentage)

    # What country has the highest percentage of people that earn >50K?
    highest_earning_country = round(
        (df.loc[df['salary'] == '>50K', 'native-country'].value_counts() /
         df['native-country'].value_counts()) * 100, 1).idxmax()
    # print(highest_earning_country)

    highest_earning_country_percentage = round(
        (df.loc[df['salary'] == '>50K', 'native-country'].value_counts() /
         df['native-country'].value_counts()) * 100, 1).max()
    # print(highest_earning_country_percentage)

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df.loc[(df['native-country'] == 'India') & (
        df['salary'] == '>50K'), 'occupation'].value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE
    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(
            f"Percentage with higher education that earn >50K: {higher_education_rich}%"
        )
        print(
            f"Percentage without higher education that earn >50K: {lower_education_rich}%"
        )
        print(f"Min work time: {min_work_hours} hours/week")
        print(
            f"Percentage of rich among those who work fewest hours: {rich_percentage}%"
        )
        print("Country with highest percentage of rich:",
              highest_earning_country)
        print(
            f"Highest percentage of rich people in country: {highest_earning_country_percentage}%"
        )
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
