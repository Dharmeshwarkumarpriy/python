try:
    print("try block")
except:
    print("except block")
else:
    print("else block")
finally:
    print("finally block")

# we not write multiple else bock for a try block.
# 2 we not write multiple finally block for a try block.
# 3. we not write multiple except block for a try block.
# 4. use structure (1) try block try--except--else--finally, (2) try--except--finally, (3) try--finally