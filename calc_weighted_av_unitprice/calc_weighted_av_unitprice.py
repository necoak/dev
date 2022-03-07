#!/usr/bin/env python3
from decimal import Decimal
from decimal import ROUND_HALF_UP

class Calc:
    
    def init(self):
        self.num_of_person = int(input()) # 人数

        self.allowable_min_unitprice = int(input()) # 許容最小単金
        self.allowable_max_unitprice = int(input()) # 許容最大単金
        self.minunit_of_unitprice = int(input())    # 単金最小単位

        self.allowable_min_of_monthhour = 150 # 許容最小人時/1人月
        self.allowable_max_of_monthhour = 200 # 許容最大人時/1人月
        self.minunit_of_monthhour = int(input())    # 月時間数最小単位

        self.minunit_of_manhour = Decimal(input()) # 人月最小単位

        self.allowable_min_of_amount = int(input()) # 許容最小総額
        self.allowable_max_of_amount = int(input()) # 許容最大総額
        self.minunit_of_amount = int(input()) # 総額最小単位

        self.allowable_min_of_totalhour = int(input()) # 許容最小稼働時間
        self.allowable_max_of_totalhour = int(input()) # 許容最大稼働時間
        #
        self.unitprice_hour_pairs = []
        for i in range(self.num_of_person):
            i_name, i_allowable_max_unitprice, i_allowable_min_unitprice, i_minunit_of_unitprice, \
                i_allowable_max_hour, i_allowable_min_hour,  i_minunit_of_hour = input().split()
            # print(i_name, i_unitprice, i_hour)
            #i_unitprice, i_hour = map(int, (i_unitprice, i_hour))
            self.unitprice_hour_pairs.append(
                {'name': i_name, 
                 'allowable_max_unitprice': int(i_allowable_max_unitprice),
                 'allowable_min_unitprice': int(i_allowable_min_unitprice),
                 'minunit_of_unitprice': int(i_minunit_of_unitprice),
                 'allowable_max_hour': int(i_allowable_max_hour),
                 'allowable_min_hour': int(i_allowable_min_hour),
                 'minunit_of_hour': i_minunit_of_hour}
        

    def calc_weighted_av_unitprice(self):
        self.init()
        # 単金のとりうるレンジ
        allowable_unitprices = list(range(self.allowable_min_unitprice, self.allowable_max_unitprice, self.minunit_of_unitprice))
        # 稼働時間のとりうるレンジ
        allowable_totalhours = list(range(self.allowable_min_of_totalhour, self.allowable_max_of_totalhour, 1))
        # 1人月時間のとりうるレンジ
        monthhour_range = range(self.allowable_min_of_monthhour, self.allowable_max_of_monthhour, self.minunit_of_monthhour)
        ## 人月のとりうるレンジ
        #manhour_range = range(0, 100, self.minunit_of_manhour) # todo



        for unitprice in allowable_unitprice_range:
            for totalhour in totalhour_range:
                for monthhour in monthhour_range:
                    amount1 = unitprice * totalhour
                    if amount1 < self.allowable_min_of_amount:
                        continue
                    if amount1 > self.allowable_max_of_amount:
                        continue
                    manhour = Decimal(totalhour / monthhour,).quantize(Decimal('0.01'),rounding=ROUND_HALF_UP)
                
                    if (manhour * monthhour) != totalhour:
                        continue
                        
                    print('総額: ' + str(amount1) + '単金: ' + str(unitprice) + ' 時間: ' + str(totalhour) + '時間/1人月: ' + str(monthhour) + ' 人月: ' + str(manhour))

    def calc_manmonth(self, hour, monthhour):
        return Decimal(hour / monthhour).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    
    def get_unitprice_hour_patterns(self):
        result = []
        for unitprice_hour_pair in self.unitprice_hour_pairs:
            result.append(self.get_unitprice_hour_pattern(unitprice_hour_pair))
        return result
    
    def get_unitprice_hour_pattern(self, unitprice_hour_pair):
        result = []
        for i_unitprice in range(unitprice_hour_pair['allowable_min_unitprice'], unitprice_hour_pair['allowable_max_unitprice'], unitprice_hour_pair['minunit_of_unitprice']):
            for i_hour in range(unitprice_hour_pair['allowable_min_hour'], unitprice_hour_pair['allowable_max_hour'], unitprice_hour_pair['minunit_of_hour']):
                result.append(
                    {'name': unitprice_hour_pair['name'],
                     'hour': i_hour,
                     'unitprice': i_unitprice
                    })
        return result
        
if __name__ == '__main__':
    calc = Calc()  
    calc.calc_weighted_av_unitprice()
