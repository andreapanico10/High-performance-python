import pstats

# python -m cProfile -o profile.stats julia.py      

p = pstats.Stats("profile.stats")
p.sort_stats("cumulative")
#p.print_stats()
#p.print_callers()
p.print_callees()