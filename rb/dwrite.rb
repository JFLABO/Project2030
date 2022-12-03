# coding: utf-8
require 'json'
s="136-0071_2-13-12_"
date="2022/12/03 17:06:06"
date=date.delete("/")
date=date.delete(" ")
File.open("data/"+s+date+".json", "w") do |file|
  hash = {"ID" => 1,
          "title" => "豚肉を熱して食べる　定義書　隊員と隊列",
          "project"=>"2030project",
          "content" => "日程管理スタート　定義"}
  JSON.dump(hash, file)
end

