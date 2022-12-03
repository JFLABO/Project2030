from pyquery import PyQuery
import datetime
class Point:
        #def __init__(self, x, y):
                #self._x = x
                #self._y = y

        #def output(self):
                #print('Point(%d, %d)' % (self._x, self._y))
        def a(self,code):
                print ("=========")
                print(datetime.datetime.today())
                #q=PyQuery('https://kabutan.jp/stock/?code=8601')              \

                q=PyQuery('https://kabutan.jp/stock/?code='+code)
                #sector=q.find('table.kobetsu_data_table2 a')[0].text          \

                sector = q.find('#stockinfo_i2 > div > a').text()
                print(sector)
                sector2 = q.find('.kabuka').text()
                print(sector2)
                sector3 = q.find('.si_i1_1').text()
                print(sector3)
                sector4 = q.find('#stockinfo_i3').text()
                print(sector4)
                #sector5 = q.find('.gyouseki_block').text()
                #print(sector5)
p1 = Point()
#mylist = ['6632','9973','4337','9681','7860','9945','7974','6758','6460','7832\
','6501','2791','3038','6632','6178','8214','7211','6702','3778','1802','9684']
mylist = ['7860','9945','7974','6758','6460','7832','6501','2791','3038','6632'\
,'6178','8214','7211','6702','9684','1802','9973']
#大林組(1802)
for code in mylist:
        p1.a(code)
