# student number:

# IMPLEMENT YOUR FUNCTION HERE
import random
import cmath

converter_types = ['int', 'float', 'bool', 'string', 'complex']
def random_converter(x):
    input_type = type(x)
    val = random.randint(0,4)
    ctype = converter_types[val]
    print(" x = {}, type(x)= {}, convert_type = {} ".format(x, type(x), ctype), end="")
    if ctype == 'int':
        # string
        if input_type == type('1'):
            if x.isdigit():
                return int(x)
            else:
                return None
        # float
        elif input_type == type(2.5):
            return int(x)
        # interger
        elif input_type == type(2):
            return x
        # bool
        elif input_type == type(True):
            if x == True:
                return 1
            elif x == False:
                return 0
            else :
                return None
        # complex
        elif input_type == type(complex(3,4)):
            return None
            # if x.imag == 0:
            #     return int(x.real)
            # else:
            #     return None

        
    elif ctype == 'float':
        # string
        if input_type == type('1'):
            if x.replace('.','',1).isdigit():
                return float(x)
            else:
                return None
        # float
        elif input_type == type(2.5):
            return x 
        # integer
        elif input_type == type(2):
            return float(x)
        # bool
        elif input_type == type(True):
            if x == True:
                return 1.0
            elif x == False:
                return 0.0
            else :
                return None
        # complex
        elif input_type == type(complex(3,4)):
            return None
            # if x.imag == 0:
            #     return float(x.real)
            # else:
            #     return None

    elif ctype == 'bool':
        # string
        if input_type == type('1'):
            if x.lower() == 'true' or x == '1': return True
            elif x.lower() == 'false' or x == '0': return False
            else: return None
        # float
        elif input_type == type(2.5):
            if x == float(1): return True
            elif x == float(0): return False
            else: return None
        # integer
        elif input_type == type(2):
            if x == 1: return True
            elif x == 0: return False
            else: return None
        # bool
        elif input_type == type(True):
            return x
        # complex
        elif input_type == type(complex(3,4)):
            return None
            # if x.imag == 0 and x.real == 1:
            #     return True
            # elif x.imag == 0 and x.real == 0:
            #     return False
            # else:
            #     return None

    elif ctype == 'string':
        # string
        if input_type == type('1'):
            return x
        # float
        elif input_type == type(2.5):
            return str(x)
        # integer
        elif input_type == type(2):
            return str(x)
        # bool
        elif input_type == type(True):
            return str(x)
        # complex
        elif input_type == type(complex(3,4)):
            return str(x)

    elif ctype == 'complex':
        # string
        if input_type == type('1'):
            temp =  x.replace(" ", "").replace("+", "").replace("j","")
            if temp.replace('.','',1).isdigit():
                val = complex(x.replace(" ", "").replace("+", "+"))
                return val
            else:
                return None
        # float
        elif input_type == type(2.5):
            return complex(x, 0)
        # integer
        elif input_type == type(2):
            return complex(x, 0)
        # bool
        elif input_type == type(True):
            return complex(x, 0)
        # complex
        elif input_type == type(complex(3,4)):
            return x

if __name__ == "__main__":

    x = [4, 1 ,0 , 4.4, 4.54, "strval", "45", "34jal", "34.45", "34.45.56", "4+4j", "True", "False", True, False, complex(3.4, 0) , complex(3.4, 4)]
    for value in x:
        val = random_converter(value)
        print(", value = {}, type(value)= {}".format(val, type(val)))