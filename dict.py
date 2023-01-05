data={1:"Navin"
,2:"Kieran",4:"Hersch"}
print(data)
data[4]
print(data[4])
print(data.get(1))
keys=["Navin","kieran","hersch"]
values=["Python","java","C#"]
data = dict(zip(keys,values))
print(data)
data["Monika"]="C#"
print(data)
del data["hersch"]
print(data)
prog = {"JS":"Atom","CS":"VS","Python":["Pycharm","Sublime"],"Java":{"JSE":"Netbeans","JEE":"Eclipse"}}