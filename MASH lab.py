# -*- coding: utf-8 -*-

"""
By Jordane Thomas, Goldman Sach 2016 ASC Cohort
7/15/2016
M.A.S.H. lab
"""

from random import *

wife = ["A Girl Who Codes","I really don't know Im just a game",
        "Basic Algorithms such as my self can't be trusted to predict the furture", 
        "I'm not Mathed up enought actually predict the future", 
        "If want to know who your wife will be go out there and meet women"
        ]

career = ["The world is your's, do what you want","do what you want",
          "You know better than me","you need to find out yourself",
          "don't depend me for your financial freedom"
         ]

housing = ["Mansion-I'm only saying this I don't mean it",
           "Apartment-I'm only saying this I don't mean it",
           "Shack-I mean this one ;)",
           "House-I'm only saying this I don't mean it"
           ]
           
print("Hello, this is a  game called M.A.S.H..\n",
      ",It's supposted to predict events in your life,\n",
      "but the truth is that it cann't. Though this one can\n",
      "because it has the magical power of truth, and realistic thinking."
      )
      
print("\nTell me what your name is.")
name = raw_input()

print("\nTell who your you want your wife to be.")
spouse = raw_input()
spouse = wife[randint(0,len(wife)-1)]

print("\nTell me what career you want.")
job = raw_input()
job = career[randint(0,len(job)-1)]

print("\nTell me where you want live.")
home = raw_input()
home = housing[randint(0,len(housing)-1)]

print("\nI have looked in the to the future and can tell you with accuray",
      "\nYour wife is: ",spouse,
      "\nYour job is: ",job,
      "\nYour home is: ",home)
