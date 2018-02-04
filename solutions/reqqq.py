import requests

url='https://stepic.org/media/attachments/course67/3.6.3/699991.txt'
st=requests.get(url)
print(st.text[0])
while 'We'!=st.text[0]+st.text[1]:
    url='https://stepic.org/media/attachments/course67/3.6.3/'+st.text.strip()
    st=requests.get(url)
    print(st.text)
print(st.text)

f=open('output.txt','w')
f.write(st.text)
f.close()