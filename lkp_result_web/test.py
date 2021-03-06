#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'jennyzhang'
import os
import json
import sys
#reload(sys)
#sys.setdefaultencoding('utf8')
def getDir(path):

    detail={}

    tags=[]
    dir_list=[]
    tags_format=[]

    file_name_list=[]
    for parent,dirnames,filenames in os.walk(path):
        for dirname in dirnames:
            if dirname not in tags:
                tags.append(dirname)

        for filename in filenames:
            shortname=filename

            if filename not in tags:

                tags.append(shortname)
                detail[shortname]=[]
                temp={}
                temp["path"]=os.path.join(parent,filename)[20:]
                temp["tags"]=temp["path"].split('/')[1:]
                detail[shortname].append(temp)
            else:
                temp={}
                temp["path"]=os.path.join(parent,filename)[20:]
                temp["tags"]=temp["path"].split('/')[1:]
                detail[shortname].append(temp)


    temp=[]
    for tag in tags:
        if((tag != 'var') and (tag != 'www') and (tag != 'html') and (tag != 'result')):
            temp.append(tag)

          
    temp.sort()
    temp.reverse()
    
    return {"init_tags":temp,"detail":detail}

if __name__ == '__main__':
    path=r"/var/www/html/result"
    json_data=getDir(path)
    print json.dumps(json_data,ensure_ascii=False).decode('gbk')

#    #为搜索准备
#    data_format=[]
#    for tag in json_data['init_tags']:
#        tmp={}
#        tmp["value"]=tag
#        tmp["text"]=tag
#        data_format.append(tmp)
#    print str(data_format).decode('gbk')
