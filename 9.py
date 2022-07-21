#Write a python program to implement python string functions
str0="this is my project"
print("capitalize function returns: ",str0.capitalize())
print("find function:",str0.find("my",1,12))

str1="abc123"
print("isalnum function:",str1.isalnum())
print("isalpha function:",str1.isalpha())
print("isdigit function:",str1.isdigit())
print("isspace function:",str1.isspace())
print("islower function:",str1.islower())
print("isupper function:",str1.isupper())
print("lower function:",str1.lower())
print("upper function:",str1.upper())
print("lower function:",str1.title())

str2="This Is my Third string"
print("swapcase function:",str2.swapcase())
print("partition function:",str2.partition('$'))

str3="abcdefgh"
print("lstrip function:",str3.lstrip('bad'))
print("rstrip function:",str3.rstrip('fgh'))

str4="Capital of {} is {}."
print("format function:",str4.format("India","Delhi"))

str5="Kolkata is the capital of India."
print("replace function: ",str5.replace("Kolkata","Delhi"))

str6="join function of python."
print("join function: ","#".join(str6))

str7="This is 9th program \nThis is a new line."
print("splitlines function: ",str7.splitlines())

str8="is_identifier"
print("isidentifier function: ",str8.isidentifier())

str9="CaSEFold FuncTioN Is SIMIlar TO LoweR FuNcTiOn."
print("casefold function: ",str9.casefold())

str10="This line is for partition function."
print("Partition function: ",str10.partition("partition"))









