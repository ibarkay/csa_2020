listy = [
"The Land of CSA",
"CSA HINT: I",
"CSA HINT: o",
"CSA HINT: A",
"CSA HINT: 8",
"CSA HINT: e",
"Level 6",
"CSA HINT: 7",
"Level 8",
"CSA HINT: h",
"CSA HINT: R",
"Level 11",
"CSA HINT: c",
"Level 13",
"CSA HINT: !",
"CSA HINT: L",
"CSA HINT: _",
"",
"Title Page"
]

dicy = {0:1,1:2,2:9,3:3,4:7,5:5,6:16,7:4,8:10,9:2,10:12,11:12,12:2,13:16,14:1,15:14}

for i in dicy:
    print(listy[dicy[i]].replace('CSA HINT: ',''),end='')