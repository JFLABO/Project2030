# coding: utf-8
# 2023/12/29 21:06:08　在校生へ　OB訪問を開催します。
# 事業が軌道に乗るまでNEDOやJAXAの管理下にいなさい　
# 研究の枠組み　科研費の申請のやり方について
require 'date'
today = Date.new(2023,12,29)
future = Date.new(2024, 1, 4)

time = Time.now

year = time.year
month = time.month
day = time.day
hour = time.hour
min = time.min
sec = time.sec
puts "今日は" + year.to_s + "年" + month.to_s + "月" + day.to_s + "日です。"
puts "今は" + hour.to_s + "時" + min.to_s + "分" + sec.to_s + "秒です。"
week = ["日曜日", "月曜日", "火曜日", "水曜日", "木曜日", "金曜日", "土曜日"]
puts week[time.wday] +"です。"

remainingDay = future -today
puts "目標日は" + future.to_s
puts "目標の日まであと" + remainingDay.to_i.to_s + "日です。"
