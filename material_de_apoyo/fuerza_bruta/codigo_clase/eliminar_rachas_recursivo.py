def f(palabra: str, n: int, cont_actual: int = 0, i: int = 0, ult_letra: str = "", ns: str = "") -> str:
    if(len(palabra)== i):        
        print(f"letra:{ult_letra} - conteo:{cont_actual}")
        if(cont_actual > n):
            return ns
        else:
            return ns + (ult_letra * cont_actual)
    
    if(palabra[i] != ult_letra):
        if(cont_actual != 0):
            print(f"letra:{ult_letra} - conteo:{cont_actual}")
            if(cont_actual >= n):
                return f(palabra, n, 1, i+1, palabra[i], ns)
            return f(palabra, n, 1, i+1, palabra[i], ns + (ult_letra * cont_actual))
        return f(palabra, n, 1, i+1, palabra[i], ns)
    else:
        return f(palabra, n, cont_actual + 1, i+1, palabra[i], ns)
    
print(f("abcd", 3))