#!/usr/bin/env python
# -*- coding: utf-8 -*-


# tv names
#tv_names = ['CCTV-1', 'CCTV-10', 'CCTV-11', 'CCTV-12', 'CCTV-13', 'CCTV-14', 'CCTV-15', 'CCTV-2', 'CCTV-3', 'CCTV-4', 'CCTV-5', 'CCTV-6', 'CCTV-7', 'CCTV-8', 'CCTV-9', '\xe4\xb8\x9c\xe5\x8d\x97\xe5\x8d\xab\xe8\xa7\x86', '\xe4\xb8\x9c\xe6\x96\xb9\xe5\x8d\xab\xe8\xa7\x86', '\xe4\xba\x91\xe5\x8d\x97\xe5\x8d\xab\xe8\xa7\x86', '\xe5\x86\x85\xe8\x92\x99\xe5\x8f\xa4\xe5\x8d\xab\xe8\xa7\x86', '\xe5\x8c\x97\xe4\xba\xac\xe5\x8d\xab\xe8\xa7\x86', '\xe5\x90\x89\xe6\x9e\x97\xe5\x8d\xab\xe8\xa7\x86', '\xe5\x9b\x9b\xe5\xb7\x9d\xe5\x8d\xab\xe8\xa7\x86', '\xe5\xa4\xa9\xe6\xb4\xa5\xe5\x8d\xab\xe8\xa7\x86', '\xe5\xae\x81\xe5\xa4\x8f\xe5\x8d\xab\xe8\xa7\x86', '\xe5\xae\x89\xe5\xbe\xbd\xe5\x8d\xab\xe8\xa7\x86', '\xe5\xb1\xb1\xe4\xb8\x9c\xe5\x8d\xab\xe8\xa7\x86', '\xe5\xb1\xb1\xe8\xa5\xbf\xe5\x8d\xab\xe8\xa7\x86', '\xe5\xb9\xbf\xe4\xb8\x9c\xe5\x8d\xab\xe8\xa7\x86', '\xe5\xb9\xbf\xe8\xa5\xbf\xe5\x8d\xab\xe8\xa7\x86', '\xe6\x96\xb0\xe7\x96\x86\xe5\x85\xb5\xe5\x9b\xa2\xe5\x8d\xab\xe8\xa7\x86', '\xe6\x96\xb0\xe7\x96\x86\xe5\x8d\xab\xe8\xa7\x86', '\xe6\x97\x85\xe6\xb8\xb8\xe5\x8d\xab\xe8\xa7\x86', '\xe6\xb1\x9f\xe8\x8b\x8f\xe5\x8d\xab\xe8\xa7\x86', '\xe6\xb1\x9f\xe8\xa5\xbf\xe5\x8d\xab\xe8\xa7\x86', '\xe6\xb2\xb3\xe5\x8c\x97\xe5\x8d\xab\xe8\xa7\x86', '\xe6\xb5\x99\xe6\xb1\x9f\xe5\x8d\xab\xe8\xa7\x86', '\xe6\xb7\xb1\xe5\x9c\xb3\xe5\x8d\xab\xe8\xa7\x86', '\xe6\xb9\x96\xe5\x8c\x97\xe5\x8d\xab\xe8\xa7\x86', '\xe6\xb9\x96\xe5\x8d\x97\xe5\x8d\xab\xe8\xa7\x86', '\xe7\x94\x98\xe8\x82\x83\xe5\x8d\xab\xe8\xa7\x86', '\xe8\xa5\xbf\xe8\x97\x8f\xe5\x8d\xab\xe8\xa7\x86', '\xe8\xb4\xb5\xe5\xb7\x9e\xe5\x8d\xab\xe8\xa7\x86', '\xe8\xbe\xbd\xe5\xae\x81\xe5\x8d\xab\xe8\xa7\x86', '\xe9\x87\x8d\xe5\xba\x86\xe5\x8d\xab\xe8\xa7\x86', '\xe9\x87\x91\xe9\xb9\xb0\xe5\x8d\xa1\xe9\x80\x9a', '\xe9\x99\x95\xe8\xa5\xbf\xe5\x8d\xab\xe8\xa7\x86', '\xe9\x9d\x92\xe6\xb5\xb7\xe5\x8d\xab\xe8\xa7\x86', '\xe9\xbb\x91\xe9\xbe\x99\xe6\xb1\x9f\xe5\x8d\xab\xe8\xa7\x86', '\xe6\x97\xa0\xe5\x8f\xb0\xe6\xa0\x87']
#tv_names = ['CCTV-1','CCTV-10','CCTV-11','CCTV-12','CCTV-13','CCTV-14','CCTV-15','CCTV-2','CCTV-3','CCTV-4','CCTV-5','CCTV-6','CCTV-7','CCTV-8','CCTV-9','东南卫视','东方卫视','东方卫视-娱乐','东方卫视-直播','中央人民广播电台','云南公共','云南卫视','云南国际频道','云南娱乐','云南少儿','云南影视','云南都市','其他','内蒙古卫视','内蒙古卫视蒙语','北京体育','北京卫视','北京少儿','北京影视','北京文艺','北京新闻','北京科教','北京青年','吉林-篮球','吉林乡村','吉林卫视','四川-公共','四川-峨眉电影','四川-康巴卫视','四川sctv-3','四川sctv-5','四川sctv-7','四川sctv-9','四川卫视','四川科教','天津卫视','宁夏卫视','宁夏在线','安徽公共','安徽卫视','安徽导视','安徽影视','安徽综艺','山东公共','山东卫视','山东少儿','山东影视','山东齐鲁','山西卫视','山西少儿','山西影视','广东卫视','广东少儿','广东影视','广东经济科教','广东综艺','广西-科教','广西公共','广西卫视','广西广电网络','广西综艺','延边卫视','新疆10','新疆12','新疆13','新疆2','新疆3','新疆4','新疆5','新疆6','新疆8','新疆9','新疆兵团卫视','新疆卫视','旅游卫视','无台标','江苏卫视','江西-2','江西-3','江西-5','江西卫视','江西指南','河北公共','河北卫视','河北影视','河北经济','河北都市','河南-新农村频道','河南-电视剧频道','河南梨园频道','河南都市频道','浙江公共频道','浙江卫视','浙江民生休闲频道','浙江经济生活','海南旅游','海峡卫视','深圳卫视','深圳生活','湖北体育','湖北卫视','湖北影视','湖北教育','湖北电视台','湖北经视','湖南卫视','湖南国际','湖南电影','湖南电视剧','湖南经视','湖南金鹰卡通','甘肃卫视','福建导视','芒果演艺','西藏卫视','贵州-2','贵州-3','贵州3','贵州4','贵州5','贵州卫视','辽宁公共','辽宁卫视','辽宁宜佳购物','辽宁影视剧','辽宁经济','辽宁都市','重庆-影视','重庆-新闻','重庆-生活资讯','重庆-移动','重庆-精彩重庆','重庆卫视','金鹰卡通','陕西-新闻资讯','陕西卫视','青海tv1','青海tv3-生活','青海卫视','青海藏语','黑龙江-文艺','黑龙江-新闻','黑龙江-都市','黑龙江卫视','Notv']
#tv_names = ['CCTV-1','CCTV-10','CCTV-11','CCTV-12','CCTV-13','CCTV-14','CCTV-15','CCTV-2','CCTV-3','CCTV-4','CCTV-5','CCTV-6','CCTV-7','CCTV-8','CCTV-9','东南卫视','东方卫视','东方卫视-娱乐','东方卫视-直播','云南公共','云南卫视','云南国际频道','云南娱乐','云南少儿','云南影视','云南都市','其他','内蒙古卫视','内蒙古卫视蒙语','北京体育','北京卫视','北京少儿','北京文艺','北京新闻','北京科教','北京青年','吉林-篮球','吉林乡村','吉林卫视','四川-公共','四川-峨眉电影','四川-康巴卫视','四川sctv-3','四川sctv-5','四川sctv-7','四川sctv-9','四川卫视','四川科教','天津卫视','宁夏卫视','宁夏在线','安徽公共','安徽卫视','安徽导视','安徽影视','安徽综艺','山东公共','山东卫视','山东少儿','山东影视','山东齐鲁','山西卫视','山西少儿','山西影视','广东卫视','广东少儿','广东影视','广东经济科教','广东综艺','广西-科教','广西公共','广西卫视','广西广电网络','广西综艺','延边卫视','新疆10','新疆12','新疆13','新疆2','新疆3','新疆4','新疆5','新疆6','新疆8','新疆9','新疆兵团卫视','新疆卫视','旅游卫视','无台标','江苏卫视','江西-2','江西-3','江西-5','江西卫视','江西指南','河北公共','河北卫视','河北影视','河北经济','河北都市','河南-新农村频道','河南-电视剧频道','河南梨园频道','河南都市频道','浙江公共频道','浙江卫视','浙江经济生活','海南旅游','海峡卫视','深圳卫视','深圳生活','湖北体育','湖北卫视','湖北影视','湖北教育','湖北电视台','湖北经视','湖南卫视','湖南国际','湖南电影','湖南电视剧','湖南经视','湖南金鹰卡通','甘肃卫视','福建导视','芒果演艺','西藏卫视','贵州-2','贵州-3','贵州3','贵州4','贵州5','贵州卫视','辽宁公共','辽宁卫视','辽宁宜佳购物','辽宁影视剧','辽宁经济','辽宁都市','重庆-影视','重庆-新闻','重庆-生活资讯','重庆-移动','重庆-精彩重庆','重庆卫视','金鹰卡通','陕西-新闻资讯','陕西卫视','青海tv1','青海tv3-生活','青海卫视','青海藏语','黑龙江-文艺','黑龙江-新闻','黑龙江-都市','黑龙江卫视','Notv']
#tv_names = ['CCTV-1','CCTV-10','CCTV-11','CCTV-12','CCTV-13','CCTV-14','CCTV-15','CCTV-2','CCTV-3','CCTV-4','CCTV-5','CCTV-6','CCTV-7','CCTV-8','CCTV-9','东南卫视','东方卫视','东方卫视-娱乐','东方卫视-直播','中央人民广播电台','云南公共','云南卫视','云南国际频道','云南娱乐','云南少儿','云南影视','云南都市','其他','内蒙古卫视','内蒙古卫视蒙语','北京体育','北京卫视','北京少儿','北京影视','北京文艺','北京新闻','北京科教','北京青年','吉林-篮球','吉林乡村','吉林卫视','四川-公共','四川-峨眉电影','四川-康巴卫视','四川sctv-3','四川sctv-5','四川sctv-7','四川sctv-9','四川卫视','四川科教','天津卫视','宁夏卫视','宁夏在线','安徽公共','安徽卫视','安徽导视','安徽影视','安徽综艺','山东公共','山东卫视','山东少儿','山东影视','山东齐鲁','山西卫视','山西少儿','山西影视','广东卫视','广东少儿','广东影视','广东经济科教','广东综艺','广西-科教','广西公共','广西卫视','广西广电网络','广西综艺','延边卫视','新疆10','新疆12','新疆13','新疆2','新疆3','新疆4','新疆5','新疆6','新疆8','新疆9','新疆兵团卫视','新疆卫视','旅游卫视','江苏卫视','江西-2','江西-3','江西-5','江西卫视','江西指南','河北公共','河北卫视','河北影视','河北经济','河北都市','河南-新农村频道','河南-电视剧频道','河南梨园频道','河南都市频道','浙江公共频道','浙江卫视','浙江民生休闲频道','浙江经济生活','海南旅游','海峡卫视','深圳卫视','深圳生活','湖北体育','湖北卫视','湖北影视','湖北教育','湖北电视台','湖北经视','湖南卫视','湖南国际','湖南电影','湖南电视剧','湖南经视','湖南金鹰卡通','甘肃卫视','福建导视','芒果演艺','西藏卫视','贵州-2','贵州-3','贵州3','贵州4','贵州5','贵州卫视','辽宁公共','辽宁卫视','辽宁宜佳购物','辽宁影视剧','辽宁经济','辽宁都市','重庆-影视','重庆-新闻','重庆-生活资讯','重庆-移动','重庆-精彩重庆','重庆卫视','金鹰卡通','陕西-新闻资讯','陕西卫视','青海tv1','青海tv3-生活','青海卫视','青海藏语','黑龙江-文艺','黑龙江-新闻','黑龙江-都市','黑龙江卫视','Notv']
tv_names = ['Notv','兵团卫视','北京少儿','四川-康巴卫视','四川sctv-3','四川sctv-7','山东齐鲁','广东嘉佳卡通','广东影视','广东珠江','新疆13','湖北电视台','湖北经视','湖南电视剧','湖南经视','湖南金鹰卡通','辽宁都市','重庆-影视','东南卫视','东方卫视','云南卫视','内蒙古卫视','北京卫视','吉林卫视','四川卫视','天津卫视','宁夏卫视','安徽卫视','山东卫视','山西卫视','广东卫视','广西卫视','新疆兵团卫视','新疆卫视','江苏卫视','江西卫视','河北卫视','河南卫视','浙江卫视','深圳卫视','湖北卫视','湖南卫视','甘肃卫视','西藏卫视','贵州卫视','辽宁卫视','重庆卫视','陕西卫视','青海卫视','黑龙江卫视','CCTV-1','CCTV-10','CCTV-11','CCTV-12','CCTV-13','CCTV-14','CCTV-15','CCTV-2','CCTV-3','CCTV-4','CCTV-5','CCTV-6','CCTV-7','CCTV-8','CCTV-9']



'''
0 CCTV-1
1 CCTV-10
2 CCTV-11
3 CCTV-12
4 CCTV-13
5 CCTV-14
6 CCTV-15
7 CCTV-2
8 CCTV-3
9 CCTV-4
10 CCTV-5
11 CCTV-6
12 CCTV-7
13 CCTV-8
14 CCTV-9
15 东南卫视
16 东方卫视
17 云南卫视
18 内蒙古卫视
19 北京卫视
20 吉林卫视
21 四川卫视
22 天津卫视
23 宁夏卫视
24 安徽卫视
25 山东卫视
26 山西卫视
27 广东卫视
28 广西卫视
29 新疆兵团卫视
30 新疆卫视
31 旅游卫视
32 江苏卫视
33 江西卫视
34 河北卫视
35 浙江卫视
36 深圳卫视
37 湖北卫视
38 湖南卫视
39 甘肃卫视
40 西藏卫视
41 贵州卫视
42 辽宁卫视
43 重庆卫视
44 金鹰卡通
45 陕西卫视
46 青海卫视
47 黑龙江卫视
48 无台标
'''


