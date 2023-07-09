from glass import *
import glob

files = glob.glob("./AGF/*.agf")

manager = GlassCatalogManager()
manager.load_agf_files(files)
manager.set_temperature(25)


def get_operand1(g):
    return g.refractive_index(SpectralLine.d/1000.0)

def get_operand2(g):
    nd = g.refractive_index(SpectralLine.d/1000.0)
    nF = g.refractive_index(SpectralLine.F/1000.0)
    nC = g.refractive_index(SpectralLine.C/1000.0)

    vd = (nd-1)/(nF-nC)
    return vd

def merit_func(g, operands, targets, weights):
    err = 0.0
    for i in range(len(operands)):
        err += weights[i]*(operands[i](g) - targets[i])**2
        
    return err



operands = [get_operand1, get_operand2]
targets = [1.51633, 64.14]
weights = [1.0, 0.001]

results_count = 5
search_results = []

for catalog in manager.catalogs:
    for g in catalog.glasses:
        err = merit_func(g, operands, targets, weights)

        current = [g, err]

        if not search_results:
            search_results.append(current)
        else:
            for i, r in enumerate(search_results):
                if err < r[1]:
                    search_results.insert(i,current)
                    if len(search_results) > results_count:
                        search_results.pop(-1)
                    break

for r in search_results:
    g = r[0]
    print("{:<10} : {:.5f}, {:2f}".format(g.product_name, get_operand1(g), get_operand2(g)))

