a = {"UPI855002":"shivam", "UPI855001":"rahul"}
print(a)
a["UPI855010"] = a["UPI855002"]
del a["UPI855002"]
print(a)