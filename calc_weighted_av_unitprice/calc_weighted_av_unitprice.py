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
            i_name, i_unitprice, i_hour = input().split()
            print(i_name, i_unitprice, i_hour)
            i_unitprice, i_hour = map(int, (i_unitprice, i_hour))
            self.unitprice_hour_pairs.append(
                {'name': i_name, 'unitprice': i_unitprice, 'hour': i_hour})
        # もともとの総額
        self.raw_amount = 0
        for i_unitprice_hour_pairs in self.unitprice_hour_pairs:
            i_name = i_unitprice_hour_pairs['name']
            i_unitprice = i_unitprice_hour_pairs['unitprice']
            i_hour = i_unitprice_hour_pairs['hour']
            #
            self.raw_amount += i_unitprice * i_hour
        pass

    def calc_weighted_av_unitprice(self):
        self.init()
        # 単金のとりうるレンジ
        allowable_unitprice_range = range(self.allowable_min_unitprice, self.allowable_max_unitprice, self.minunit_of_unitprice)
        # 稼働時間のとりうるレンジ
        totalhour_range = range(self.allowable_min_of_totalhour, self.allowable_max_of_totalhour, 1)
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


if __name__ == '__main__':
    calc = Calc()  
    calc.calc_weighted_av_unitprice()
