import requests, urllib
from bs4 import BeautifulSoup
import json
import pandas as pd
import time
import datetime
from pandas.plotting import  table
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']#显示中文字体
import warnings
warnings.filterwarnings('ignore')

# 添加所有需统计打卡的同学leetcode的id(在leetcode主页网址中)
# 例如：https://leetcode.cn/u/xiaoffy/ 的id名称是xiaoffy
# 将收集到的id添加到username数组中
#username=['xiaoffy','teavamc','leetcode-wei','deathymz','juruoer','diamonds-e','night_lun']
#构建一个字典，表示昵称与username的对应关系
username={"xiaoffy":'VIP','teavamc':'A','leetcode-wei':'B','deathymz':'C','juruoer':'D','diamonds-e':'E','night_lun':'F'}
# name用来收集打卡人的id与通过题目数
name=dict()
today=datetime.date.today()
x=[]
#打卡时间段当日00：00到23：59
start_time = int(time.mktime(datetime.date.today().timetuple()))
end_time = start_time+86399
def open_url(url):
    head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/5'
                          '37.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    req = urllib.request.Request(url, headers=head)
    response = urllib.request.urlopen(req)

    html = response.read()
    html_str = html.decode('utf-8')
    t = json.loads(html_str)
    for item in t['data']['recentSubmissions']:
        # 统计的条件是位于当日时间段且通过的题目数，状态码A_10
        if end_time >= item['submitTime'] >= start_time and item['status'] == 'A_10':
            x.append(item['question']['questionFrontendId'])
    name[username[user]] = len(set(x))
    return name
y=[]
for user in username:
    url = "https://leetcode-cn.com/graphql?oprationName=recentSubmissions&variables={%22userSlug%22:%22" + user + "%22}&query=query%20recentSubmissions($userSlug:%20String!){recentSubmissions(userSlug:%20$userSlug){status%20lang%20question{questionFrontendId%20title%20translatedTitle%20titleSlug%20__typename}submitTime%20__typename}}"
    y.append(open_url(url))
df = pd.DataFrame.from_dict(y[0], orient='index',columns=['今日题数'])
df = df.reset_index().rename(columns = {'index':'id'})
df=df.sort_values(by='今日题数',ascending=False)
df.reset_index(drop=True, inplace=True)
df.index=df.index+1
#df.to_csv("{}打卡数据.csv".format(datetime.date.today()),index=False)

# 输出结果转图片
fig = plt.figure(figsize=(3, 4), dpi=1400)
ax = fig.add_subplot(111, frame_on=False)
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)
table(ax, df, loc='center')  # 将df换成需要保存的dataframe即可
#plt.savefig('表格.jpg')
print(df)