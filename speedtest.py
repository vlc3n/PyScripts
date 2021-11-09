import speedtest
st = speedtest.Speedtest()
print('Hello! This is a Simple Speedtest Programmed in Python! Please write "start" to begin the Test')
inp = input()
if inp == "start":
    servernames = []
    st.get_servers(servernames)
    print(st.download(), "b/s") 
    print(st.upload(), "b/s") 
    print(st.results.ping, "b/s") 
else:
    print(f'You need to write "start" and not {inp}')