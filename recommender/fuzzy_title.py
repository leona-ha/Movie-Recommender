""" Use fuzzy matching (= the process of finding similar results from search queries)
to insert title"""

from fuzzywuzzy import fuzz, process

Str1 = "Titanic"
Str2 = "Titus Andronicus"


#direct string comparison
ratio = fuzz.ratio(Str1.lower(),Str2.lower()) #basic character for character comparison
partial_ratio = fuzz.partial_ratio(Str1.lower(),Str2.lower()) #compares sub-sections of text for matches
token_set_ratio = fuzz.token_set_ratio(Str1,Str2) # allows for different word order as well as partial matching

#best of  the rest comparison
str2Match = "apple "
strOptions = ["Apple Inc.","apple park","apple incorporated","iphone"]

Ratios = process.extract(str2Match,strOptions)
highest = process.extractOne(str2Match,strOptions)
