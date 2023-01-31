from parallelHillClimber import PARALLEL_HILL_CLIMBER

#     os.system("python3 generate.py")
#     os.system("python3 simulate.py")

phc = PARALLEL_HILL_CLIMBER()
phc.Evolve()
phc.Show_Best()

# for _ in range(5):
#     generate.fun_g()
#     simulate.fun_s()