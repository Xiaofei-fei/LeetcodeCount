# leetcode刷题统计

## 主要功能

- 通过统计个人leetcode主页信息，对每天刷题数进行爬取统计
- 统计时间：当时00:00-23:59
- 基本输出：昵称+当日通过题数

## 使用方法

- 统计leetcode用户名及个人昵称，打开leetcode个人主页，网址一般为

```html
https://leetcode.cn/u/username/ 的用户名称是username
```

- 将username与个人昵称存入一个hashmap，进行映射
- 通过爬虫程序爬取当日刷题的题号，是否通过以及是否提交等相关信息
- 统计刷题数目
- 输出当日的图片记录

## 未来期待

- 基于此进行其他有意思想法的实现，比如周赛上分，高频题目抓取等
- 自动化爬取，结果通过微信api自动群发等
- 程序优化，提升运行速度





