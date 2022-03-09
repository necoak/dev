#!/usr/bin/env python3
from decimal import Decimal
from decimal import ROUND_HALF_UP
import itertools

class Calc:
    
    def init(self):
        self.num_of_person = int(input()) # 人数

        self.allowable_min_unitprice = int(input()) # 許容最小単金
        self.allowable_max_unitprice = int(input()) # 許容最大単金
        self.minunit_of_unitprice = int(input())    # 単金最小単位

        self.allowable_min_of_monthhour = int(input()) # 許容最小人時/1人月
        self.allowable_max_of_monthhour = int(input()) # 許容最大人時/1人月
        self.minunit_of_monthhour = int(input())    # 月時間数最小単位

        self.allowable_min_of_amount = int(input()) # 許容最小総額
        self.allowable_max_of_amount = int(input()) # 許容最大総額
        self.minunit_of_amount = int(input()) # 総額最小単位

        self.allowable_min_of_totalhour = int(input()) # 許容最小稼働時間
        self.allowable_max_of_totalhour = int(input()) # 許容最大稼働時間
        #
        self.unitprice_hour_pairs = []
        for i in range(self.num_of_person):
            i_name, i_allowable_min_unitprice, i_allowable_max_unitprice, i_minunit_of_unitprice, \
                i_allowable_min_hour, i_allowable_max_hour,  i_minunit_of_hour = input().split()
            # print(i_name, i_unitprice, i_hour)
            #i_unitprice, i_hour = map(int, (i_unitprice, i_hour))
            self.unitprice_hour_pairs.append(
                {'name': i_name, 
                 'allowable_min_unitprice': int(i_allowable_min_unitprice),
                 'allowable_max_unitprice': int(i_allowable_max_unitprice),
                 'minunit_of_unitprice': int(i_minunit_of_unitprice),
                 'allowable_min_hour': int(i_allowable_min_hour),
                 'allowable_max_hour': int(i_allowable_max_hour),
                 'minunit_of_hour': int(i_minunit_of_hour)})
        
        
    def calc_weighted_av_unitprice(self):
        self.init()
        # 単金のとりうるレンジ
        #allowable_unitprices = list(range(self.allowable_min_unitprice, self.allowable_max_unitprice, self.minunit_of_unitprice))
        # 稼働時間のとりうるレンジ
        #allowable_totalhours = list(range(self.allowable_min_of_totalhour, self.allowable_max_of_totalhour, 1))
        # 1人月時間のとりうるレンジ
        monthhour_range = range(self.allowable_min_of_monthhour, self.allowable_max_of_monthhour, self.minunit_of_monthhour)
        ## 人月のとりうるレンジ
        #manhour_range = range(0, 100, self.minunit_of_manhour) # todo

        ans_cnt = 0
        unitprice_hour_patterns = self.get_unitprice_hour_patterns()
        #print(list(unitprice_hour_patterns))
        for unitprice_hour_pattern in unitprice_hour_patterns:
            #print('.', end='')
            total_hour = 0
            total_price = 0
            for i_unitprice_hour in unitprice_hour_pattern:
                #print(i_unitprice_hour)
                #print(i_unitprice_hour['hour'])
                total_hour += i_unitprice_hour['hour']
                total_price += i_unitprice_hour['price']
            
            # 総額が条件にはまるか
            if not(self.allowable_min_of_amount <= total_price <= self.allowable_max_of_amount):
                #print('err1: ' + str(unitprice_hour_pattern))
                continue

            # 加重平均単金を計算
            wav_unit_price = total_price // total_hour
            # 加重平均単金は条件にはまるか
            ## 加重平均単金が割り切れること
            if (total_price % total_hour) != 0:
                #print('err2: ' + str(unitprice_hour_pattern))
                continue
            ## 加重平均単金が最小単位以上であること
            if wav_unit_price % self.minunit_of_unitprice != 0:
                #print('err3: ' + str(unitprice_hour_pattern))
                continue
            ## 加重平均単金が許容範囲内に収まっていること
            if not(self.allowable_min_unitprice <= wav_unit_price <= self.allowable_max_unitprice):
                #print('err3: ' + str(unitprice_hour_pattern))
                continue
            # 時間数が条件にはまるか
            if not(self.allowable_min_of_totalhour <= total_hour <= self.allowable_max_of_totalhour):
                #print('err4: ' + str(unitprice_hour_pattern))
                continue
            # 人月換算は条件にはまるか
            matched_month_hours = []
            for month_hour in monthhour_range:
                tmp_total_hour = total_hour * 1000
                if tmp_total_hour % month_hour != 0:
                    continue
                matched_month_hours.append(month_hour)
            if len(matched_month_hours) == 0:
                #print('err5: ' + str(unitprice_hour_pattern))
                continue
            
            for month_hour in matched_month_hours:
                print(
                    '総額:' + str(total_price) + 
                    ' 単金:' + str(wav_unit_price) +
                    ' 時間:' + str(total_hour) +
                    ' 時間/1人月:' + str(month_hour) +
                    ' 人月:' + str(total_hour // month_hour) + '.' +str( ((total_hour % month_hour)*1000)//month_hour) + 
                    ' 単金組合せ:' + str(unitprice_hour_pattern))
                ans_cnt += 1
            
        if ans_cnt == 0:
            print('Answer doesnt exist.')
        else:
            print('Answer cnt: ' + str(ans_cnt))

    def calc_manmonth(self, hour, monthhour):
        return Decimal(hour / monthhour).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    
    def get_unitprice_hour_patterns(self):
        each_patterns = []
        for unitprice_hour_pair in self.unitprice_hour_pairs:
            each_patterns.append(self.get_unitprice_hour_pattern(unitprice_hour_pair))
        kumiawase_patterns = self.get_patterns(each_patterns, [], [])
        return kumiawase_patterns
    
    def get_patterns(self, patterns, selected, kumiawase):
        if len(patterns) == 0:
            kumiawase.append(selected)
            return kumiawase
        patterns1 = patterns[0]
        for pattern in patterns1:
            tmp_selected = selected + [pattern]
            kumiawase = self.get_patterns(patterns[1:], tmp_selected, kumiawase)
        return kumiawase

    def get_unitprice_hour_pattern(self, unitprice_hour_pair):
        result = []
        for i_unitprice in range(unitprice_hour_pair['allowable_min_unitprice'], unitprice_hour_pair['allowable_max_unitprice']+1, unitprice_hour_pair['minunit_of_unitprice']):
            for i_hour in range(unitprice_hour_pair['allowable_min_hour'], unitprice_hour_pair['allowable_max_hour']+1, unitprice_hour_pair['minunit_of_hour']):
                result.append(
                    {'name': unitprice_hour_pair['name'],
                     'hour': i_hour,
                     'unitprice': i_unitprice,
                     'price': i_hour * i_unitprice
                    })
        return result
        
if __name__ == '__main__':
    calc = Calc()  
    calc.calc_weighted_av_unitprice()
