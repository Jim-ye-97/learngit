from urllib.robotparser import RobotFileParser

rp=RobotFileParser()
rp.set_url('https://www.jianshu.com/robots.txt')
rp.read()
print(rp.can_fetch('*','https://www.jianshu.com/p/b67554025d7d'))
print(rp.can_fetch('*','https://www.jianshu.com/search?q=python&page=l&ty e=collections'))
print(rp.can_fetch('*','https://www.jianshu.com/'))


