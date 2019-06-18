#python rogram to illustrating:-------
#**kargs for variablenumber of keyword arguments
def ved2(arg1, **kargs):
   print("first argument",arg1)
   for key , value in kargs.items():
       print("  %s == %s" %(key, value))

#driver code
ved2('hi',first_name='vedant',second_name='bhatt',nick_name='theseus')
