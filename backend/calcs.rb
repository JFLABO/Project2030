
# coding: utf-8
require "csv"

sum=0
CSV.foreach("data/.dat", col_sep: "\t", headers: false) do |row|
    # 行に対する処理
    p row
        sum=sum+row[1].to_i
end
print "費用の合計："
print sum
print "\n"
in01=250000
sa01=in01-sum
print sa01
print " 一日あたり:"
day=sa01/(31*2)
print day
print "\n"
