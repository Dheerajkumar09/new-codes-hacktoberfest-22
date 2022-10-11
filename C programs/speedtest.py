import speedtest

s = speedtest.Speedtest()

bytes_num= 1000000

dws = round(s.download()/bytes_num, 2)

ups = round(s.upload()/bytes_num, 2)

print(f'My download speed is: {dws} Mbps')
print(f'My upload speed is: {ups} Mbps')