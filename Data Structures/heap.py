"""List based heap implementation, heap with minimum value at root"""


class BinHeap():

    def __init__(self):
        self.heap_list = [0]
        self.curr_size = 0

    def perc_up(self, i):
        while i // 2 > 0:
            parent = self.heap_list[i // 2]
            child = self.heap_list[i]
            if parent > child:
                self.heap_list[i // 2], self.heap_list[i] = self.heap_list[i], self.heap_list[i // 2]
            i = i // 2

    def insert(self, val):
        self.heap_list.append(val)
        self.curr_size += 1
        self.perc_up(self.curr_size)

    def min_child(self, i):
        if (i * 2 + 1) > self.curr_size:
            return i * 2
        L_child = self.heap_list[i * 2]
        R_child = self.heap_list[i * 2 + 1]
        if L_child < R_child:
            return i * 2
        else:
            return i * 2 + 1

    def perc_down(self, i):
        while i * 2 <= self.curr_size:
            root = self.heap_list[i]
            min_ch_ix = self.min_child(i)
            if self.heap_list[min_ch_ix] >= root:
                return
            self.heap_list[i], self.heap_list[min_ch_ix] = self.heap_list[min_ch_ix], self.heap_list[i]
            i = min_ch_ix

    def del_min(self):
        min_val = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.curr_size]
        del self.heap_list[self.curr_size]
        self.curr_size -= 1
        self.perc_down(1)
        return min_val

    def build_heap(self, vals):
        ix = len(vals) // 2 #which pos to start perc down from
        self.curr_size = len(vals)
        self.heap_list = [0] + vals
        while(ix > 0):
            self.perc_down(ix)
            ix -= 1

bh = BinHeap()
bh.build_heap([6,5,9,2,4,1])
print(bh.del_min())
print(bh.del_min())
print(bh.del_min())
print(bh.del_min())
print(bh.del_min())
