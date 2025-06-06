def divide(x,y):
    try:
        result=x/y
    except ZeroDivisionError:
        print("por favor, nao utilize zeros!")
    except:
        print("\033[91m algodeu errado...")
    else:
        print(f"seu resultado é: {result}")
    finally:
        print("\033[92m vamos de novo?")
divide(13,0)
divide(13,2)
divide(13,"a")



