import hello_dessia as hd
import plot_data.core as plot_data
import volmdlr as vm

p1 = hd.Panel(1, 1, 0.01)
p2 = hd.Panel(1.1, 1, 0.01)
# p1.babylonjs()

# c = p1.plot_data()
# plot_data.plot_canvas([c.to_dict()], 'contour')

r1 = hd.Rivet(0.01, 0.05, 0.012, 0.005)
# r1.babylonjs()

# c = r1.plot_data(False)
# plot_data.plot_canvas([c.to_dict()], 'contour')

pc1 = hd.PanelCombination([p1, p2], [vm.Point3D(0, 0, 0), vm.Point3D(0.7, 0.2, 0.01)])
sol = pc1.intersection_area()
c3 = sol.plot_data()
cs = pc1.plot_data()
# plot_data.plot_canvas([c.to_dict() for c in [cs[0], cs[1], c3]], 'contour')

rule1 = hd.Rule(0.1, 0.2)
all_possibilities = rule1.define_number_rivet(sol, r1)

g1 = hd.Generator(pc1, r1, rule1)
solutions = g1.generate()

cs = solutions[-1].plot_data()
plot_data.plot_canvas([c.to_dict() for c in cs], 'contour')