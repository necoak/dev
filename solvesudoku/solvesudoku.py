import logging
import copy

logging.basicConfig(level=logging.INFO)

SQ_MEMS = [
    [(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)],
    [(3,0), (3,1), (3,2), (4,0), (4,1), (4,2), (5,0), (5,1), (5,2)],
    [(6,0), (6,1), (6,2), (7,0), (7,1), (7,2), (8,0), (8,1), (8,2)],
    [(0,3), (0,4), (0,5), (1,3), (1,4), (1,5), (2,3), (2,4), (2,5)],
    [(3,3), (3,4), (3,5), (4,3), (4,4), (4,5), (5,3), (5,4), (5,5)],
    [(6,3), (6,4), (6,5), (7,3), (7,4), (7,5), (8,3), (8,4), (8,5)],
    [(0, 6), (0, 7), (0, 8), (1, 6), (1, 7), (1, 8), (2, 6), (2, 7), (2, 8)],
    [(3, 6), (3, 7), (3, 8), (4, 6), (4, 7), (4, 8), (5, 6), (5, 7), (5, 8)],
    [(6, 6), (6, 7), (6, 8), (7, 6), (7, 7), (7, 8), (8, 6), (8, 7), (8, 8)],
]

solve_count = 0

class Banmen:
    def __init__(self, banmen):
        self.banmen = banmen

    def create(banmen_matrix):
        new_banmen = Banmen(copy.deepcopy(banmen_matrix))
        return new_banmen

    def clone(self):
        new_banmen = Banmen(copy.deepcopy(self.banmen))
        return new_banmen

    def _calc_candidate(self, gyou_num, retu_num,):
        candidate = list(range(1,10,1))
        # omit gyou
        for i in range(9):
            remove_v = self.banmen[gyou_num][i]
            if remove_v in candidate:
                candidate.remove(remove_v)
        # omit retu
        for i in range(9):
            remove_v = self.banmen[i][retu_num]
            if remove_v in candidate:
                candidate.remove(remove_v)
        # omit square
        for sq_mem in SQ_MEMS:
            if not (gyou_num, retu_num) in sq_mem:
                continue
            for (i,j) in sq_mem:
                remove_v = self.banmen[i][j]
                if remove_v in candidate:
                    candidate.remove(remove_v)

        # 要revise! : 2国同盟法
        return candidate

    def is_complete(self):
        for i in range(9):
            for j in range(9):
                if self.banmen[i][j] == 0:
                    return False
        return True

    def set_val(self, gyou, retu, val):
        self.banmen[gyou][retu] = val

    def calc_candidates(self):
        self.candidates = dict()
        for i in range(9):
            for j in range(9):
                if self.banmen[i][j] == 0:
                    self.candidates[(i,j)] = self._calc_candidate(i, j)

    def get_candidates(self):
        return self.candidates

    def print_candidates(self):
        for k, v in self.candidates.items():
            print(f'{k}: {v}')

    def print_banmen(self):
        for i in range(9):
            if (i in [0, 3, 6]):
                print('+-----+-----+-----+')
            print('|', end='')
            for j in range(9):
                print(self.banmen[i][j], end='')
                if (j in [2, 5, 8]):
                    print('|', end='')
                else:
                    print(' ', end='')
            print()
        print('+-----+-----+-----+')




def solve_sudoku(banmen, mng_dipth, mng_width):
    # mng
    global solve_count
    solve_count += 1
    if solve_count % 10000 == 0:
        print(f'cnt:{solve_count} dipth={mng_dipth} width={mng_width}')
        banmen.print_banmen()

    banmen.calc_candidates()

    candidates = banmen.get_candidates()

    if banmen.is_complete():
        return banmen

    if len(candidates) == 0:
        return None

    cand_len_position_dict = {}

    for (cand_gyou, cand_retu) in list(candidates):
        cand_len = len(candidates[(cand_gyou, cand_retu)])
        if not (cand_len in cand_len_position_dict):
            cand_len_position_dict[cand_len] = [(cand_gyou, cand_retu)]
        else:
            cand_len_position_dict[cand_len].append((cand_gyou, cand_retu))

    cand_len_min = min(list(cand_len_position_dict))
    for (cand_gyou, cand_retu) in cand_len_position_dict[cand_len_min]:
        mng_width2 = mng_width # mng
        for cand_val in candidates[(cand_gyou, cand_retu)]:
            next_banmen = banmen.clone()
            next_banmen.set_val(cand_gyou, cand_retu, cand_val)
            answer_banmen = solve_sudoku(next_banmen, mng_dipth+1, mng_width2)
            if answer_banmen is not None:
                return answer_banmen
            mng_width2 += 1 # mng
    return None





def main():
    in_banmen_matrix = []
    for i in range(9):
        gyo_text = input()
        gyo = []
        for item_chr in gyo_text.split():
            if item_chr == '#':
                item_num = 0
            else:
                item_num = int(item_chr)
            gyo.append(item_num)
        in_banmen_matrix.append(gyo)
    banmen = Banmen.create(in_banmen_matrix)
    answer_banmen = solve_sudoku(banmen, 0, 0)
    if answer_banmen is None:
        print('回答はありませんでした')
    else:
        print('回答はこちらです')
        answer_banmen.print_banmen()

if __name__ == '__main__':
    main()
