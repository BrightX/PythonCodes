txt = '''
    储存盒即时存档消耗品储存箱
    即时存档非消耗品EXP自造器移
    动时自动增加经验值与金钱自
    造器二选一在水怪山洞旁营地领
    取赏金时低几率奖励金钱自造器
    移动时自动增加金钱
    '''

# 统计字频，从高到低排序
co = {}
for i in txt:
    if i in ['','\n', ' ']:
        continue
    co[i] = co.get(i, 0) + 1
it = list(co.items())
it.sort(key=lambda x:x[1], reverse=True)
for i in range(len(it)):
    w, c = it[i]
    print("{0:<10}{1:>5}".format(w, c))
