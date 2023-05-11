import os
path = 'C:/Users/User/Desktop/Pre-processed tetramers'
os.chdir(path)

cmd.fetch('6HTX')
Chainlibrary = cmd.get_chains("all")
print(Chainlibrary)
cmd.split_chains ('6HTX')
cmd.delete("6HTX")

cmd.create("Best_cloneA", "best_model")
cmd.create("Best_cloneB", "best_model")
cmd.create("Best_cloneC", "best_model")
cmd.create("Best_cloneD", "best_model")

cmd.delete("best_model")
cmd.delete("best_model_A")

cmd.align("Best_cloneA", "6HTX_A")
cmd.align("Best_cloneB", "6HTX_B")
cmd.align("Best_cloneC", "6HTX_C")
cmd.align("Best_cloneD", "6HTX_D")

cmd.delete("6HTX_A")
cmd.delete("6HTX_B")
cmd.delete("6HTX_C")
cmd.delete("6HTX_D")

cmd.multifilesave("{name}.pdb")