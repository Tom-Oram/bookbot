my_dict = {"a": 2, "b": 5}


#for k, v in my_dict.items():
#    print("k =", k, "v =", v)

pairs = [{"char": k, "num": v} for k, v in my_dict.items()]
print(pairs)