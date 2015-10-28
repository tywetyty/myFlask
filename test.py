#coding=utf-8
import os
basedir = os.path.abspath(os.path.dirname(__file__))
print basedir
print os.environ.get('SECRET_KEY')
chang = ['化五厂HCCP','安邦','化一厂','化三厂','离子膜','热电厂']
for i in chang:
	print i