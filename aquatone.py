file = input("域名：")
with open('./aquatone/%s/hosts.txt' % file) as f:
    while True:
        line =f.readline().strip().split(',')[0]
        if not line:
            break
        with open('%s.txt' % file,"a+") as k:
            k.write(line + "\n")