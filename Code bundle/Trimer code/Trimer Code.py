import os
path = 'C:/Users/User/Desktop/Pre-processed trimers'
os.chdir(path)

cmd.fetch('4WIZ')
Chainlibrary = cmd.get_chains("all")
print(Chainlibrary)

cmd.create("Best_cloneA", "best_model")
cmd.create("Best_cloneB", "best_model")
cmd.create("Best_cloneC", "best_model")

cmd.align("Best_cloneA", "chain AA")
cmd.align("Best_cloneB", "chain BA")
cmd.align("Best_cloneC", "chain CA")

cmd.delete("best_model")
cmd.delete("4WIZ")

cmd.multifilesave("{name}.pdb")