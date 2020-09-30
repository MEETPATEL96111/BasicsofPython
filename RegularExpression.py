import  re
phrase="my name is Durgaprasad and my email id durgaprasad8883@gmail.com, jyos emaill id gsjyothirani@gmail.com"
#email Scrapping
pattern=re.compile("[a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+") //change the Regex equation it is best ever equation for email Scrapping
#result=pattern.search(phrase) geeting single email
result=pattern.findall(phrase)
print(result)
