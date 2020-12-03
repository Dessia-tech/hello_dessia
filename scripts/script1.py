import hello_dessia as hd
import plot_data.core as plot_data

r1 = hd.Rivet(0.005, 0.05, 0.012, 0.005)

# show 3D with babylon
r1.babylonjs()

# show 2D with plot_data
cs = r1.plot_data()
plot_data.plot_canvas(cs.to_dict(), canvas_id='canvas', debug_mode=True)

# rivet_diameter, rivet_length, head_diameter, head_length
rivets_definition = [[0.01, 0.05, 0.012, 0.005],
                     [0.012, 0.05, 0.013, 0.0055],
                     [0.0125, 0.05, 0.014, 0.0057],
                     [0.013, 0.05, 0.016, 0.006],
                     [0.014, 0.05, 0.018, 0.007],
                     [0.0145, 0.05, 0.0185, 0.0071],
                     [0.015, 0.05, 0.0186, 0.0073],
                     ]

# instantiate rivet generator
g1 = hd.Generator(rivets_definition)
solutions = g1.generate()
