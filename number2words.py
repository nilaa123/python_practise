dict={"0":"zero","1":"one","2":"two","3":"three","4":"four","5":"five","6":"six","7":"seven","8":"eight","9":"nine"}
Phone=input("Phone:")
output=""
for num in Phone:
    output+=(dict[num])+" "   #output+=dict.get(num)              To avoid error if missing key
print(output)